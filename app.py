import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
model = pickle.load(open("fish_model_5.sav", "rb"))
scaler = pickle.load(open("fish_scale.sav", "rb"))




def create_one_hot_encoding(value, num_categories):
    one_hot_encoding = [0] * num_categories
    if 0 <= value < num_categories:  # Ensure the value is within the valid range
        one_hot_encoding[int(value)] = 1
    return one_hot_encoding

# Function to make predictions
def predict(features):
    # Convert the input features to a DataFrame
    input_data = pd.DataFrame([features], columns=['CIC0', 'SM1_Dz', 'GATS1i', 'NdsCH', 'NdssC', 'MLOGP'])

    # Perform one-hot encoding for relevant features
    num_categories_index4 = 5
    num_categories_index5 = 7

    index4_value = input_data['NdsCH'].values[0]
    one_hot_encoding_index4 = create_one_hot_encoding(index4_value, num_categories_index4)

    index5_value = input_data['NdssC'].values[0]
    one_hot_encoding_index5 = create_one_hot_encoding(index5_value, num_categories_index5)

    # Update the DataFrame with one-hot encoded values
    input_data = pd.concat([input_data, pd.DataFrame([one_hot_encoding_index4], columns=[f'NdsCH_{i}' for i in range(num_categories_index4)])], axis=1)
    input_data = pd.concat([input_data, pd.DataFrame([one_hot_encoding_index5], columns=[f'NdssC_{i}' for i in range(num_categories_index5)])], axis=1)

    # Drop the original columns after encoding
    input_data = input_data.drop(['NdsCH', 'NdssC'], axis=1)

    # Scale the input data
    scaled_input = scaler.transform(input_data)

    # Make predictions
    prediction = model.predict(scaled_input)
    return prediction

# Streamlit app
def main():
    st.title("Aquatic toxicity prediction towards Pimephales Promelas")


    # User input for features
    CIC0 = st.number_input("CIC0", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    SM1_Dz = st.number_input("SM1_Dz", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    GATS1i = st.number_input("GATS1i", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    
    # Drop-down menu for NdsCH
    NdsCH_options = list(range(5))
    NdsCH = st.selectbox("NdsCH", NdsCH_options, index=2)  # Default value set to 2
    
    # Drop-down menu for NdssC
    NdssC_options = list(range(7))
    NdssC = st.selectbox("NdssC", NdssC_options, index=3)  # Default value set to 3
    
    MLOGP = st.number_input("MLOGP", min_value=0.0, max_value=10.0, step=0.1, value=5.0)

    # Make prediction
    if st.button("Predict"):
        features = [CIC0, SM1_Dz, GATS1i, NdsCH, NdssC, MLOGP]
        result = predict(features)
        st.markdown(f"<p style='font-size:20px;'>The Lethal Concentrationis {result} moles per liter(mol/L)</p>", unsafe_allow_html= True) 
          

if __name__ == "__main__":
    main()
