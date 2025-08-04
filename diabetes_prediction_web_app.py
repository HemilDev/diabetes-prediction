import numpy as np
import pickle
import streamlit as st

# Loding the saved model
model_path = r"C:\Users\hemil\ML\project\Diabetes Prediction\trained model.sav"
loaded_model = pickle.load(open(model_path, 'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return ('The person is not diabetic')
    else:
        return ('The person is diabetic')
    
def main():

    # giving a title
    st.title('Diabetes prediction web App')

    # Getting the input data from the user
    pregnancies = st.text_input("Number of Pregnancies")
    glucose = st.text_input("Glucose level")
    blood_pressure = st.text_input("Blood Pressure value")
    skin_thickness = st.text_input("Skin Thickness value")
    insulin = st.text_input("Insulin Level")
    bmi = st.text_input("BMI value")
    diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function value")
    age = st.text_input("Age of the Person")



    # Creating a Button for prediction
    if st.button('Diabetes Test Result'):
        # Check if any field is empty or contains non-numeric data
        try:
            input_data = [
                float(pregnancies),
                float(glucose),
                float(blood_pressure),
                float(skin_thickness),
                float(insulin),
                float(bmi),
                float(diabetes_pedigree_function),
                float(age)
            ]
            # Make the prediction
            diagnosis = diabetes_prediction(input_data)
            st.success(diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")


if __name__ == '__main__':
    main()

