#part4- displaying plots and media on streamlit app
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data=pd.DataFrame(np.random.randn(100,3),columns=["a","b","c"])


st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

plt.scatter(data["a"],data["b"])
plt.title("scatter")
st.pyplot()


chart =alt.Chart(data).mark_circle().encode(
    x='a', y="b",tooltip=["a","b"]
) #tooltip- show a and b values in a particular point
st.altair_chart(chart,use_container_width=True) #width using the container space

st.graphviz_chart(""" 
digraph{
watch -> like
like -> share
share -> subscribe
subscribe -> watch
}""")  #to create a flowchart

st.map() #world map
#you should have dataframe having latitude and longitude column

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})

st.map(city)



st.image("D:\\photos\\bombay1\\100_0871.jpg")

st.audio("C:\\Users\\karth\\Downloads\\demo.wav")

st.video("C:\\Users\\karth\\Downloads\\virtual.mp4")

st.video("https://www.youtube.com/watch?v=nNwVAc6OdN4&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=2")

