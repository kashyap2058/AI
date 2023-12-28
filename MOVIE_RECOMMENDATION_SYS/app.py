import streamlit as st 
import pickle
import requests


movies = pickle.load(open(r'C:/Users/Kashyap Ghimire/Desktop/AI training/NLP/Movie Recommendation/movies_data.pkl','rb'))
movies_list=movies['title'].values
similarity=pickle.load(open(r'C:/Users/Kashyap Ghimire/Desktop/AI training/NLP/Movie Recommendation/similarity.pkl','rb'))
st.header("Movie Recommender")
selected_movie=st.selectbox("Select movies from dropdown", movies_list)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=a60b37e4681a6bb1a32b73ce141b4903&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     print(data)
     poster_path =data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path    

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster


if st.button("Show Recommended"):
    movie_names,poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(poster[0])
    with col2:
        st.text(movie_names[1])
        st.image(poster[1])
    with col3:
        st.text(movie_names[2])
        st.image(poster[2])
    with col4:
        st.text(movie_names[3])
        st.image(poster[3])
    with col5:
        st.text(movie_names[4])
        st.image(poster[4])