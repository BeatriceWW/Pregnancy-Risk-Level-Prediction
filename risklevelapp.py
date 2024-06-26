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
    print(prediction)

    if prediction[0] == 0:
        return 'High Risk: It is crucial to seek urgent medical attention to ensure the health and safety of both you and your baby. Please consult your healthcare provider immediately.'
    elif prediction[0] == 1:
        return 'Low Risk: Your pregnancy is currently considered low risk. Continue with your regular prenatal check-ups and maintain a healthy lifestyle.'
    elif prediction[0] == 2:
        return 'Medium Risk: It is important to seek medical attention to monitor and manage any potential complications. Please schedule an appointment with your healthcare provider soon'
    else:
        return 'Error: Please enter valid numerical values'
 

def main():
    # Add title to web interface
    st.title('Pregnancy Risk Level Prediction')

    #get input from user 
    Age = st.text_input('Age')
    Body_Temperature = st.text_input('Body Temperature')
    Heart_Rate = st.text_input('Heart Rate')
    Systolic_Blood_Pressure = st.text_input('Systolic Blood Pressure')
    Diastolic_Blood_Pressure = st.text_input('Diastolic  BloodPressure')
    BMI = st.text_input('BMI')
    Blood_Glucose_HbA1c = st.text_input('Blood Glucose HbA1c')
    Blood_Glucose_Fasting = st.text_input('Blood Glucose Fasting')

    # Code for prediction 

    diagnosis = ''

    if st.button('Pregnancy Risk Level Result'):
        
        diagnosis = risk_level_prediction([Age, Body_Temperature, Heart_Rate, 
                                   Systolic_Blood_Pressure, Diastolic_Blood_Pressure,
                                   BMI, Blood_Glucose_HbA1c, Blood_Glucose_Fasting])
    
    st.success(diagnosis)


if __name__ == '__main__':
    main() 
