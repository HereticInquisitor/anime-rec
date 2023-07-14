import numpy as np
import pandas as pd
import os

movies=pd.read_csv('anime.csv')
movies.head()

movies=movies[['anime_id', 'name', 'genre']]

movies.head()

print(movies.shape)
movies.dropna(inplace=True)
print(movies.shape)
movies['genre'].isnull().sum()

from sklearn.feature_extraction.text import CountVectorizer
cv= CountVectorizer(max_features=5000,stop_words='english')

vc=cv.fit_transform(movies['genre']).toarray()
vc.shape

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vc)
similarity[0]

sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x:x[1])

movies[movies['name'] =='Kimi no Na wa.'].index[0]

def recommend(movie):
    m_index=movies[movies['name'] == movie].index[0]
    distances = similarity[m_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:11]

    for i in movies_list:
        # print(movies.iloc[i[0]].name)
        print(movies.iloc[i[0]])

recommend('Steins;Gate')

import pickle
import bz2

pickle.dump(movies.to_dict(), bz2.open('movies_dict.pkl','wb'))
pickle.dump(similarity,bz2.open('similarity.pkl','wb'))

