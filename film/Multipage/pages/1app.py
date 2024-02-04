import requests 
from pathlib import Path
import streamlit as st
#import streamlit_authenticator as stauth

from streamlit_extras.switch_page_button import switch_page 
 


st.title("WELCOME TO CINEMA BOX")
st.sidebar.success("Pilih halaman diatas")
with open("logged_in.txt", "r") as logged_in:
      st.sidebar.success(logged_in.read())
      

if st.sidebar.button("logout"):
   switch_page("login")
   
st.header("Rekomendasi Film Action")

if st.button("Rekomendasi Action"): 
   switch_page("Action")

query = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=28&api_key=daa72e5129266ed8b88b414c034ff362"
movies = requests.get(query).json()["results"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[0]['poster_path'] }", caption=f'⭐{movies[0]["vote_average"]}')
      st.text(movies[0]["title"])
with col2:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[1]['poster_path'] }", caption=f'⭐{movies[1]["vote_average"]}')
      st.text(movies[1]["title"])
with col3:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[2]['poster_path'] }", caption=f'⭐{movies[2]["vote_average"]}')
      st.text(movies[2]["title"])
with col4:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[3]['poster_path'] }", caption=f'⭐{movies[3]["vote_average"]}')
      st.text(movies[3]["title"])
with col5:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[4]['poster_path'] }", caption=f'⭐{movies[4]["vote_average"]}')
      st.text(movies[4]["title"])


st.header("Rekomendasi Film Animasi")
if st.button("Rekomendasi Animasi"): 
      switch_page("Animasi")


query = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=16&api_key=daa72e5129266ed8b88b414c034ff362"
movies = requests.get(query).json()["results"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[0]['poster_path'] }", caption=f'⭐{movies[0]["vote_average"]}')
      st.text(movies[0]["title"])
with col2:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[1]['poster_path'] }", caption=f'⭐{movies[1]["vote_average"]}')
      st.text(movies[1]["title"])
with col3:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[2]['poster_path'] }", caption=f'⭐{movies[2]["vote_average"]}')
      st.text(movies[2]["title"])
with col4:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[3]['poster_path'] }", caption=f'⭐{movies[3]["vote_average"]}')
      st.text(movies[3]["title"])
with col5:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[4]['poster_path'] }", caption=f'⭐{movies[4]["vote_average"]}')
      st.text(movies[4]["title"])

st.header("Rekomendasi Film Komedi")
if st.button("Rekomendasi Komedi"): 
      switch_page("Komedi")


query = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=35&api_key=daa72e5129266ed8b88b414c034ff362"
movies = requests.get(query).json()["results"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[0]['poster_path'] }", caption=f'⭐{movies[0]["vote_average"]}')
      st.text(movies[0]["title"])
with col2:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[1]['poster_path'] }", caption=f'⭐{movies[1]["vote_average"]}')
      st.text(movies[1]["title"])
with col3:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[2]['poster_path'] }", caption=f'⭐{movies[2]["vote_average"]}')
      st.text(movies[2]["title"])
with col4:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[3]['poster_path'] }", caption=f'⭐{movies[3]["vote_average"]}')
      st.text(movies[3]["title"])
with col5:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[4]['poster_path'] }", caption=f'⭐{movies[4]["vote_average"]}')
      st.text(movies[4]["title"])


st.header("Rekomendasi Film Romance")
if st.button("Rekomendasi Romance"): 
      switch_page("Romance")


query = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=10749&api_key=daa72e5129266ed8b88b414c034ff362"
movies = requests.get(query).json()["results"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[0]['poster_path'] }", caption=f'⭐{movies[0]["vote_average"]}')
      st.text(movies[0]["title"])
with col2:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[1]['poster_path'] }", caption=f'⭐{movies[1]["vote_average"]}')
      st.text(movies[1]["title"])
with col3:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[2]['poster_path'] }", caption=f'⭐{movies[2]["vote_average"]}')
      st.text(movies[2]["title"])
with col4:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[3]['poster_path'] }", caption=f'⭐{movies[3]["vote_average"]}')
      st.text(movies[3]["title"])
with col5:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[4]['poster_path'] }", caption=f'⭐{movies[4]["vote_average"]}')
      st.text(movies[4]["title"])

st.header("Rekomendasi Film Horor")
if st.button("Rekomendasi Horor"): 
      switch_page("Horor")



query = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=27&api_key=daa72e5129266ed8b88b414c034ff362"
movies = requests.get(query).json()["results"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[0]['poster_path'] }", caption=f'⭐{movies[0]["vote_average"]}')
      st.text(movies[0]["title"])
with col2:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[1]['poster_path'] }", caption=f'⭐{movies[1]["vote_average"]}')
      st.text(movies[1]["title"])
with col3:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[2]['poster_path'] }", caption=f'⭐{movies[2]["vote_average"]}')
      st.text(movies[2]["title"])
with col4:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[3]['poster_path'] }", caption=f'⭐{movies[3]["vote_average"]}')
      st.text(movies[3]["title"])
with col5:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[4]['poster_path'] }", caption=f'⭐{movies[4]["vote_average"]}')
      st.text(movies[4]["title"])

st.header("Rekomendasi Film Documentary")
if st.button("Rekomendasi Documentary"): 
      switch_page("Documentary")

query = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=99&api_key=daa72e5129266ed8b88b414c034ff362"
movies = requests.get(query).json()["results"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[0]['poster_path'] }", caption=f'⭐{movies[0]["vote_average"]}')
      st.text(movies[0]["title"])
with col2:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[1]['poster_path'] }", caption=f'⭐{movies[1]["vote_average"]}')
      st.text(movies[1]["title"])
with col3:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[2]['poster_path'] }", caption=f'⭐{movies[2]["vote_average"]}')
      st.text(movies[2]["title"])
with col4:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[3]['poster_path'] }", caption=f'⭐{movies[3]["vote_average"]}')
      st.text(movies[3]["title"])
with col5:
      st.image(f"https://image.tmdb.org/t/p/w500{ movies[4]['poster_path'] }", caption=f'⭐{movies[4]["vote_average"]}')
      st.text(movies[4]["title"])