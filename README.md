# 📊 Stock Price Trend Prediction using Machine Learning

## 🚀 Overview

This project predicts the **trend of stock prices** (UP 📈 or DOWN 📉) using Machine Learning techniques. Instead of predicting exact prices, the model focuses on trend direction, which is more realistic and practical.

---

## 🎯 Objective

To build a machine learning model that:

* Analyzes historical stock data
* Learns patterns using technical indicators
* Predicts whether the stock price will go up or down

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* yfinance
* TA (Technical Analysis library)
* Streamlit (for UI)

---

## 📁 Project Structure

```
stock_trend_project/
│
├── data/
├── notebooks/
├── src/
│   ├── data_collection.py
│   ├── features.py
│   ├── model.py
│   ├── evaluate.py
│   └── predict.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Features Used

* Moving Average (MA10, MA50)
* Relative Strength Index (RSI)
* Daily Returns

---

## 🤖 Model Used

* Random Forest Classifier

---

## 📊 Workflow

1. Data Collection using Yahoo Finance
2. Feature Engineering
3. Target Creation (UP/DOWN)
4. Model Training
5. Evaluation
6. Prediction

---

## 📈 Output Example

* Prediction: 📈 UP
* Accuracy: ~70% (varies by stock)

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone <your-repo-link>
cd stock_trend_project
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Model

```
python main.py
```

### 5. Run UI

```
streamlit run app.py
```

---

## ⚠️ Disclaimer

This project is for educational purposes only.
Stock market predictions are uncertain and should not be used for financial decisions.

---

## 🌟 Future Improvements

* LSTM Deep Learning model
* Real-time prediction
* More technical indicators (MACD, Bollinger Bands)
* Model optimization

---

## 👨‍💻 Author

Your Name
AI/ML Student
