import streamlit as st
import requests
import pickle
import gzip



#Load pickle files
movies = pickle.load(gzip.open('./artifacts/movies_data.pkl.gz', 'rb'))
movies_list = movies['title'].values

similarity = pickle.load(gzip.open('./artifacts/similarity.pkl.gz', 'rb'))


#Functions
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key= lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_movie_posters


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


#Page Layout
st.set_page_config(page_title="Recommendation Engine", page_icon="®️", layout='centered')
st.title("®️ Recommendation Engine")

selected_movie_name = st.selectbox(label="Movie", options=movies_list)


#Button
st.divider()
if st.button("Recommend"):

    recommended_movies, recommended_movie_posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movies[idx])
            st.image(recommended_movie_posters[idx])
    
