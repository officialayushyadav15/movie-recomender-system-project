import numpy as np
import pandas as pd
import ast

movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")

# merge the dataframes on title
movies = movies.merge(credits, on='title')

# included columns: genres, id, keywords, title, overview, cast, crew
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# now we basically need three columns movie_id, title and tags where tags comprises the combined data of overview, cast, crew, genres and keywords data so in order to do this we have to do preprocessing of data
movies.dropna(inplace=True)

def convert(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l

movies['genres'] = movies['genres'].apply(convert)

movies['keywords'] = movies['keywords'].apply(convert)

def convert5(obj):
    l=[]
    c=0
    for i in ast.literal_eval(obj):
        l.append(i['name'])
        c=c+1
        if(c==5):
            break
    return l

movies['cast'] = movies['cast'].apply(convert5)

def director(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            l.append(i['name'])
            break
    return l

movies['crew'] = movies['crew'].apply(director)

movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])

movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])

movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])

movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies['tags'] = movies['genres'] + movies['keywords'] + movies['overview'] + movies['cast'] + movies['crew']

new_df = movies[['movie_id','title','tags']]

new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))

new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

new_df.to_csv("dataset/data.csv", index=False)