# ============================================================================
# HEART DISEASE PREDICTION SYSTEM - STREAMLIT FRONTEND
# ============================================================================
# Author: AI/ML Student
# Description: Professional UI for Heart Disease Prediction using Streamlit
# ============================================================================

# Import required libraries
import streamlit as st
import numpy as np
import pickle

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: #DC143C;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    
    /* Card styling for sections */
    .input-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    
    /* Result card styling */
    .result-card-high {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(231, 76, 60, 0.4);
        margin: 20px 0;
    }
    
    .result-card-low {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(39, 174, 96, 0.4);
        margin: 20px 0;
    }
    
    .result-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .result-text {
        font-size: 1.1rem;
    }
    
    /* Section headers */
    .section-header {
        color: #2c3e50;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 25px 0 15px 0;
        padding-bottom: 10px;
        border-bottom: 3px solid #3498db;
    }
    
    /* Info box styling */
    .info-box {
        background-color: #e8f4f8;
        border-left: 5px solid #3498db;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }
    
    /* Summary table styling */
    .summary-table {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #888;
        border-top: 1px solid #eee;
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(231, 76, 60, 0.4);
    }
    
    /* Divider styling */
    .divider {
        height: 3px;
        background: linear-gradient(90deg, #e74c3c, #3498db, #27ae60);
        margin: 30px 0;
        border-radius: 2px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER SECTION
# ============================================================================
st.markdown('<h1 class="main-title">❤️ Heart Disease Prediction System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🏥 Enter patient details below to predict heart disease risk</p>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================================================
# LOAD MODEL (Placeholder - Replace with your actual model)
# ============================================================================
# Uncomment and modify the following lines to load your trained model:
# @st.cache_resource
# def load_model():
#     with open('heart_disease_model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     return model
# model = load_model()

# For demonstration, we'll create a dummy prediction function
def dummy_predict(features):
    """
    Dummy prediction function for demonstration.
    Replace this with: prediction = model.predict(features)
    """
    # This is just for demo - remove when using actual model
    return np.random.choice([0, 1])

# ============================================================================
# INFORMATION BOX
# ============================================================================
st.markdown("""
<div class="info-box">
    <strong>ℹ️ Instructions:</strong> Please fill in all the patient medical details accurately. 
    All fields are required for accurate prediction.
</div>
""", unsafe_allow_html=True)

# ============================================================================
# INPUT SECTION - PATIENT DETAILS
# ============================================================================
st.markdown('<p class="section-header">📋 Patient Medical Information</p>', unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns(2)

# ----------------------------------------------------------------------------
# Column 1 Inputs
# ----------------------------------------------------------------------------
with col1:
    # Age Input
    age = st.number_input(
        "🎂 Age (years)",
        min_value=1,
        max_value=120,
        value=45,
        step=1,
        help="Enter patient's age in years"
    )
    
    # Sex Input
    sex_display = st.selectbox(
        "👤 Sex",
        options=["Male", "Female"],
        help="Select patient's biological sex"
    )
    sex = 1 if sex_display == "Male" else 0
    
    # Chest Pain Type Input
    chest_pain_options = {
        "Type 0: Typical Angina": 0,
        "Type 1: Atypical Angina": 1,
        "Type 2: Non-Anginal Pain": 2,
        "Type 3: Asymptomatic": 3
    }
    chest_pain_display = st.selectbox(
        "💔 Chest Pain Type",
        options=list(chest_pain_options.keys()),
        help="Select the type of chest pain experienced"
    )
    chest_pain_type = chest_pain_options[chest_pain_display]
    
    # Resting Blood Pressure
    resting_bp = st.number_input(
        "🩸 Resting Blood Pressure (mm Hg)",
        min_value=50,
        max_value=250,
        value=120,
        step=1,
        help="Enter resting blood pressure in mm Hg"
    )
    
    # Cholesterol
    cholesterol = st.number_input(
        "🧪 Cholesterol (mg/dl)",
        min_value=100,
        max_value=600,
        value=200,
        step=1,
        help="Enter serum cholesterol in mg/dl"
    )
    
    # Fasting Blood Sugar
    fbs_display = st.selectbox(
        "🍬 Fasting Blood Sugar > 120 mg/dl",
        options=["No", "Yes"],
        help="Is fasting blood sugar greater than 120 mg/dl?"
    )
    fasting_blood_sugar = 1 if fbs_display == "Yes" else 0

# ----------------------------------------------------------------------------
# Column 2 Inputs
# ----------------------------------------------------------------------------
with col2:
    # Resting ECG
    ecg_options = {
        "Normal (0)": 0,
        "ST-T Wave Abnormality (1)": 1,
        "Left Ventricular Hypertrophy (2)": 2
    }
    ecg_display = st.selectbox(
        "📊 Resting ECG Results",
        options=list(ecg_options.keys()),
        help="Select resting electrocardiographic results"
    )
    resting_ecg = ecg_options[ecg_display]
    
    # Maximum Heart Rate
    max_heart_rate = st.number_input(
        "💓 Maximum Heart Rate Achieved",
        min_value=50,
        max_value=250,
        value=150,
        step=1,
        help="Enter maximum heart rate achieved during exercise"
    )
    
    # Exercise Induced Angina
    angina_display = st.selectbox(
        "🏃 Exercise Induced Angina",
        options=["No", "Yes"],
        help="Does exercise induce angina?"
    )
    exercise_angina = 1 if angina_display == "Yes" else 0
    
    # Oldpeak (ST Depression)
    oldpeak = st.number_input(
        "📉 Oldpeak (ST Depression)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
        format="%.1f",
        help="ST depression induced by exercise relative to rest"
    )
    
    # ST Slope
    slope_options = {
        "Upsloping (0)": 0,
        "Flat (1)": 1,
        "Downsloping (2)": 2
    }
    slope_display = st.selectbox(
        "📈 ST Slope",
        options=list(slope_options.keys()),
        help="The slope of the peak exercise ST segment"
    )
    st_slope = slope_options[slope_display]

# ============================================================================
# DISPLAY ENTERED VALUES
# ============================================================================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="section-header">📝 Patient Data Summary</p>', unsafe_allow_html=True)

# Create summary display
summary_col1, summary_col2 = st.columns(2)

with summary_col1:
    st.markdown(f"""
    | **Parameter** | **Value** |
    |:--------------|:----------|
    | 🎂 Age | {age} years |
    | 👤 Sex | {sex_display} |
    | 💔 Chest Pain Type | {chest_pain_display.split(':')[0]} |
    | 🩸 Resting BP | {resting_bp} mm Hg |
    | 🧪 Cholesterol | {cholesterol} mg/dl |
    | 🍬 Fasting Blood Sugar >120 | {fbs_display} |
    """)

with summary_col2:
    st.markdown(f"""
    | **Parameter** | **Value** |
    |:--------------|:----------|
    | 📊 Resting ECG | {ecg_display.split('(')[0].strip()} |
    | 💓 Max Heart Rate | {max_heart_rate} bpm |
    | 🏃 Exercise Angina | {angina_display} |
    | 📉 Oldpeak | {oldpeak} |
    | 📈 ST Slope | {slope_display.split('(')[0].strip()} |
    """)

# ============================================================================
# PREDICTION SECTION
# ============================================================================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Center the predict button
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    predict_button = st.button("🔍 Predict Heart Disease Risk", use_container_width=True)

# ============================================================================
# HANDLE PREDICTION
# ============================================================================
if predict_button:
    # Prepare input data for model
    input_data = np.array([[
        age,
        sex,
        chest_pain_type,
        resting_bp,
        cholesterol,
        fasting_blood_sugar,
        resting_ecg,
        max_heart_rate,
        exercise_angina,
        oldpeak,
        st_slope
    ]])
    
    # Validate inputs (basic validation)
    is_valid = True
    
    # Age validation
    if age < 1 or age > 120:
        st.error("❌ Please enter a valid age (1-120 years)")
        is_valid = False
    
    # Blood pressure validation
    if resting_bp < 50 or resting_bp > 250:
        st.error("❌ Please enter a valid resting blood pressure (50-250 mm Hg)")
        is_valid = False
    
    # Cholesterol validation
    if cholesterol < 100 or cholesterol > 600:
        st.error("❌ Please enter a valid cholesterol level (100-600 mg/dl)")
        is_valid = False
    
    # Heart rate validation
    if max_heart_rate < 50 or max_heart_rate > 250:
        st.error("❌ Please enter a valid maximum heart rate (50-250 bpm)")
        is_valid = False
    
    if is_valid:
        # Show loading spinner during prediction
        with st.spinner("🔄 Analyzing patient data..."):
            import time
            time.sleep(1)  # Simulate processing time
            
            # ================================================================
            # MAKE PREDICTION
            # ================================================================
            # Replace dummy_predict with your actual model prediction:
            # prediction = model.predict(input_data)
            prediction = dummy_predict(input_data)  # Demo only
        
        # Display results
        st.markdown("---")
        
        if prediction == 1:
            # HIGH RISK Result
            st.markdown("""
            <div class="result-card-high">
                <div class="result-title">⚠️ HIGH RISK DETECTED</div>
                <div class="result-text">
                    The patient shows <strong>high risk indicators</strong> for heart disease.<br>
                    Please consult a cardiologist immediately for further evaluation.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Additional recommendations for high risk
            st.error("🚨 **Immediate Actions Recommended:**")
            st.markdown("""
            - 🏥 Schedule an appointment with a cardiologist
            - 🩺 Get a comprehensive cardiac evaluation
            - 💊 Review current medications with your doctor
            - 🥗 Consider lifestyle modifications
            - 🚭 Avoid smoking and excessive alcohol
            """)
            
        else:
            # LOW RISK Result
            st.markdown("""
            <div class="result-card-low">
                <div class="result-title">✅ LOW RISK</div>
                <div class="result-text">
                    The patient shows <strong>low risk indicators</strong> for heart disease.<br>
                    Continue maintaining a healthy lifestyle!
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Additional recommendations for low risk
            st.success("🌟 **Keep Up the Good Work!**")
            st.markdown("""
            - 🏃 Maintain regular physical activity
            - 🥗 Continue with a balanced diet
            - 😴 Get adequate sleep (7-8 hours)
            - 🧘 Manage stress effectively
            - 📅 Schedule regular health check-ups
            """)

# ============================================================================
# ADDITIONAL INFORMATION SECTION
# ============================================================================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Expandable section for more information
with st.expander("ℹ️ About This Prediction System"):
    st.markdown("""
    ### How It Works
    This Heart Disease Prediction System uses machine learning algorithms to analyze 
    patient medical data and predict the risk of heart disease.
    
    ### Important Disclaimer
    ⚠️ **This tool is for educational and informational purposes only.** 
    It should NOT be used as a substitute for professional medical advice, 
    diagnosis, or treatment. Always consult with qualified healthcare providers 
    for any health-related decisions.
    
    ### Features Analyzed
    The model considers the following medical parameters:
    - **Age**: Patient's age in years
    - **Sex**: Biological sex (Male/Female)
    - **Chest Pain Type**: Classification of chest pain (0-3)
    - **Resting Blood Pressure**: BP at rest in mm Hg
    - **Cholesterol**: Serum cholesterol in mg/dl
    - **Fasting Blood Sugar**: Whether FBS > 120 mg/dl
    - **Resting ECG**: Electrocardiographic results
    - **Maximum Heart Rate**: Peak heart rate during exercise
    - **Exercise Induced Angina**: Angina triggered by exercise
    - **Oldpeak**: ST depression during exercise
    - **ST Slope**: Slope of peak exercise ST segment
    """)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <p>💻 <strong>Developed by AI/ML Student</strong></p>
    <p>🏥 Heart Disease Prediction System v1.0</p>
    <p>⚠️ For educational purposes only - Not a substitute for professional medical advice</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR (Optional - Additional Features)
# ============================================================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/heart-with-pulse.png", width=80)
    st.title("Quick Guide")
    
    st.markdown("---")
    st.markdown("### 📌 How to Use")
    st.markdown("""
    1. Enter all patient details
    2. Review the summary
    3. Click 'Predict' button
    4. View the results
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Risk Factors")
    st.markdown("""
    - High blood pressure
    - High cholesterol
    - Smoking
    - Diabetes
    - Obesity
    - Physical inactivity
    - Unhealthy diet
    - Age
    """)
    
    st.markdown("---")
    st.markdown("### 🆘 Emergency")
    st.markdown("""
    If experiencing chest pain or 
    heart attack symptoms, 
    **call emergency services 
    immediately!**
    
    🚨 **Emergency: 911 (US)**
    """)

