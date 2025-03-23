import streamlit as st
from prompts import gen_seq_chain
import ast
import json

#-----------------------------Working Functions------------------------------

# Generate comic content by invoking the chain from prompt module
def generate_content(input):
    output = gen_seq_chain.invoke({'title': input})
    return output

#---

# Cleaning data to remove the "delimiters"
def clean_data(data):
    start_python = data.find("```python")
    start_json = data.find("```json")
    start_csv = data.find("```csv")
    end = data.rfind("```")
    if start_json == -1 and start_csv == -1:
        try:
            cleaned_data= data.strip("```python").strip("```").strip()
            return cleaned_data
        except Exception as e:
            st.error(f"Cleaning error occurred. Please try again.\n{e}")
    elif start_python == -1 and start_csv == -1:
        try:
            cleaned_data= data.strip("```json").strip("```").strip()
            return cleaned_data
        except Exception as e:
            st.error(f"Cleaning error occurred. Please try again.\n{e}")
    elif start_json == -1 and start_python == -1:
        try:
            cleaned_data= data.strip("```csv").strip("```").strip()
            return cleaned_data
        except Exception as e:
            st.error(f"Cleaning error occurred. Please try again.\n{e}")
    else:
        return data

#---

# converting string to dictionary
def convert_to_dict(comic_element_data):
    # st.write(theme_output)
    response = comic_element_data
    # first try is for python dictionary
    try:
        # cleaning the data
        clean_response = clean_data(response)   # string
        python_dic = ast.literal_eval(clean_response)
        # corrected_string = response.replace('"', r'\"')
        # st.write(response)
        # python_dic = ast.literal_eval(response)
        return python_dic
    except Exception as e:
        st.error(f"Conversion error occurred. Please try again.\n{e}")
    return {}

#---

#-----------------------------------Comic Data------------------------

def collect_theme_data(theme_data):
    title = theme_data.get('title', '')
    genre = theme_data.get('genre', '')
    tone = theme_data.get('tone', '')
    themes = theme_data.get('themes', [])
    keywords = theme_data.get('keywords', [])
    setting = theme_data.get('setting', {})
    location = setting.get('location', '')
    time_period = setting.get('time_period', '')
    atmosphere = setting.get('atmosphere', '')

#

def show_theme_data(theme_data):
    st.markdown("## Theme Data")

    # Iterate the dictionary and its items
    for key, value in theme_data.items():

        # Check if the value is Themes and Keywords as they are list
        if key == 'themes' or key == 'keywords':
            st.markdown(f"- **{key.capitalize()}:**")

            # Iterate the list and its items
            for items in theme_data.get(key):
                # Displaying the items
                st.markdown(f"&emsp; ➡️ :orange[*{items}*]")

        # Check if the value is Setting as it is dictionary
        elif key == 'setting':
            st.markdown(f"- **{key.capitalize()}:**")

            # Iterate the dictionary and its items
            for sub_key, sub_value in theme_data.get(key).items():
                # Displaying the items
                st.markdown(f"&emsp; ➡️ :green[*__{sub_key.capitalize()}:__*] &nbsp; :orange[*{sub_value}*]")
        
        # Displaying the other items
        else:
            st.markdown(f"- **{key.capitalize()}:** &nbsp; :orange[*{value}*]")

#

#---    

#-----------------------------Steamlit app interface------------------------------

st.title("Comic Generator App")
st.write("This app generates comic book plots based on the title you provide.")

# Get user input
input_text = st.text_input("Enter the title of your comic book:")
# input_text = "The Dark Knight"

# Generate comic data
if st.button("Generate Comic Plot"):
    try:
        # call the function to generate the comic data in dictionary (title, theme and plot)[in string]
        comic_response = generate_content(input_text)
        st.write(comic_response)

        # convert the theme_data and plot_data from comic_response into string-dictionary to dictionary
        theme_dict = convert_to_dict(comic_response.get("theme_data"))
        plot_dict = convert_to_dict(comic_response.get("plot_data"))
        char_dict = convert_to_dict(comic_response.get("character_data"))

        # Show the dict data
        st.write(theme_dict)
        st.write(plot_dict)
        st.write(char_dict)

    except Exception as e:
        st.error(f"App error occurred. Please try again.\n{e}")






































# ----------------------------- Extra's---------------------------
        # # if python dictionary fails, try to convert to json
        # try:
        #     # response = response.replace("'","\"").strip()   # to remove single quotes (for csv data)
        #     clean_response = clean_data(response)   # string
        #     st.write(clean_response)
        #     st.markdown(type(clean_response))
        #     python_dic = json.loads(clean_response)
        #     return python_dic    
        # except Exception as e:
        #     st.error(f"Conversion error occurred. Please try again.\n{e}")