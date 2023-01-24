import streamlit  as st
import pandas

st.title(' 🥗 🐔 🥑🍞 My parent\'s healthy new dinner!')

st.header('Breakfast Favorites')

st.text('🍞 Omega 3 & Blueberry Oatmeal')
st.text('🥗  Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard Boilded Free-Range Eggs')


st.header('🍌🍞 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)

my_test_file = pandas.read_csv("C:\Users\F618004\Downloads\veggie_details_a_to_k_comma_opt_enclosed (2).csv")
st.dataframe(my_test_file)
 
