import streamlit as st
import random
from main_auto import simulating_game
import time

st.title("Monty Hall")

num_games = st.number_input("how many time you wanna simulate?", min_value=2, max_value=100000, value=100)
win_switch = 0
win_no_switch = 0

col1, col2 = st.columns(2)
col1.subheader("win percentage with swithcing")
col2.subheader("win percentage without swithcing")
chart1 = col1.line_chart([1.0])
chart2 = col2.line_chart([1.0])


for i in range (num_games):
    num_with_switch, num_without_switch = simulating_game(1)
    win_switch += num_with_switch
    win_no_switch += num_without_switch

    chart1.add_rows([win_switch / (i+1)])
    chart2.add_rows([win_no_switch / (i+1)])


time.sleep(0.009)
