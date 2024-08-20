import streamlit as st

st.title("Streamlit text input")


age=st.slider("Select your age:", 0,100,35)

st.write(f"Your age is {age}.")

options=['Python', 'Java', 'C++', 'Javascript', 'Scala']
choice=st.selectbox("Choose your faviorite language:", options)
st.write(f"You selected {choice}")

name = st.text_input("Enter your name")


if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please enter your name")