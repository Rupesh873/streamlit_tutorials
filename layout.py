import streamlit as st
st.title("registration form")

first,last= st.columns(2)

first.text_input("first name")
last.text_input("last name")

email,mob=st.columns([3,1]) #email will be 3times big as mob, 3:1 ratio as a list[3,1]
email.text_input("email id")
mob.text_input("mobile number")

username,password,retype=st.columns(3)
username.text_input("username")
password.text_input("password",type="password")
retype.text_input("re-enter your password",type="password")

checkbox,blank,submit=st.columns(3)
checkbox.checkbox("i agree")
submit.button("submit")