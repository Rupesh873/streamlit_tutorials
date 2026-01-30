#installing the packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error



#loading the datasets
data=pd.read_csv("c:\\Users\\karth\\Downloads\\Salary_Data.csv")

x=np.array(data["YearsExperience"]).reshape(-1,1)
y=np.array(data["Salary"])
lr=LinearRegression()
lr.fit(x,y)




#title of the web application
st.title("Salary Predictor")


#creating the sidebar,radio button, 3 columns
navigation=st.sidebar.radio("navigation",["Home","Prediction","Contribute"])






#home page
if navigation=="Home":
    st.write("Home")
    st.image("c:\\Users\\karth\\Downloads\\OIP (1).webp")
    if st.checkbox("Show Table"):
        st.table(data=data)



    graph= st.selectbox("What kind of Graph?",["Non-Interactive","Interactive"],index=None)
    val=st.slider("Filter data using years",0,20)
    data=data.loc[data["YearsExperience"]>=val]
    if graph=="Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()



    if graph=="Interactive":
        layout=go.Layout(
            xaxis=dict(range=[0,16]),
            yaxis=dict(range=[0,2100000])
        )
        fig=go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"],mode="markers"),
                      layout=layout)
        st.plotly_chart(fig)
        









#prediction page
if navigation=="Prediction":
    st.header("Know your Salary")
    val=st.number_input("Enter your exp",0.00,20.00,step=0.25)
    val=np.array(val).reshape(1,-1)
    st.write("Prediction")

    predict= lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(predict)}")

if st.checkbox("Show Model Accuracy Metrics"):
    y_pred = lr.predict(x)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    st.subheader("Model Performance Metrics")
    st.write(f"R² Score: {r2:.2f}")
    st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
    st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")









#contribution page
if navigation=="Contribute":
    st.header("Contribute to our dataset")
    ex=st.number_input("Enter your Experience",0.00,20.00)
    sal=st.number_input("Enter your Salary",0.00,1000000.00,step=1000.00)

    if st.button("submit"):
        to_add={"YearsExperience":ex,"Salary":sal}
        to_add=pd.DataFrame([to_add])
        to_add.to_csv("D:\\computer science\\ai and data science\\env\\Salary_Data.csv",mode="a",header=False,index=False)
        st.success("Submitted!!")


