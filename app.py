import streamlit as st

st.write('Hello World')
st.title('My first app')
st.markdown("## This is a markdown cell")
st.header("This is a header")
st.subheader("This is a subheader")
st.text_input("Enter your name")
st.checkbox("Checkbox")
st.button("Predict")
st.selectbox("Select", [1,2,3])

st.file_uploader("Upload a file")

st.progress(50)

st.success("Successful")
st.error("Error")