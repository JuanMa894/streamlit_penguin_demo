import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

st.sidebar.title('Change name')
side_button = st.sidebar.button('Press Me!')
if side_button:
    st.sidebar.write('side bar button was pressed')
    
st.image('images/penguins.jpg', use_column_width='always')
st.title('Streamlit with Penguins')
st.header('This is a header')

col1, col2 = st.columns(2)
col1.subheader('Col1')
col2.subheader('Col2')

col21, col22, col23 = st.columns([3,2,1])
col21.write('Widest column, testing 1 2 3, text should wrap if it needs to, since it might be to long')
col22.write('Medium col, mic check')
col23.write('Small col, succes')

st.markdown('# Mrkdown **syntax** *works*')

check = st.checkbox('Please check me!')

button_check = st.button('Is box checked?')

if button_check:
    if check:
        st.write('the box was checked')
    else:
        st.write('not checked')


animal_options = ['Cats', 'Dogs', 'Guinea pig', 'Bearded Dragon']

Fav_animal = st.radio('Which animal is your favorite', animal_options)
button_fav = st.button('Submit animal')
if button_fav:
    st.write(f'You selected {Fav_animal} as your fav animal')
    if Fav_animal == 'Cats':
        st.write('MEOW')
    if Fav_animal == 'Dog':
        st.write('WHOOF')
    else:
        st.write('animal noise')

Fav_animal2 = st.selectbox('Fav Animal?', animal_options)
button_fav2 = st.button('Submit')
if button_fav2:
    st.write(f'You selected {Fav_animal} as your fav animal')
    if Fav_animal == 'Cats':
        st.write('MEOW')
    if Fav_animal == 'Dog':
        st.write('WHOOF')
    else:
        st.write('animal noise')

animals_like = st.multiselect('which animal do you like', animal_options)
button_like = st.button('animals')
if button_like:
    st.write(animals_like)
    st.write(f'Your first animal submission was {animals_like}')

num_pets = st.slider('How many pets do you have?', 2, 20, 2, 2)

in_text = st.text_input('What is your pets name', value= "i don't have a pet")
st.write("Pet's name is:", in_text)

num_imput = st.number_input(" How many pets?", min_value=0)
st.write(f'i have {num_imput} pets')