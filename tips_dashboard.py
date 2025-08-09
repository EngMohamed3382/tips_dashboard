import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Tips Dashboard', layout='wide', initial_sidebar_state='expanded')


df = pd.read_csv('tips.csv')

#Side Bar
st.sidebar.header('Tips Dashboard')
st.sidebar.image('tips.jpg')
st.sidebar.write("Explore the tips dataset and gain insights.")
st.sidebar.write('')
st.sidebar.write("Filter your data:")
cat_filter = st.sidebar.selectbox("Select a category:", [ None,'sex', 'smoker', 'day', 'time'])
num_filter = st.sidebar.selectbox("Select a category:", [ None,'total_bill', 'tip'])
row_filter = st.sidebar.selectbox("Select a row:", [ None,'sex', 'smoker', 'day', 'time'])  
col_filter = st.sidebar.selectbox("Select a column:", [ None,'sex', 'smoker', 'day', 'time'])

st.sidebar.write('')
st.sidebar.markdown("Made with ❤️ by [Atlas Home](https://www.youtube.com/@atlashome8869)")

#body


#row a
a1, a2, a3, a4 = st.columns(4)

a1.metric(label="Max. Total Bill", value=df['total_bill'].max())
a2.metric(label="Max. Tip", value=df['tip'].max())
a3.metric(label="Min. Total Bill", value=df['total_bill'].min())
a4.metric(label="Min. Tip", value=df['tip'].min())


# row b

#st.subheader('Total Bills vs. Tips')
fig = px.scatter(df, x='total_bill', y='tip', color= cat_filter, size=num_filter,
                 facet_col=col_filter, facet_row=row_filter,
                 title='Total Bill vs Tip by Day', hover_data=['sex', 'time'])
st.plotly_chart(fig, use_container_width=True)


# row c

c1, c2, c3 = st.columns((4, 3, 3))
with c1:
    st.write("### Total Bill Distribution")
    fig = px.bar(data_frame=df, x='sex', y='total_bill', color=cat_filter, title='Total Bill Distribution')
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.write("### Tip Distribution")
    fig = px.pie(df, values='tip', names=cat_filter, hole=0.4, title='Tip Distribution')
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.write("### Size Distribution")
    fig = px.pie(df, values='size', names=cat_filter, title='Size Distribution')
    st.plotly_chart(fig, use_container_width=True)