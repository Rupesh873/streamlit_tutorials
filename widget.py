#part5- adding widgets to streamlit

#in this part we will be seeing how you can make your streamlit app interactive using widgets

#widgets allows us to interact with the application and in return the whatever input we get from the 
#widget will be used to trigger certain actions in that app 


import streamlit as st


st.title("widget")
#we should also activate a virtual environment which is env\scripts\activate



#we will be adding our first widget and that we be a button
st.button("subscribe")





#adding functionality to this button
#type if, so the button returns a boolean true value whenever it is clicked. 
#so thats why i have a if statement so whenever this is true we will add a funciton.
if st.button("join"):
    st.write("would you like to join")





#text input allows the user to input text into our app 
st.text_input("Name")

name=st.text_input("enter your details")
st.write(name)



#multiple lines of input
address=st.text_area("enter your address")
st.write(address)


#date and time input
st.date_input("enter a date")
st.time_input("enter a time")



#add check box
st.checkbox("you accept the t&c", value=False)  #True means the box will already be ticked,
#and False means we need to tick the box


#adding functionality to the checkbox
if st.checkbox("next", value=False):
    st.write("you are done")




#radio button and select box to our streamit app- both have similar function which is to select one
#of the option from the given options, and the only difference is that the select is our drop-down menu
st.radio("colours",["r","g","b"],index=1)#pre chosen option

colors=st.selectbox("colours",["r","g","b"],index=None)


school_house= st.selectbox("house",["red","green","blue"],index=None)
st.write(school_house,colors)




#select multiple options
x=st.multiselect("colours",["r","g","b"])
st.write(x)


#slider
st.slider("age") #default minimum value 0 and maximum value 100
st.slider("age",min_value=18,max_value=60,value=30,step=2)




#numbers input
st.number_input("numbers",min_value=18.0,max_value=60.0,value=30.0,step=2.0)



#upload files
img= st.file_uploader("upload a file")
st.image(img)


#in the next video we will be seeing how we can add these widgets to our sidebar and then we will be 
#creating a navigation bar using widgets and sidebars


