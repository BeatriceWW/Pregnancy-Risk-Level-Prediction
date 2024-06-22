import numpy as np 
import streamlit as st 
import pickle

#Load saved model 

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#Create a prediction function 

def risk_level_prediction(input_data):
    # Convert the input data into a numpy array
    input_data_as_numpy = np.asarray(input_data)

     # Reshape the array since we are predicting for one instance
    input_data_reshape = input_data_as_numpy.reshape(1,-1)

     # Making prediction
    prediction = loaded_model.predict(input_data_reshape)
    print (prediction)

    if prediction[0] == 0:
        print('You have a high risk pregnancy, please seek urgent medical attention')
    elif prediction[0] == 1:
        print('You have a low risk pregnancy')
    elif prediction[0] == 2:
        print('You have medium risk pregnancy, please seek medical attention')
    else:
        print('Error: please enter your health data again')

def main():
    # Add title to web interface

    st.title('Pregnancy Risk Level Prediction')

    #get input from user 
    Age = st.text_input('Age')
    Body_Temperature = st.text_input(' Body Temperature')
    Heart_Rate = st.text_input(' Heart Rate')
    Systolic_Blood_Pressure = st.text_input('  Systolic Blood Pressure')
    Diastolic_Blood_Pressure = st.text_input('Diastolic_Blood_Pressure')
    BMI = st.text_input('BMI')
    Blood_Glucose_HbA1c = st.text_input('Blood_Glucose_HbA1c')
    Blood_Glucose_Fasting = st.text_input('Blood_Glucose_Fasting ')

    # Code for prediction 

    diagnosis = ''

    if st.button('Pregnancy Risk Level Result'):
        diagnosis = risk_level_prediction( [ Age, Body_Temperature, Heart_Rate, Systolic_Blood_Pressure, Diastolic_Blood_Pressure,
                                            BMI, Blood_Glucose_HbA1c, Blood_Glucose_Fasting])
    
    st.success(diagnosis)


    if __name__ == '__main__':
        main()
