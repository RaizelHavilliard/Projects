import streamlit as st

st.title("Happy Number?!")

def Is_happy(n):
    seen_nums = set()
    while n!=1 and n not in seen_nums:
        seen_nums.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1
        
n = st.text_input("What number you wanna check if it's happy or nah?")
st.write(Is_happy(n))