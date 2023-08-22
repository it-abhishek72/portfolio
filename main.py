import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title('Abhishek Kumar')
    content = """
    Backend Developer experienced with all stages of development cycle for dynamic web project and mobile apps. 
    Well – versed in numerous programming languages including PHP, MySQL, Javascript, Ajax. Development expertise on Laravel framework. 
    Strong background in project management and client handling
    """
    st.info(content)


content2 = "Below you can find some of the app that I have developed. Feel free to contant me!!!"

st.write(content2)

df = pd.read_csv("data.csv",sep=";")
col3,empty_column, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
