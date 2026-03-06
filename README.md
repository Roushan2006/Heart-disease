❤️ Heart Disease Prediction System
This repository contains a complete Machine Learning pipeline for predicting heart disease risk. It features a data analysis and model training workflow in a Jupyter Notebook, and a user-friendly web application built with Streamlit for real-time diagnostics.

🌟 Overview
The goal of this project is to provide a tool for early detection of heart disease. By analyzing clinical parameters such as cholesterol levels, maximum heart rate, and chest pain types, the system calculates the probability of heart disease and generates a downloadable medical report.

🛠️ Tech Stack
Python 3.8+

Machine Learning: Scikit-learn (Logistic Regression)

Data Processing: Pandas, NumPy

Visualization: Plotly, Seaborn, Matplotlib

Web Framework: Streamlit

Report Generation: ReportLab

📂 Project Structure
Plaintext
├── Dataset/
│   └── heart.csv          # Raw clinical data
├── models/
│   ├── lr.pkl             # Trained Logistic Regression model
│   └── scaler.pkl         # Fitted Standard Scaler
├── app.py                 # Streamlit web application
├── simple.ipynb           # Data analysis & model training notebook
└── README.md              # Project documentation
🚀 Getting Started
1. Installation
Clone the repository and install the required dependencies:

Bash
git clone https://github.com/Roushan2006/heart-disease-prediction.git
cd heart-disease-prediction
pip install streamlit pandas plotly reportlab scikit-learn
2. Run the Application
Launch the interactive dashboard locally:

Bash
streamlit run app.py
📊 Features
Clinical Dashboard: Input 11 medical parameters (Age, Sex, Resting BP, etc.) to get an instant prediction.

Risk Visualization: * Gauge Chart: Shows the risk percentage on a scale (Low, Medium, High).

Probability Analysis: A bar chart comparing the likelihood of being healthy vs. having heart disease.

Medical Report: Generate a professional PDF report containing the patient's inputs and the model's findings for record-keeping.

🧠 Model Development
The model was trained in simple.ipynb using the Heart Failure Prediction dataset. Key steps included:

Preprocessing: One-hot encoding for categorical variables (Sex, Chest Pain Type, etc.).

Scaling: Standard scaling to normalize clinical ranges.

Evaluation: The Logistic Regression model was chosen for its interpretability and performance on binary classification for medical data.

📋 Features Explained
The model takes the following inputs:

Chest Pain Type: TA, ATA, NAP, ASY.

Resting ECG: Normal, ST, LVH.

Exercise Angina: Yes/No.

ST Slope: Up, Flat, Down.

Disclaimer: This tool is for educational purposes only and should not be used as a substitute for professional medical advice.
