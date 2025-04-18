
import streamlit as st
from model_utils import get_hr_score

st.set_page_config(page_title="HR Predictor (Original Formula)", layout="centered")

st.title("💣 HR Prediction Model – Original")

st.markdown("This version uses your original formula, fully intact. No changed weights, no hidden modifiers.")

with st.form("hr_form"):
    st.markdown("### 🧨 Hitter Stats")
    batter_name = st.text_input("Batter Name")

    barrel_rate = st.slider("Barrel Rate (%)", 0.0, 30.0, 10.0)
    exit_velocity = st.slider("Exit Velocity (mph)", 70.0, 120.0, 91.0)
    xSLG = st.slider("Expected Slugging (xSLG)", 0.300, 0.800, 0.650, step=0.01)
    sweet_spot = st.slider("Sweet Spot Contact (%)", 0.0, 60.0, 35.0)
    rpi = st.slider("Recent Performance Index (RPI)", 0.0, 1.0, 0.5, step=0.01)

    st.markdown("### ⚾ Pitcher Stats")
    hr9 = st.slider("HRs Allowed per 9 IP", 0.0, 3.0, 1.2)
    hard_hit_pct = st.slider("Hard-Hit % Allowed", 20.0, 60.0, 35.0)
    fatigue = st.slider("Fatigue (0–10)", 0, 10, 5)

    # Context placeholder
    park_factor = 0
    wind_boost = 0
    temp_boost = 0

    submitted = st.form_submit_button("Calculate HR Probability")
    if submitted:
        score, sleeper = get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                                      hr9, hard_hit_pct, fatigue,
                                      park_factor, wind_boost, temp_boost)
        st.subheader(f"🔢 HR Probability Score: {score} / 100")
        if sleeper:
            st.markdown("💡 **Sleeper Tag: This batter has sneaky upside.**")
