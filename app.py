import streamlit as st
import pickle
import pandas as pd
import requests


movies_dict = pickle.load(open('movies_dict_df.pkl','rb'))
similar = pickle.load(open('similarity.pkl','rb'))

## movies_df is now orignal dataframe that is df in jupyter
movies_df= pd.DataFrame(movies_dict)
st.title("Welcome to Movies Recommender")
selected_movie =st.selectbox('Our Recommendation for you', movies_df['title'].values)



## extra work here

def fetch_video(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/videos?api_key=79f73722a4be7e9c258f76ff6695895f&language=en-US'.format( movie_id))
    data = response.json()
    return  'https://www.youtube.com/watch?v='+data['results'][0]['key']




def poster_fetching(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=79f73722a4be7e9c258f76ff6695895f&language=en-US'.format(movie_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
## poster_fetching return poster path of each movie id from api



## function that return recommended movies name
def Recommender(selected_movie):
    movie_index = movies_df[movies_df['title'] == selected_movie].index[0]
    distance = similar[movie_index]
    movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommeneded=[]
    recommeneded_movie_poster=[]
    recommeneded_movie_video = []
    for i in movies:
        movies_id=movies_df.iloc[i[0]].movie_id
        recommeneded.append(movies_df.iloc[i[0]].title)
        recommeneded_movie_poster.append(poster_fetching(movies_id))
        recommeneded_movie_video.append(fetch_video(movies_id))
    return  recommeneded,recommeneded_movie_poster,recommeneded_movie_video
## recommended is list which  contain top 5 recommende movies name and recommended_movie_poster contain poster of each movie

## button for recommender
if st.button('Recommend'):
    recommened_list,recommended_poster,recommended_video= Recommender(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommened_list[0])
        st.image(recommended_poster[0])

    with col2:
        st.text(recommened_list[1])
        st.image(recommended_poster[1])

    with col3:
        st.text(recommened_list[2])
        st.image(recommended_poster[2])

    with col4:
        st.text(recommened_list[3])
        st.image(recommended_poster[3])

    with col5:
        st.text(recommened_list[4])
        st.image(recommended_poster[4])
    st.subheader("Trailers ")

    with st.container():
        st.video(recommended_video[0])
        st.video(recommended_video[1])
        st.video(recommended_video[2])
        st.video(recommended_video[3])
        st.video(recommended_video[4])
    st.caption("Rohit_Aggarwal")

