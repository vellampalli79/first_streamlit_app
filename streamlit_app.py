import streamlit  as st
import pandas
import os

st.title(' 🥗 🐔 🥑🍞 My parent\'s healthy new dinner!')

st.header('Breakfast Favorites')

st.text('🍞 Omega 3 & Blueberry Oatmeal')
st.text('🥗  Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard Boilded Free-Range Eggs')


st.header('🍌🍞 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

st.dataframe(my_fruit_list)

#Pick fruits from a list
fruits_selected = st.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Strawberries','Peach'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on page
st.dataframe(fruits_to_show)


