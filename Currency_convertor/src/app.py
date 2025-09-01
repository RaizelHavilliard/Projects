import streamlit as st
from curencieslist import my_list
from currencyconvertor import get_exchange_rate, convert_currency

st.title(' :dollar: Currency Convertor')

st.markdown("""This tool allows you to convert amounts between different currencies🌎.
             Enter the amount and choose the currenies to convert""")

base_currency = st.selectbox('From currency (base):', my_list)
target_currency = st.selectbox('To currency (target):', my_list)

amount = st.number_input('Enter amount:', min_value=0, value=10)

if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_currency = convert_currency(amount, exchange_rate)
        st.success(f'✅ Exchange Rate:, {exchange_rate:.4f}')
        col1, col2, col3 = st.columns(3)
        col1.metric(label="base currency", value= f'{amount:.2f} {base_currency}')
        col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="target curency", value=f'{converted_currency} {target_currency}')

    else:
        st.error('Error fetching exchange rate')






