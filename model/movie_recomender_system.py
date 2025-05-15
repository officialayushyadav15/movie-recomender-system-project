import numpy as np
import pandas as pd
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

new_df = pd.read_csv("dataset/data.csv")

# now we do vectorisation to see the movie and recomend nearest vectors for this we use bag of words

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()

# now we do stemming

ps = PorterStemmer()

def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

vectors = cv.fit_transform(new_df['tags']).toarray()

# now we detect codine distance (i.e. anglr between two vectors) instead of euclidian distance(distance between tip of data) because in higher dimensions euclidian distance is not that effective. Also rember distance is directly proportional to similarity

similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]

    distance = similarity(vectors)

    movies_list = sorted(list(enumerate(distance)),reverse = True, key = lambda x:x[1])[1:11]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))

pickle.dump(similarity,open('similarity.pkl','wb'))