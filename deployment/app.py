import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# Load Model
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "customer_churn_pipeline.joblib"

model = joblib.load(MODEL_PATH)


# ============================================================
# Feature Engineering
# ============================================================

def feature_engineering(df):

    df_fe = df.copy()

    protection_support_columns = [
        "online_security",
        "online_backup",
        "device_protection",
        "tech_support"
    ]

    df_fe["protection_support_count"] = (
        df_fe[protection_support_columns]
        .eq("Yes")
        .sum(axis=1)
    )

    entertainment_columns = [
        "streaming_tv",
        "streaming_movies"
    ]

    df_fe["entertainment_count"] = (
        df_fe[entertainment_columns]
        .eq("Yes")
        .sum(axis=1)
    )

    return df_fe


# ============================================================
# Prediction Function
# ============================================================

def predict_churn(customer_data):

    customer_data = feature_engineering(customer_data)

    prediction = model.predict(customer_data)[0]

    churn_probability = model.predict_proba(
        customer_data
    )[0, 1]

    return prediction, churn_probability


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.title("📊 Churn Predictor")

    st.markdown(
        """
        ### About the Model

        This application predicts whether a customer is likely to
        churn based on their demographic, account, service and
        financial information.
        """
    )

    st.divider()

    st.markdown("### Model")

    st.info(
        """
        **Algorithm:** Random Forest

        **Task:** Binary Classification

        **Target:** Customer Churn
        """
    )

    st.markdown("### Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Accuracy", "76.79%")
        st.metric("Recall", "80.48%")

    with col2:
        st.metric("Precision", "54.23%")
        st.metric("F1 Score", "64.80%")

    st.divider()

    st.caption(
        "Built as an end-to-end machine learning project."
    )


# ============================================================
# Main Header
# ============================================================

st.title("📊 Customer Churn Prediction System")

st.markdown(
    """
    Use the form below to enter customer information and estimate
    the customer's probability of churn.
    """
)

st.divider()


# ============================================================
# Customer Information
# ============================================================

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

with col2:

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

with col3:

    tenure_months = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=1000,
        value=12,
        step=1
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )


# ============================================================
# Internet & Payment Information
# ============================================================

st.subheader("🌐 Internet & Payment Information")

col1, col2 = st.columns(2)

with col1:

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

with col2:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Mailed check",
            "Electronic check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


# ============================================================
# Financial Information
# ============================================================

st.subheader("💰 Financial Information")

col1, col2, col3 = st.columns(3)

with col1:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.00,
        step=1.00
    )

with col2:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.00,
        step=50.00
    )

with col3:

    cltv = st.number_input(
        "Customer Lifetime Value (CLTV)",
        min_value=0,
        value=5000,
        step=100
    )


# ============================================================
# Protection & Support Services
# ============================================================

st.subheader("🛡️ Protection & Support Services")

col1, col2, col3, col4 = st.columns(4)

with col1:

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes"]
    )

with col2:

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes"]
    )

with col3:

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes"]
    )

with col4:

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes"]
    )


# ============================================================
# Entertainment Services
# ============================================================

st.subheader("🎬 Entertainment Services")

col1, col2 = st.columns(2)

with col1:

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes"]
    )

with col2:

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes"]
    )


# ============================================================
# Prediction Button
# ============================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Customer Churn",
    use_container_width=True,
    type="primary"
)


# ============================================================
# Prediction
# ============================================================

if predict_button:

    customer_data = pd.DataFrame({
        "gender": [gender],
        "senior_citizen": [senior_citizen],
        "partner": [partner],
        "dependents": [dependents],
        "tenure_months": [tenure_months],
        "phone_service": [phone_service],
        "internet_service": [internet_service],
        "payment_method": [payment_method],
        "monthly_charges": [monthly_charges],
        "total_charges": [total_charges],
        "cltv": [cltv],
        "online_security": [online_security],
        "online_backup": [online_backup],
        "device_protection": [device_protection],
        "tech_support": [tech_support],
        "streaming_tv": [streaming_tv],
        "streaming_movies": [streaming_movies]
    })

    prediction, probability = predict_churn(
        customer_data
    )

    st.divider()

    # ========================================================
    # Result Section
    # ========================================================

    st.subheader("📌 Prediction Result")

    result_col1, result_col2 = st.columns([1, 2])

    with result_col1:

        if prediction == 1:

            st.error(
                "⚠️ High Churn Risk"
            )

            st.markdown(
                "The model predicts that this customer is **likely to churn**."
            )

        else:

            st.success(
                "✅ Low Churn Risk"
            )

            st.markdown(
                "The model predicts that this customer is **likely to stay**."
            )

    with result_col2:

        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

        st.progress(
            float(probability)
        )

        if probability >= 0.70:

            st.warning(
                "🔴 **High Risk:** Immediate customer retention "
                "action may be appropriate."
            )

        elif probability >= 0.40:

            st.warning(
                "🟡 **Moderate Risk:** Consider monitoring this "
                "customer and evaluating retention opportunities."
            )

        else:

            st.info(
                "🟢 **Low Risk:** The customer currently has a "
                "relatively low predicted probability of churn."
            )


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "Customer Churn Prediction • Random Forest ML Model • "
    "End-to-End Machine Learning Project"
)