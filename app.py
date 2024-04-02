import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommended_movies = []

    for i in distance[0:5]:
        #movie_id = i[0]
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movies Recommender System")

selected_movie = st.selectbox(
    'How to contact you?',
    movies['title'].values
)
if st.button('Recommend:'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)