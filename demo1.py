#part1-introduction to streamlit app
import streamlit as st

#adding title to your streamlit app
st.title("hello streamlit")





######################################################################################################
#part2- displaying text 

#header
st.header("header")

#subheader
st.subheader("sub header")


#to add text to your application
st.text("i like this video and subscribe to the youtube channel")

#to add customization- markdown, latex
st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:
**bold**
_italics_
""",True)
#:moon:, :sunglasses: means emojis
#you can also pass in html code in the above code, you need to pass an additional argument True
#<br>- break line, emoji got shifted to the new line
#**bold** - ** makes your text bold below the sunglasses emoji
#_italics_ - underscore makes your text italics


#use latex- you can pass a string or a sympy expression
st.latex(r"""a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)""")



#write- you can pass in multiple arguments and all of them be printed on the application
#second is that its behaviour depends on the input type
st.write("rupesh","karthikeyan","python")

st.write(" # rupesh ")
st.write(st) #you will get st documentation, try this

st.write(sum) #instead of module we are passing in the function


d ={
    "name":"rupesh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d) #we can pass in the dictionary

#we can also pass in dataframe and plots. 







