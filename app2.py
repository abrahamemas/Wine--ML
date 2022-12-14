
import streamlit as st        
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
st.title("Wine Prediction")

html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Wine Classification</h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
st.sidebar.header('User Input Parameters')
st.cache()
  
def user_input_features():
        fixed_acidity = st.sidebar.slider('fixed acidity', 4.6, 15.9, 8.31)
        volatile_acidity = st.sidebar.slider('volatile acidity', 0.12,1.58 , 0.52)
        citric_acid = st.sidebar.slider('citric acid', 0.0,1.0 , 0.5)
        chlorides = st.sidebar.slider('chlorides', 0.01,0.6 , 0.08)
        total_sulfur_dioxide=st.sidebar.slider('total sulfur dioxide', 6.0,289.0 , 46.0)
        alcohol=st.sidebar.slider('alcohol', 8.4,14.9, 10.4)
        sulphates=st.sidebar.slider('sulphates', 0.33,2.0,0.65 )
        data = {'fixed_acidity': fixed_acidity,
                'volatile_acidity': volatile_acidity,
                'citric_acid': citric_acid,
                'chlorides': chlorides,
              'total_sulfur_dioxide':total_sulfur_dioxide,
              'alcohol':alcohol,
                'sulphates':sulphates}
        features = pd.DataFrame(data, index=[0])
        return features
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

data=pd.read_csv("wine-quality-white-and-red.csv")
X =np.array(data[['fixed acidity', 'volatile acidity' , 'citric acid' , 'chlorides' , 'total sulfur dioxide' , 'alcohol' , 'sulphates']])
Y = np.array(data['quality'])
clf = RandomForestClassifier()
clf.fit(X, Y)
st.subheader('Class labels and their corresponding index number')


prediction = clf.predict(df)
st.write(prediction)

st.subheader('Prediction')
st.write(prediction)


