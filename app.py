import streamlit as st
import joblib
import pandas as pd
import os
import requests

# Download model if not present locally
model_path = 'diamond_price_pred.pkl'
if not os.path.exists(model_path):
    st.info("Downloading model file...")
    # Replace with your actual storage URL
    url = "https://your-storage-url.com/diamond_price_pred.pkl"
    r = requests.get(url, allow_redirects=True)
    with open(model_path, 'wb') as f:
        f.write(r.content)
    st.success("Model downloaded successfully!")

model = joblib.load(model_path)

# Streamlit UI
st.title("💎 Diamond Price Prediction 💎")
st.write("using Random Forest Regressor")

# Input fields
cut = st.selectbox('cut : ', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('color : ',['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('clarity : ', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
carat = st.slider("carat weight (1 carat = 200mg) : ", min_value=0.2, max_value=10.0, step=0.01)
depth = st.slider("depth %: ", min_value=40.0, max_value=80.0, step=0.01)
table = st.slider("table %: ", min_value=40.0, max_value=100.0, step=0.01)
x = st.slider("x (Premium)", min_value=0.0, max_value=20.0, step=0.01)
z = st.slider("z (Very Good)", min_value=0.0, max_value=40.0, step=0.01)
y = st.slider("y (Good)", min_value=0.0, max_value=60.0, step=0.01)

# Predict Button
if st.button('Predict Price'):
    # Create input data
    input_data = pd.DataFrame({
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'carat': [carat],
        'depth': [depth],
        'table': [table],
        'x (Premium)': [x],
        'z (Very Good)': [z],
        'y (Good)': [y]
    })
    
    # Prediction
    prediction = model.predict(input_data)

    # Display result
    st.success("Predicted Price: $ "+str(prediction))