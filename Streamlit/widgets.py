import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}")
    st.write("How are you today")
    
age = st.slider("Select your age:", 0, 100, 25)
if age:
    st.write(f"Your age is {age}")
    
options = ["English", "Vietnamese", "Japaness", "Korean"]
choice = st.selectbox("Choose your favourte languge:", options)
st.write(f"You selected {choice}")

data = {
    "Name": ["Huyen My", "Bao Chau", "Lam Ngoc", "Thao Nguyen"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file")
if(uploaded_file is not None):
    df = pd.read_csv(uploaded_file)
    st.write(df)
    
