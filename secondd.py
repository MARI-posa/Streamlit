import streamlit as st
st.set_page_config(layout="wide")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #e5e5f7;
opacity: 0.8;
background-image: linear-gradient(45deg, #fdede4 50%, #e5e5f7 50%);
background-size: 29px 29px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import seaborn as sns
from PIL import Image
import matplotlib.cbook as cbook

st.markdown(f'<h1 style="text-align: center;color:#406278;font-size:38px;">{"Работа с df Tips:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#406278;font-size:38px;">{"Tips:"}</h1>', unsafe_allow_html=True)


path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path, index_col=0)
sea_tips = sns.load_dataset("tips")

sea_tips

st.markdown(f'<h1 style="text-align: center;color:#406278;font-size:38px;">{"Графики, построенные на основе иформации из df Tips:"}</h1>', unsafe_allow_html=True)

#col1,con1,col2,con2=st.beta_columns([0.3,1.2,0.3])
col1, col2, col3, col4 = st.columns([1,4,4,1])
#col1, col2 = st.columns(2)

### Гистограмма total_bill
with col2:
 #col1.subheader("Гистограмма total_bill:")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Гистограмма total_bill:"}</h1>', unsafe_allow_html=True)

 fig,ax=plt.subplots()
 sns.barplot(data=sea_tips, x='total_bill', y=sea_tips.index)
 st.pyplot(fig)

### Scatterplot, показывающий связь между total_bill and tip
with col3:
 #col2.subheader("Scatterplot, показывающий связь между total_bill and tip:")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Scatterplot, показывающий связь между total_bill and tip:"}</h1>', unsafe_allow_html=True)

 fig,ax=plt.subplots()
 sns.scatterplot(data=sea_tips, x="total_bill", y="tip");
 st.pyplot(fig)

#ows2 = col3, col4 = st.columns(2)

### График, связывающий total_bill, tip, и size
with col2:
 #col1.subheader("График, связывающий total_bill, tip, и size:")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"График, связывающий total_bill, tip, и size:"}</h1>', unsafe_allow_html=True)

 fig,ax=plt.subplots()
 sns.scatterplot(data=sea_tips, x='total_bill', y='tip', size='size');
 st.pyplot(fig)

### Связь между днем недели и размером счета
with col3:
 #col2.subheader("Связь между днем недели и размером счета:")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Связь между днем недели и размером счета:"}</h1>', unsafe_allow_html=True)

 fig,ax=plt.subplots()
 sns.barplot(data=sea_tips, x="day", y="total_bill", estimator=np.sum);
 st.pyplot(fig)

### Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу
with col2:
 #col1.subheader("Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу:")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу:"}</h1>', unsafe_allow_html=True)

 fig,ax=plt.subplots()
 sea_tips.groupby('day')['total_bill'].sum()
 sns.scatterplot(data=sea_tips, x='tip', y='day', hue='sex');
 st.pyplot(fig)

### Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)
with col3:
 #col2.subheader("Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch):")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch):"}</h1>', unsafe_allow_html=True)

 fig,ax=plt.subplots()
 sns.boxplot(data=sea_tips, x="total_bill", y="day", hue="time");
 st.pyplot(fig)

### Гистограммы чаевых на обед и ланч
with col2:
 #col1.subheader("Гистограммы чаевых на обед и ланч:")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Гистограммы чаевых на обед и ланч:"}</h1>', unsafe_allow_html=True)

 fig,ax=plt.subplots()
 tips3 = sea_tips.groupby('time')['total_bill'].sum().reset_index()
 sns.barplot(data=tips3, x='total_bill', y='time');
 st.pyplot(fig)

with col3:
 #col2.subheader("Гистограммы чаевых на обед и ланч (вариант 2):")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Гистограммы чаевых на обед и ланч (вариант 2):"}</h1>', unsafe_allow_html=True)

 sc = sns.FacetGrid(sea_tips, col="time")
 sc.map_dataframe(sns.histplot, 'tip')
 st.pyplot(sc)


### scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. 
with col2:
 #col1.subheader("scatterplots (для мужчин и женщин), показавающий связь размера счета и чаевых, дополнительно разбитый по курящим/некурящим:")
 st.markdown(f'<h1 style="color:#406278;font-size:24px;">{"Scatterplots (для мужчин и женщин), показавающий связь размера счета и чаевых, дополнительно разбитый по курящим/некурящим:"}</h1>', unsafe_allow_html=True)

 sc = sns.FacetGrid(sea_tips, col="sex", hue="smoker")
 sc.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
 st.pyplot(sc)
