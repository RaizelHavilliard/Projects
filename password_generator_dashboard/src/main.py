import string
import random
import streamlit as st
import nltk
nltk.download('words')
from nltk.corpus import words
from typing import List, Optional



st.title("Password generator")
Password_type = st.selectbox(
    "what kind of password do you want?",
    ("Random", "pin", "memorable")
)

def random_password_generator(length=8, include_numbers=True, include_symbols=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters)for _ in range(length))


def generate_pin(lenght = 8):
    characters = string.digits

    return ''.join(random.choice(characters)for _ in range(lenght))


def generate_memorable_password(length = 4, seperator = '_', capitalize = False):
    words_list = words.words() 
    chosen_words = [random.choice(words_list) for _ in range(length)]
    if capitalize:
        chosen_words = [word.capitalize() for word in chosen_words]
    password = seperator.join(chosen_words)    
    return password


if Password_type == "Random":
    length = st.slider("length", min_value=8, max_value=32, value=8)
    include_numbers = st.toggle("include numbers?", value=True)
    include_symbols = st.toggle("include symbols?", value=True)


    password = random_password_generator(length, include_numbers, include_symbols) 
    st.write("Generated Password:", password)

elif Password_type == "pin":

    length = st.slider("length", min_value=6, max_value=32, value=8)
    password = generate_pin(length)
    st.write("generated pin:", password)

elif Password_type == "memorable":
    length = st.slider("how many words?", min_value=2, max_value=10, value=3)
    capitalize = st.toggle("capitalize or nah")
    seperator = st.text_input("seperator?", value="_")
    password = generate_memorable_password(length, seperator, capitalize)
    st.write("generated memorable password is:", password)













