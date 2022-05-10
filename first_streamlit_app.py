import streamlit
import requests
#Based on another user:
#import streamlit
#import pandas as pd
#import requests
#import snowflake.connector
#from urllib.error import URLError


streamlit.title('My Mom\'s New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Adding a pick list:
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#normalized answer
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output a table on the screen
streamlit.dataframe(fruityvice_normalized)


streamlit.header('Would you like to pick another Fruit?')
#Adding a second pick list:
my_fruit_list_2 = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list_2 = my_fruit_list_2.set_index('Fruit')

#Adding a pick list:
fruits_selected_2 = streamlit.multiselect("Pick some fruits:", list(my_fruit_list_2.index),['Kiwi','Bannana'])
fruits_to_show_2 = my_fruit_list_2.loc[fruits_selected_2]

#Display the table on the page
streamlit.dataframe(fruits_to_show_2)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
