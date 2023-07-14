import streamlit as st
import pickle
import pandas as pd
import bz2

st.title('Anime Recommender System')

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
print(movies.head())


similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    m_index = movies[movies['name'] == movie].index[0]
    distances = similarity[m_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_movies=[]
    for i in movies_list:
        # print(movies.iloc[i[0]].name)
        # print(movie['name'][movies.iloc[i[0]]])
        recommended_movies.append(movies.iloc[i[0]])

    return recommended_movies

option = st.selectbox(
'Enter the name of an Anime',
movies['name'].values
)

if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)