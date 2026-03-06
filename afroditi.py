import streamlit as st
import datetime
import random

# --- ΡΥΘΜΙΣΗ & CSS ---
st.set_page_config(page_title="MyPregnancyGuide 🌸", layout="wide")
st.markdown("""<style>
    .stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
    .welcome-box { background: white; padding: 20px; border-radius: 20px; border: 2px solid #9c27b0; text-align: center; }
    .card { background: white; padding: 15px; border-radius: 15px; border-left: 8px solid #9c27b0; margin-bottom: 10px; }
</style>""", unsafe_allow_html=True)

# --- STATE ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png", width=180)
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    st.subheader("💧 Hydration Tracker")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("🥛 Ήπια!"): st.session_state.water += 1
    with c2: 
        if st.button("🔄 Reset"): st.session_state.water = 0
    st.write(f"**Σύνολο:** {st.session_state.water} ποτήρια")

# --- HEADER ---
st.markdown('<div class="welcome-box"><h1>🌸 MyPregnancyGuide</h1><p>Το ψηφιακό σου ημερολόγιο</p></div>', unsafe_allow_html=True)
st.success(f"**💡 Συμβουλή:** {random.choice(['Πιες νερό! 💧', 'Περπάτημα! 🌿', 'Χαλάρωσε ✨'])}")

# --- TABS (Διορθωμένα) ---
t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs(["📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🎒 Βαλίτσα", "💖 Ονόματα", "📅 Ραντεβού", "⚙️ Εργαλεία", "📋 Αναφορά"])

with t1:
    days_diff = (datetime.date.today() - last_period).days
    st.info(f"✨ Εβδομάδα {days_diff//7}η + {days_diff%7} ημέρες")

with t3:
    st.number_input("Βάρος (kg):", 40.0, 150.0, 65.0)
    st.multiselect("Συμπτώματα:", ["Ενέργεια ⚡", "Λιγούρες 🍏", "Κούραση 😴"])

with t4:
    st.checkbox("👘 Νυχτικά"); st.checkbox("👶 Φορμάκια"); st.checkbox("🪪 Ταυτότητα")

with t7:
    st.subheader("👣 Kick Counter")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Αισθάνθηκα μια κίνηση ✨"): st.session_state.kicks += 1
    with col2:
        if st.button("Reset 🔄"): st.session_state.kicks = 0
    st.metric("Κινήσεις σήμερα", st.session_state.kicks)

with t8:
    if st.button("📄 Εξαγωγή Αναφοράς"):
        st.write(f"Εβδομάδα: {days_diff//7} | Κινήσεις: {st.session_state.kicks} | Νερό: {st.session_state.water}")

st.write("---")
st.caption("© 2026 MyPregnancyGuide | SOS: 210-XXXXXXX")
