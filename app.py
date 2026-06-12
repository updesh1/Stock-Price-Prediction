# Create Streamlit App

import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Tesla Stock Price Prediction",
    layout="wide"
)

st.title("Tesla Stock Price Prediction using LSTM")

model = load_model("model_lstm.keras")
scaler = joblib.load("scaler.pkl")

uploaded_file = st.file_uploader(
    "Upload Tesla stock CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if "Close" not in df.columns:
        st.error("CSV file must contain a Close column.")
    else:
        data = df[["Close"]]

        scaled_data = scaler.transform(data)

        last_60_days = scaled_data[-60:]

        X_input = np.array(last_60_days)
        X_input = X_input.reshape(1, 60, 1)

        predicted_price = model.predict(X_input)

        predicted_price = scaler.inverse_transform(predicted_price)

        st.subheader("Predicted Next Day Closing Price")
        st.success(f"${predicted_price[0][0]:.2f}")

        st.subheader("Closing Price Chart")
        st.line_chart(df["Close"])