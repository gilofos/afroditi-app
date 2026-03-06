import streamlit as st
import datetime
import random

# --- ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="MyPregnancyGuide 🌸", layout="wide")
st.markdown("""<style>
    .stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
    .welcome-box { background: white; padding: 20px; border-radius: 20px; border: 2px solid #9c27b0; text-align: center; margin-bottom: 20px; }
    .card { background: white; padding: 15px; border-radius: 15px; border-left: 8px solid #9c27b0; margin-bottom: 10px; }
</style>""", unsafe_allow_html=True)

# --- STATE ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0

# --- SIDEBAR (Εδώ βάλαμε Γιατρό & Μαία) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png", width=180)
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    
    st.subheader("💧 Hydration Tracker")
    cw1, cw2 = st.columns(2)
    with cw1:
        if st.button("🥛 Ήπια!"): st.session_state.water += 1
    with cw2:
        if st.button("🔄 Reset"): st.session_state.water = 0
    st.write(f"**Σύνολο:** {st.session_state.water} ποτή
