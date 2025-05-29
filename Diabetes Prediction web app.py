import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/Documents/B.Tech/Some new projects/trained_models.sav','rb'))

#creating a function for prediction 
def diabetes_prediction(input_data):
    
    # we convert the list into numpy array because numpy array is better for such operation rather than list
    input_data_as_numpy = np.asarray(input_data).reshape(1,-1) 

    prediction = loaded_model.predict(input_data_as_numpy)
    if(prediction[0]==0):
        return("The person is non-diabetic")
    else:
        return("The person is diabetic")
    
    
def main():
    
    #giving title of the web page
    st.title('Diabetic Prediction App')
    
    #getting input data from the user
    Pergnancies = st.text_input('Number of Pregnancies')
    Glucose =st.text_input('Glucose Level')
    BloodPressure =st.text_input('Blood Pressure')
    SkinThickness =st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetic Pedigree Function Value')
    Age = st.text_input('Age Of The Person')
    
    #code for the prediction 
    diagnosis =''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis= diabetes_prediction([Pergnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
    
if __name__=='__main__':
    main()