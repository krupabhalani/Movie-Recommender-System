import streamlit as st
import pandas as pd
import pickle
import requests

st.title("Movie Recommender System")
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
selected_movie_name = st.selectbox(':popcorn::cd:', movies['title'].values, index=None, placeholder="Enter Movie Name...")

similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8c97576894166c82f3558f0da71f47d7&language=en-US".format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))  # fetch poster from API
    return recommended_movies, recommended_movies_posters


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.caption(names[0])
        st.image(posters[0])
    with col2:
        st.caption(names[1])
        st.image(posters[1])
    with col3:
        st.caption(names[2])
        st.image(posters[2])
    with col4:
        st.caption(names[3])
        st.image(posters[3])
    with col5:
        st.caption(names[4])
        st.image(posters[4])
    with col6:
        st.caption(names[5])
        st.image(posters[5])
    with col7:
        st.caption(names[6])
        st.image(posters[6])
    with col8:
        st.caption(names[7])
        st.image(posters[7])
    with col9:
        st.caption(names[8])
        st.image(posters[8])
    with col10:
        st.caption(names[9])
        st.image(posters[9])
