import streamlit as st
import pandas as pd

st.title("Daily Wellness Tracker 🌱")
st.write("Track your mood, water intake, and energy level")

# Section 1: Daily Check-in
st.subheader("Section 1: Daily Check-in")

username = st.text_input("Enter your name", key="user")
mood = st.selectbox(
    "How is your mood today?",
    ["Happy 😊", "Neutral 😐", "Stressed 😟"],
    key="mood"
)
water = st.number_input(
    "Glasses of water consumed",
    min_value=0,
    max_value=20,
    key="water"
)

if st.button("Log Today", key="log_btn"):
    st.write("Name:", username)
    st.write("Mood:", mood)
    st.write("Water Intake:", water, "glasses")

# ---------------------------------------------

st.markdown("---")
st.subheader("Section 2: Wellness Tips")

tips = [
    {"Tip": "Drink Water", "Benefit": "Improves focus"},
    {"Tip": "Exercise", "Benefit": "Boosts energy"},
    {"Tip": "Sleep Well", "Benefit": "Better mood"}
]

st.table(tips)

# ---------------------------------------------

st.markdown("---")
st.subheader("Section 3: Wellness Log (Persistent)")

if "wellness_log" not in st.session_state:
    st.session_state.wellness_log = []

energy = st.slider("Energy Level", 1, 10, key="energy")

if st.button("Save Log", key="save_btn"):
    if username:
        st.session_state.wellness_log.append({
            "Name": username,
            "Mood": mood,
            "Water": water,
            "Energy": energy
        })
        st.success("Log saved successfully!")
    else:
        st.warning("Please enter your name")

df = pd.DataFrame(st.session_state.wellness_log)
st.dataframe(df)

# ---------------------------------------------

st.markdown("---")
st.subheader("Section 4: Energy Analysis")

if not df.empty:
    st.bar_chart(df.set_index("Name")["Energy"])