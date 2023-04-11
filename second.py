import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import seaborn as sns
from PIL import Image
import matplotlib.cbook as cbook

st.write("""
# Tips:



""")


path = '~/ds_bootcamp/ds-phase-0/learning/datasets/tips.csv'
tips = pd.read_csv(path, index_col=0)
sea_tips = sns.load_dataset("tips")

sea_tips

#col1,con1,col2,con2=st.beta_columns([0.3,1.2,0.3])
col1, col2 = st.columns(2)

### Гистограмма total_bill
with col1:
 col1.subheader("Гистограмма total_bill:")

 fig,ax=plt.subplots()
 sns.barplot(data=sea_tips, x='total_bill', y=sea_tips.index)
 st.pyplot(fig)

### Scatterplot, показывающий связь между total_bill and tip
with col2:
 col2.subheader("Scatterplot, показывающий связь между total_bill and tip:")

 fig,ax=plt.subplots()
 sns.scatterplot(data=sea_tips, x="total_bill", y="tip");
 st.pyplot(fig)

#ows2 = col3, col4 = st.columns(2)

### График, связывающий total_bill, tip, и size
with col1:
 col1.subheader("График, связывающий total_bill, tip, и size:")

 fig,ax=plt.subplots()
 sns.scatterplot(data=sea_tips, x='total_bill', y='tip', size='size');
 st.pyplot(fig)

### Связь между днем недели и размером счета
with col2:
 col2.subheader("Связь между днем недели и размером счета:")

 fig,ax=plt.subplots()
 sns.barplot(data=sea_tips, x="day", y="total_bill", estimator=np.sum);
 st.pyplot(fig)

### Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу
with col1:
 col1.subheader("Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу:")

 fig,ax=plt.subplots()
 sea_tips.groupby('day')['total_bill'].sum()
 sns.scatterplot(data=sea_tips, x='tip', y='day', hue='sex');
 st.pyplot(fig)

### Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)
with col2:
 col2.subheader("Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch):")

 fig,ax=plt.subplots()
 sns.boxplot(data=sea_tips, x="total_bill", y="day", hue="time");
 st.pyplot(fig)

### Гистограммы чаевых на обед и ланч
with col1:
 col1.subheader("Гистограммы чаевых на обед и ланч:")

 fig,ax=plt.subplots()
 tips3 = sea_tips.groupby('time')['total_bill'].sum().reset_index()
 sns.barplot(data=tips3, x='total_bill', y='time');
 st.pyplot(fig)

with col2:
 col2.subheader("Гистограммы чаевых на обед и ланч (вариант 2):")

 fig,ax = plt.subplots()
 eleven = sns.FacetGrid(sea_tips, col="time")
 eleven.map(sns.histplot, "tip");
 st.pyplot(fig)

### scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. 
with col1:
 col1.subheader("scatterplots (для мужчин и женщин), показавающий связь размера счета и чаевых, дополнительно разбитый по курящим/некурящим:")

 fig,ax=plt.subplots()
 twelve = sns.FacetGrid(sea_tips, col="sex", hue="smoker")
 twelve.map(sns.scatterplot, "total_bill", "tip")
 twelve.add_legend();
 st.pyplot(fig)


with col2:
 col2.subheader("Последние два графика, которые не отображаются (я так понимаю, что проблема в FacetGrit. Перепробовала кучу вариантов, но пока не знаю, как ее решить):")

 image1 = Image.open('f1.png')
 st.image(image1, caption='Гистограммы чаевых на обед и ланч:')
 image2 = Image.open('f2.png')
 st.image(image2, caption='scatterplots (для мужчин и женщин), показавающий связь размера счета и чаевых, дополнительно разбитый по курящим/некурящим:')