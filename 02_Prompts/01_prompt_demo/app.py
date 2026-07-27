from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

st.header('my app')

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash",temperature=0.3)

#---------------- static_prompt -----------------------------#

# user_input = st.text_input('Enter what you ask')

# if st.button('summery'):
#     result = model.invoke(user_input)
#     st.write(result.content)
    

#---------------- dynamics_prompt -----------------------------#

# city name
city_input = st.selectbox(
    'Select a city:', 
    ['Mumbai', 'London', 'Tokyo', 'New York', 'Gotan']
)

# city data type like population area
city_data = st.selectbox(
    'Select data type:', 
    ['Population', 'Total Area', 'Weather Summary', 'Top Tourist Attractions']
)

# output length
city_output = st.selectbox(
    'Select output length:', 
    ['One sentence', 'One short paragraph', 'Three bullet points']
)

template = load_prompt('templete.json')

prompt = template.invoke({
    'city' : city_input,
    'data' : city_data,
    'length': city_output
})

if st.button('summary'):
    result = model.invoke(prompt)
    st.write(result.content)


