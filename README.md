# Tesla Stock Price Prediction using SimpleRNN and LSTM

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

How to Run the Project
1. Clone the Repository
git clone <your-repository-link>
cd Stock_prediction
2. Install Required Libraries
pip install -r requirements.txt
3. Run the Streamlit App
streamlit run app.py
4. Upload Dataset

After running the app:

Open the local URL shown in terminal.
Upload the Tesla stock CSV file.
The app will display the dataset preview.
The app will predict the next day Tesla closing price.
The closing price chart will also be shown.
Dataset Format

The CSV file should contain at least this column:

Close

Recommended columns:

Date, Open, High, Low, Close, Adj Close, Volume
Model Details

The project uses:

SimpleRNN

SimpleRNN is used as a baseline recurrent neural network model for stock price prediction.

LSTM

LSTM is used because it can capture long-term dependencies in time-series data better than SimpleRNN.

Evaluation Metrics

The models are evaluated using:

Mean Squared Error
Root Mean Squared Error
Mean Absolute Error
Final Conclusion

LSTM performed better than SimpleRNN because it can retain long-term time-series patterns more effectively. The model can predict Tesla's next closing price using the previous 60 days of closing price data.

Author

Updesh Chauhan
