# Tesla Stock Price Prediction using SimpleRNN and LSTM

## Author

**Updesh Chauhan**

This project predicts Tesla stock closing prices using Deep Learning models.  
It uses historical Tesla stock data and compares SimpleRNN and LSTM models for stock price forecasting.

## Project Features

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Closing price trend visualization
- Moving average analysis
- SimpleRNN model
- LSTM model
- 1-day stock price prediction
- 5-day and 10-day forecasting
- Hyperparameter tuning
- Streamlit web app deployment

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras
- Streamlit
- Joblib

## Project Overview

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd Stock_prediction
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

### 4. Upload Dataset

After running the application:

1. Open the local URL displayed in the terminal.
2. Upload the Tesla stock CSV dataset.
3. View the dataset preview.
4. Generate stock price predictions.
5. Visualize the Tesla closing price trend.

---

## Dataset Format

The CSV file should contain at least the following column:

```text
Close
```

Recommended dataset columns:

```text
Date
Open
High
Low
Close
Adj Close
Volume
```

---

## Model Details

### SimpleRNN

SimpleRNN is used as a baseline recurrent neural network model for stock price prediction. It learns sequential patterns from historical stock prices and provides a benchmark for comparison.

### LSTM

LSTM (Long Short-Term Memory) is used because it can capture long-term dependencies in time-series data more effectively than SimpleRNN. This makes it more suitable for stock price forecasting.

---

## Evaluation Metrics

The models are evaluated using the following metrics:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)

---

## Project Structure

```text
Stock_prediction/
│
├── app.py
├── model_lstm.keras
├── scaler.pkl
├── requirements.txt
├── README.md
├── report.pdf
│
├── data/
│   └── TSLA.csv
│
└── notebooks/
    └── tesla_stock_prediction.ipynb
