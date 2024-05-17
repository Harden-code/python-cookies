import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('x')
st.write(x,'squared is',x * x)

st.text_input('your name',key = 'name')


def show():
    st.write('hello ')


st.button('button',on_click = show)

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ',option

st.line_chart(df)

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76,-122.4],
    columns = ['lat','lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a','b','c'])

    chart_data

st.markdown('## H-O')
st.markdown('''
            ### Hello
            - j
            ''')

with st.sidebar:
    st.write('1')
    st.radio('x',[1,2,3])