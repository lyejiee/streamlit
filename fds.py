import requests
import xmltodict
import time
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(

    page_title='시청률 현황',
    page_icon=''
)
data = pd.read_csv('data2.csv', encoding='cp949')
category = st.sidebar.selectbox('카테고리를 선택하세요', ['예능', '드라마', '뉴스'])
채널리스트 = ''
if category == '예능':
    채널리스트 = st.sidebar.multiselect('예능을 선택하세요', ['런닝맨','일밤','1박 2일','개그콘서트'])
elif category == '드라마':
    채널리스트 = st.sidebar.multiselect('드라마를 선택하세요', ['오로라 공주','최고다 이순신','금나와라 뚝딱'])
else:
    채널리스트 = st.sidebar.multiselect('뉴스를 선택하세요', ['KBS9시뉴스', 'MBC뉴스데스크', 'SBS8뉴스'])

date = ['7월7일', '7월14일','7월21일','7월28일']

temp = data[data['title']=='런닝맨']
plt.rc('font', family='Malgun Gothic')
for value in 채널리스트:
    temp = data[data['title']==value]
    plt.plot(date, temp['시청률'])

    # plt.plot(temp['createDt'], temp['natDefCnt'], label=value)
    # temp = df[df['nationNm'] == value]
    # plt.plot(temp['createDt'], temp['natDefCnt'], label=value)

plt.legend()


st.pyplot(plt)