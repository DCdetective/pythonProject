import streamlit as st

st.title('Welcome to my web page')

st.header('Want to know about me?')
option_1 = "None"
option = st.selectbox("Want to know about me ?" ,("None","Yes","No"))
if option == "Yes":
    option_1 = st.selectbox("Exactly what do u want to know about me?",("None","Skills","Education" ,"Bio data"))
elif option == "No":
    st.subheader("Thank you for visiting my website")
else:
    st.write("Select the given options")
if option_1 == "Skills":
    st.write("I have skills in Python and Java programming languages")
    st.write("i have experience in Python libraries for Data Analysis like matplot ,numpy and pandas")
    st.write('Hands on Machine Learning and Deep Learning')
    st.write("Maths for Statistical intution")
elif option_1 == "Education":
    st.write("I am persuing my bachlores degree in Artificial Intelligence and Data Science")
elif option_1 == "Bio data" :
    st.write("I was born in December 6th 2003")
    st.write('Place of birth is Riyad , Saudi Arabia')
else:
    st.write("Select")