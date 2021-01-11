#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re

import numpy as np

# Read csvs

path = 'C:\\P\\IA\\Practica_2\\krelboynes_proyecto_2\\ml-latest-small\\ml-latest-small\\'

# links.csv will not be used
# df_links = pd.read_csv(path + 'links.csv')

df_movies = pd.read_csv(path + 'movies.csv')
df_ratings = pd.read_csv(path + 'ratings.csv')
df_tags = pd.read_csv(path + 'tags.csv')

# print(df_links.head())
print(df_movies.head())
print(df_ratings.head())
print(df_tags.head())


# In[2]:


print(len(df_movies['title']))
#df_movies['title'][20]


# In[3]:


# Extract (year) from df_movies['title']
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    
year = []


    
for i in range(0,len(df_movies['title'])):
    if ") (2" in df_movies['title'][i]:
        year.append('2' + find_between(df_movies['title'][i],") (2", ")"))
    elif ") (1" in df_movies['title'][i]:
        year.append('1' + find_between(df_movies['title'][i],") (1", ")"))
    elif " (2" in df_movies['title'][i]:
        year.append('2' + find_between(df_movies['title'][i]," (2", ")"))
    elif " (1" in df_movies['title'][i]:
        year.append('1' + find_between(df_movies['title'][i]," (1", ")"))
    else:
        year.append(find_between(df_movies['title'][i],"(", ")"))
        
df_movies['Release_Year'] = year


# In[4]:


print(df_movies)


# In[5]:


# Row 9518 has the value '2006-2007' in Release_Year it will be replaced with the value 2006
# print(df_movies['Release_Year'][9518])

# df_movies['Release_Year'][9518] = 2006
df_movies.loc[[9518],['Release_Year']] = 2006

# Remove all records without defined Release_Year
df_movies = df_movies[(df_movies['Release_Year'] != "" )]

df_movies.reset_index(drop=True, inplace=True)

df_movies.to_csv(path + 'movies_2.csv')

print(df_movies)


# In[6]:


# Convert Release_Date to 
#print(df_movies['Release_Year'].dtype)

df_movies['Release_Year'] = pd.to_numeric(df_movies['Release_Year'])
print(df_movies['Release_Year'].dtype)


# In[7]:


# Generate 19 columns with 0s or 1s if it belongs to the individual genre
Action_col = []
Adventure_col = []
Animation_col = []
Children_col = []
Comedy_col = []
Crime_col = []
Documentary_col = []
Drama_col = []
Fantasy_col = []
Film_Noir_col = []
Horror_col = []
Musical_col = []
Mystery_col = []
Romance_col = []
Sci_Fi_col = []
Thriller_col = []
War_col = []
Western_col = []
No_Genre_Listed_col = []

#print(len(df_movies['genres']))

for i in range(0,len(df_movies['genres'])):
    
    Action = 0
    Adventure = 0
    Animation = 0
    Children = 0
    Comedy = 0
    Crime = 0
    Documentary = 0
    Drama = 0
    Fantasy = 0
    Film_Noir = 0
    Horror = 0
    Musical = 0
    Mystery = 0
    Romance = 0
    Sci_Fi = 0
    Thriller = 0
    War = 0
    Western = 0
    No_Genre_Listed = 0
    
    s = str(df_movies['genres'][i])
    
    if "Action" in s:
        Action = 1
        
    if "Adventure" in s:
        Adventure = 1
    
    if "Animation" in s:
        Animation = 1
        
    if "Children's" in s:
        Children = 1
    
    if "Comedy" in s:
        Comedy = 1
    
    if "Crime" in s:
        Crime = 1
    
    if "Documentary" in s:
        Documentary = 1
    
    if "Drama" in s:
        Drama = 1
    
    if "Fantasy" in s:
        Fantasy = 1
        
    if "Film-Noir" in s:
        Film_Noir = 1
    
    if "Horror" in s:
        Horror = 1
    
    if "Musical" in s:
        Musical = 1
    
    if "Mystery" in s:
        Mystery = 1
    
    if "Romance" in s:
        Romance = 1
        
    if "Sci-Fi" in s:
        Sci_Fi = 1
    
    if "Thriller" in s:
        Thriller = 1
    
    if "War" in s:
        War = 1
    
    if "Western" in s:
        Western = 1
    
    if "(no genres listed)" in s:
        No_Genre_Listed = 1
    
    
    Action_col.append(Action)
    Adventure_col.append(Adventure)
    Animation_col.append(Animation)
    Children_col.append(Children)
    Comedy_col.append(Comedy)
    Crime_col.append(Crime)
    Documentary_col.append(Documentary)
    Drama_col.append(Drama)
    Fantasy_col.append(Fantasy)
    Film_Noir_col.append(Film_Noir)
    Horror_col.append(Horror)
    Musical_col.append(Musical)
    Mystery_col.append(Mystery)
    Romance_col.append(Romance)
    Sci_Fi_col.append(Sci_Fi)
    Thriller_col.append(Thriller)
    War_col.append(War)
    Western_col.append(Western)
    No_Genre_Listed_col.append(No_Genre_Listed)
    
df_movies['Action_genre'] = Action_col
df_movies['Adventure_genre'] = Adventure_col
df_movies['Animation_genre'] = Animation_col
df_movies['Children_genre'] = Children_col
df_movies['Comedy_genre'] = Comedy_col
df_movies['Crime_genre'] = Crime_col
df_movies['Documentary_genre'] = Documentary_col
df_movies['Drama_genre'] = Drama_col
df_movies['Fantasy_genre'] = Fantasy_col
df_movies['Film_Noir_genre'] = Film_Noir_col
df_movies['Horror_genre'] = Horror_col
df_movies['Musical_genre'] = Musical_col
df_movies['Mystery_genre'] = Mystery_col
df_movies['Romance_genre'] = Romance_col
df_movies['Sci_Fi_genre'] = Sci_Fi_col
df_movies['Thriller_genre'] = Thriller_col
df_movies['War_genre'] = War_col
df_movies['Western_genre'] = Western_col
df_movies['No_Genre_Listed_genre'] = No_Genre_Listed_col
    

print(len(Action_col))


# In[8]:


# Compute the Q_4 quartile for movie's ratings
Q4_ratings = np.quantile(df_ratings[['rating']],0.75)
Q4_ratings


# In[9]:


# Evaluate the given rating and compare it with Q4_ratings, 
like_array = []

for i in range(0,len(df_ratings[['rating']])):
    if df_ratings['rating'][i] < Q4_ratings:
        like_array.append(0)
    else:
        like_array.append(1)

#print(like_array)
df_ratings['like'] = like_array
print(df_ratings)


# In[10]:


# Pivot the binary rating using userId as rows and movieId columns columns
df_user_item = df_ratings.pivot(index='userId', columns='movieId')['like']
df_user_item


# In[11]:


df_user_item = df_user_item.fillna(0)


# In[ ]:




