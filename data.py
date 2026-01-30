#part3-displaying data
import streamlit as st
import pandas as pd
import numpy as np
import time

a=[1,2,3,4,5,6,7,8]
n=np.array(a)
nd=n.reshape((2,4))

dic={"name":"rupesh",
     "age":21,
     "city":"chennai"
     }

data=pd.read_csv("C:\\Users\\karth\\Downloads\\Salary_Data.csv")
print(data)

#first method to display data
st.dataframe(a)
st.dataframe(n)
st.dataframe(nd)
st.dataframe(data,width=1000,height=1000)


#secnd method
st.table(data) #another way to display data, we dont get a scroll bar, it displays all the data
st.table(dic)


#third method
st.json(dic) #needs text formatted


#fourth method
st.write(data)
st.write(a)
st.write(dic)


@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))


if st.checkbox("2"):
    st.write(ret_time(2))