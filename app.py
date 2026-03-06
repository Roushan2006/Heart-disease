import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import plotly.express as px
import io

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-image: url("https://img.freepik.com/free-photo/blur-hospital_1203-7972.jpg");
    background-size: cover;
}

.block-container {
    background-color: rgba(255,255,255,0.92);
    padding: 2rem;
    border-radius: 15px;
}

h1 {
    color:#c1121f;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)


with open('./models/lr.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('./models/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('./models/columns.pkl', 'rb') as columns_file:
    ex_columns = pickle.load(columns_file)


def create_pdf_report(data, prediction, probability):

    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("Heart Disease Prediction Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1,20))

    result = "High Risk" if prediction == 1 else "Low Risk"

    summary = Paragraph(
        f"<b>Prediction Result:</b> {result}<br/>"
        f"<b>Risk Probability:</b> {round(probability*100,2)}%",
        styles['Normal']
    )

    elements.append(summary)
    elements.append(Spacer(1,20))

    table_data = [["Feature", "Value"]]

    for key, value in data.items():
        table_data.append([key, str(value)])

    table = Table(table_data)
    elements.append(table)

    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    pdf.build(elements)

    buffer.seek(0)

    return buffer


st.title("❤️ AI Heart Disease Prediction System")
st.markdown("Provide the following patient details")


col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 16,100,40)
    sex = st.selectbox("Sex",['M',"F"])
    chest_pain = st.selectbox("Chest Pain Type",["ATA", "NAP", "TA","ASY"])

with col2:
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholestrol = st.number_input("Cholesterol (mg/DL)", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar >120 mg/DL",[0,1])

with col3:
    resting_ecg = st.selectbox("Resting ECG", ['Normal','ST','LVH'])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise Angina", ['Y','N'])

oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])


if st.button("🔍 Predict Heart Disease"):

    raw_input = {
        'Age' : age,
        'RestingBP' : resting_bp,
        'Cholesterol' : cholestrol,
        'FastingBS' : fasting_bs,
        'MaxHR' : max_hr,
        'Oldpeak' : oldpeak,
        'Sex_' + sex : 1,
        'ChestPainType_' + chest_pain : 1,
        'RestingECG_' + resting_ecg : 1,
        'ExerciseAngina_' + exercise_angina : 1,
        'ST_Slope_' + st_slope : 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in ex_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[ex_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    st.subheader("🧠 Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk Of Heart Disease")
    else:
        st.success("✅ Low Risk Of Heart Disease")


    prob_df = pd.DataFrame({
        "Category":["Low Risk","High Risk"],
        "Probability":[1-probability, probability]
    })

    bar_fig = px.bar(
        prob_df,
        x="Category",
        y="Probability",
        text="Probability",
        color="Category",
        title="📊 Prediction Probability"
    )

    st.plotly_chart(bar_fig, use_container_width=True)


    risk_score = probability * 100

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={'text': "❤️ Heart Disease Risk %"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "red"},
            'steps': [
                {'range':[0,30],'color':'green'},
                {'range':[30,70],'color':'yellow'},
                {'range':[70,100],'color':'red'}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)


    report_data = {
        "Age": age,
        "Sex": sex,
        "Chest Pain Type": chest_pain,
        "Resting BP": resting_bp,
        "Cholesterol": cholestrol,
        "Fasting Blood Sugar": fasting_bs,
        "Resting ECG": resting_ecg,
        "Max Heart Rate": max_hr,
        "Exercise Angina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST Slope": st_slope
    }

    pdf_file = create_pdf_report(report_data, prediction, probability)

    st.download_button(
        label="📄 Download Patient Report",
        data=pdf_file,
        file_name="heart_disease_report.pdf",
        mime="application/pdf"
    )