#part6-sidebar,navigation,progress and status

#in previous part we saw how we can add widgets to your streamlit app and make your app interactive

#in this part we will be seeing how you can add these widgets to the sidebar

#so adding a widget to the sidebar allows you to pin the mentioned widgets on the left hand side of the
#screen so this allows the users to focus on the content present in the app.

#we will be seeing how this sidebar can be utilized in a our streamlit application
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time


plt.style.use("ggplot")

data={
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}


df=pd.DataFrame(data=data)

#activate the virtual environment- env\scripts\activate



#streamlit.sidebar.widget
st.sidebar.selectbox("select a number",[1,2,3,4,5])


st.sidebar.selectbox("select a column",df.columns)


col=st.sidebar.selectbox("select a Column",df.columns)
plt.plot(df["num"],df[col])
st.pyplot() #run this and check the difference from the above code
#you will get a graph your x-axis will be "num" and your y-axis will be "num,square,twice,thrice"


#except write,echo and spinner all the widgets can be added to the sidebar



#instead of single columns lets see how we can add multiple columns by using multiselect over here
col=st.sidebar.multiselect("select a Col",df.columns)
plt.plot(df["num"],df[col])
st.pyplot()




#we will see how we can use this sidebar with widget as navigation bar.
#so instead we dont get the option to have multiple pages but, we can create a multiple pages looking
#look by using the sidebar and the widgets
rad= st.sidebar.radio("navigation",["home","about us"])

if rad=="home":
    col=st.sidebar.multiselect("select a kolumn",df.columns)
    plt.plot(df["num"],df[col])
    st.pyplot()

if rad=="about us":
    st.write("you are here in about us")
    progress=st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()





#displaying progress and status in streamlit
#streamlit provides us with few methods that allows you add animation to your web application

#so these animation includes progress bars, status messages like a warning success or error then we
#also have a balloon animation that is given to us by streamlit.





#status messages
st.error("error")
st.success("success")
st.info("information")
st.exception(RuntimeError("this is an error"))
st.warning("this is a warning")

'''
progress=st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i+1)

    #progress part is in the above code

    '''