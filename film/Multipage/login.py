import streamlit as st
import hashlib
from streamlit_extras.switch_page_button import switch_page 

# Fungsi untuk mengenkripsi password
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Fungsi untuk memeriksa apakah password sudah ada di database
def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return True
    return False

# Membuat database dari file .txt
database = {}
with open("database.txt", "r") as f:
    for line in f:
        username, password = line.strip().split(",")
        database[username] = password

# Membuat tampilan streamlit
menu = ["Login","Sign Up"]
choice = st.selectbox("Menu",menu)

if choice == "Login":
    st.subheader("Masuk ke akun Anda")

    username = st.text_input("Username")
    password = st.text_input("Password",type='password')
    if st.button("Login"):
        if username in database:
            hashed_pswd = database[username]
            if check_hashes(password,hashed_pswd):
                with open("logged_in.txt", "w") as logged_in:
                    logged_in.write(username) 
                    switch_page("app")
            else:
                st.error("Password salah")
        else:
            st.error("Username tidak ditemukan")

elif choice == "Sign Up":
    st.subheader("Buat akun baru")

    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("Sign Up"):
        if new_user in database:
            st.warning("Username sudah ada")
        else:
            database[new_user] = make_hashes(new_password)
            with open("database.txt", "a") as f:
                f.write(new_user + "," + database[new_user] + "\n")
            st.success("Akun Anda berhasil dibuat")
            st.info("Silakan login untuk melanjutkan")
