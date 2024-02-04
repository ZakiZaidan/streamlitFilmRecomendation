import streamlit as st
import requests
import urllib.request
 
pages = ["Output 1", "Output 2", "Output 3 ","Output 4","Output 5","Output 6","Output 7","Output 8","Output 9","Output 10","Output 11","Output 12","Output 13","Output 14","Output 15","Output 16","Output 17","Output 18","Output 19","Output 20"]

if "page_index" not in st.session_state:
    st.session_state.page_index = 0

with st.form("navigation"):
    # Buat dua kolom untuk menempatkan tombol "back" dan "next"
    col1, col2 = st.columns(2)
    # Buat tombol "back" di kolom pertama
    back = col1.form_submit_button("Back")
    # Buat tombol "next" di kolom kedua
    next = col2.form_submit_button("Next")

if back:
    st.session_state.page_index -= 1

if next:
    st.session_state.page_index += 1


# Jika indeks halaman kurang dari 0, kembalikan ke nilai maksimum
if st.session_state.page_index < 0:
    st.session_state.page_index = len(pages) -1
# Jika indeks halaman lebih dari nilai maksimum, kembalikan ke 0
if st.session_state.page_index >= len(pages):
    st.session_state.page_index = 0


query = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=10749&api_key=daa72e5129266ed8b88b414c034ff362"
response = requests.get(query).json()["results"]


counter = 0
for movie in response:
      if st.session_state.page_index == counter:
            img_layout, info_layout = st.columns(2)
            video_json = requests.get(
                 f"https://api.themoviedb.org/3/movie/{movie['id']}/videos?api_key=daa72e5129266ed8b88b414c034ff362"
            ).json()["results"]
            cast_json = requests.get(
                f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key=daa72e5129266ed8b88b414c034ff362"
            ).json()["cast"][:5]

            with img_layout: 
                st.image(f"https://image.tmdb.org/t/p/w500{ movie['poster_path'] }",caption=f'⭐{movie["vote_average"]}')
           
            with info_layout:
                st.subheader(movie["title"])
            # urllib.request.urlretrieve(‘Image url’, “file_name”)

            # image = Image.open(f"https://image.tmdb.org/t/p/w500{ movie['poster_path'] }")


                with st.expander("SINOPSIS"):
                  st.text(f'''{movie["overview"]}''')

                with st.expander("TRAILER"):
                  st.video(f"https://www.youtube.com/watch?v={video_json[0]['key']}")
                  pass
             
            st.subheader ("CAST")

            cast_cols = st.columns(len(cast_json))
            for i in range(len(cast_cols)):
                 with cast_cols[i]:
                     st.image(f"http://image.tmdb.org/t/p/w154/{cast_json[i]['profile_path']}", caption=f"{cast_json[i]['name']}", width=150)
      counter += 1