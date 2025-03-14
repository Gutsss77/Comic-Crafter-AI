import streamlit as st
from prompts import *
import ast
import re
import json

# Steamlit app interface
st.title("Comic Generator App")
st.write("This app generates comic book plots based on the title you provide.")

# Get user input
# input_text = st.text_input("Enter the title of your comic book:")
input_text = "The Dark Knight"


###############################
# Cleaning data
def clean_data(data):
    start_python = data.find("```python")
    start_json = data.find("```json")
    end = data.rfind("```")
    if start_json == -1:
        try:
            cleaned_data= data.strip("```python").strip("```").strip()
            return cleaned_data
        except Exception as e:
            st.error(f"An error occurred. Please try again.\n{e}")
    elif start_python == -1:
        try:
            cleaned_data= data.strip("```json").strip("```").strip()
            return cleaned_data
        except Exception as e:
            st.error(f"An error occurred. Please try again.\n{e}")
    else:
        return None

#

# button functions
def generate_theme():
    theme_output = theme_seq_chain.invoke({'title': input_text})
    # st.write(theme_output)
    response = theme_output['theme_data']  # this response is a string
    try:
        clean_response = clean_data(response)
        python_dic = ast.literal_eval(clean_response)
        return python_dic
    except Exception as e:
        st.error(f"An error occurred. Please try again.\n{e}")
    return {}

#

def generate_plot():
    plot_output = plot_seq_chain.invoke({'title': title, 'genre': genre, 'tone': tone, 'themes': themes, 'keywords': keywords, 'location': location, 'time_period': time_period, 'atmosphere': atmosphere})
    st.write(plot_output)
    # plot_data = plot_output['plot_data']
    # st.write(plot_data)

#-----------------------------------Comic Data------------------------

title = input_text
theme_data = generate_theme()
genre = theme_data.get('genre', '')
tone = theme_data.get('tone', '')
themes = theme_data.get('themes', [])
keywords = theme_data.get('keywords', [])
setting = theme_data.get('setting', {})
location = setting.get('location', '')
time_period = setting.get('time_period', '')
atmosphere = setting.get('atmosphere', '')
plot_data = {}

def show_theme_data():
    global genre, tone, themes, keywords, location, time_period, atmosphere
    

#

#---    

# Generate comic plot
if st.button("Generate Comic Plot"):
    try:
        show_theme_data()
    except Exception as e:
        st.error(f"An error occurred. Please try again.\n{e}")

