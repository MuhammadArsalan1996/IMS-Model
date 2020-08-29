# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:47:38 2020

@author: Muhammad Arsalan
"""



import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Loading ML Model
IMS_model = pickle.load(open('ims.pkl', 'rb'))

@app.route('/')
def welcome():
    return "Welcome All"
@app.route('/predict',methods=["Get"])
def predict_note_authentication(DiabetesTypeOne,DiabetesTypeTwo,liverDisease
,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP):

   
    prediction=IMS_model.predict([[DiabetesTypeOne,DiabetesTypeTwo,liverDisease
,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP]])
    print(prediction)
    return prediction



def main():
    st.title("Select your Disease if necessary")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
   
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    DiabetesTypeOne = st.checkbox("DiabetesTypeOne")
    if DiabetesTypeOne:
     st.checkbox("yes", value = True,key=0);
    DiabetesTypeTwo = st.checkbox("DiabetesTypeTwo")
    if DiabetesTypeTwo:
     st.checkbox("yes", value = True,key=1)
    liverDisease = st.checkbox("liverDisease")
    if liverDisease:
     st.checkbox("yes", value = True,key=2)
    heartDisease = st.checkbox("heartDisease")
    if heartDisease:
     st.checkbox("yes", value = True,key=3)
    kidneyDisease = st.checkbox("kidneyDisease")
    if kidneyDisease:
     st.checkbox("yes", value = True,key=4)
    Flu = st.checkbox("Flu")
    if Flu:
     st.checkbox("yes", value = True,key=5)
    Fever = st.checkbox("Fever" )
    if Fever:
     st.checkbox("yes", value = True,key=6)
    LowBP = st.checkbox("LowBP" )
    if LowBP:
     st.checkbox("yes", value = True,key=7)
    HighBP= st.checkbox("HighBP")
    if HighBP:
     st.checkbox("yes", value = True,key=8)
    result=""
    if st.button("Predict"):
      result=predict_note_authentication(DiabetesTypeOne,DiabetesTypeTwo,liverDisease,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP)
    st.success('Recommended {}'.format(result)) 
   
   
       
        
        #Mobile App Api
@app.route('/predict_api',methods=['GET', 'POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''   
    data = request.get_json(force=True)
   
  # DiabetesTypeOne = data['DiabetesTypeOne']
   # DiabetesTypeTwo = data['DiabetesTypeTwo']
    #liverDisease = data['liverDisease']
    #heartDisease= data['heartDisease']
    #kidneyDisease = data['kidneyDisease']
    #Flu = data['Flu']
    #Fever = data['Fever']
    #LowBP = data['LowBP']
    #HighBP = data['HighBP']
    recommended =IMS_model.predict(data)
    recommended2 =IMS_model.predict(data)
    recommended3 =IMS_model.predict(data)
    recommended4 =IMS_model.predict(data)
    recommended5 =IMS_model.predict(data)
   

    
    return jsonify(recommended=recommended,recommended2=recommended2,recommended3=recommended3,recommended4=recommended4,recommended5=recommended5)


if __name__=='__main__':
    main()
    
    
    
