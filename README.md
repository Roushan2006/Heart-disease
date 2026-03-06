❤️ Heart Disease Prediction System
This repository provides an end-to-end solution for predicting heart disease risk. The project covers the entire machine learning lifecycle, from data analysis and model training to deployment via a user-friendly web interface.

📁 Project Overview
The project is divided into two main components:

Analysis (simple.ipynb): A Jupyter Notebook containing the data exploration, preprocessing, and training of a Logistic Regression model.

Application (app.py): A robust Streamlit application that allows users to input clinical data and receive real-time risk predictions, complete with visual feedback and downloadable medical reports.

🚀 Key Features
Machine Learning Integration: Uses a pre-trained Logistic Regression model and StandardScaler to process patient input accurately.

Visual Risk Assessment:

Risk Gauge: Displays a dynamic gauge indicating low, moderate, or high-risk levels.

Probability Analysis: Uses Plotly to show the probability breakdown of the prediction.

Automated Reporting: Generates instant, professional-style PDF summaries for patients using reportlab.

Responsive UI: A custom-styled Streamlit interface featuring background imagery and structured data inputs.

🛠️ Technical Stack
Core: Python, Pandas, NumPy

Machine Learning: Scikit-learn, Pickle

Visualization: Plotly (Gauge charts & Bar charts), Seaborn, Matplotlib

Web Framework: Streamlit

PDF Generation: ReportLab

📋 How to Run
Prerequisites
Ensure you have the required libraries installed:

Bash
pip install streamlit pandas plotly reportlab scikit-learn
Execution
Clone the repository:

Bash
git clone https://github.com/Roushan2006/heart-disease-prediction.git
cd heart-disease-prediction
Launch the App:

Bash
streamlit run app.py
🏗️ Data Flow
The system processes data in three distinct stages:

Raw Data Processing: Loading heart.csv in simple.ipynb.

Feature Scaling: Transforming inputs via models/scaler.pkl to match the training distribution.

Inference: Predicting the target class using models/lr.pkl and rendering the results in the browser.

⚖️ Disclaimer
This tool is for educational and demonstrative purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider regarding a medical condition.
