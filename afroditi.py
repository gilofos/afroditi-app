import streamlit as st
import datetime
import pandas as pd
import random

# --- 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="MyPregnancyGuide 🌸", page_icon="🌸", layout="wide")

# --- 2. CUSTOM CSS ---
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
.welcome-box { background-color: white; padding: 25px; border-radius: 20px; border: 2px solid #9c27b0; text-align: center; box-shadow: 0 4px 12px rgba(156,39,176,0.1); margin-bottom: 25px; }
.card { background-color: white; padding: 20px; border-radius: 18px; border-left: 8px solid #9c27b0; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 18px; }
.link-button { display: inline-block; width: 100%; padding: 15px; background: linear-gradient(90deg, #9c27b0, #7b1fa2); color: white !important; text-decoration: none; border-radius: 12px; font-weight: bold; text-align: center; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

# --- 3. INITIALIZE SESSION STATE ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0
if 'names' not in st.session_state: st.session_state.names = []
if 'dates' not in st.session_state: st.session_state.dates = []

# --- 4. SIDEBAR ---
with st.sidebar:
    # Σωστό Logo από το GitHub
    st.image("https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png", width=200)
    
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    
    st.subheader("💧 Ενυδάτωση")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        if st.button("🥛 Ήπια!"): st.session_state.water += 1
    with col_w2:
        # Διόρθωση: Κουμπί για μηδενισμό ποτηριών
        if st.button("🔄 Μηδενισμός"): st.session_state.water = 0
    st.write(f"**Σήμερα:** {st.session_state.water} ποτήρια")

# --- 5. ΚΑΛΩΣΟΡΙΣΜΑ ---
st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
col_anim, col_txt = st.columns([1, 4])
with col_anim:
    # Διακριτικό animation καρδιάς αντί για Simpson
    st.markdown('<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXF3bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1z/3o7TKVUn7iM8FMEU24/giphy.gif" width="100">', unsafe_allow_html=True)
with col_txt:
    st.markdown('<h1 style="color: #7b1fa2;">🌸 MyPregnancyGuide</h1>', unsafe_allow_html=True)
    st.write("Το δικό σου ψηφιακό ημερολόγιο εγκυμοσύνης.")
st.markdown('</div>', unsafe_allow_html=True)

if last_period:
    today = datetime.date.today()
    edd = last_period + datetime.timedelta(days=280)
    weeks = (today - last_period).days // 7
    days = (today - last_period).days % 7
    remaining = (edd - today).days

    # Συμβουλή Ημέρας
    tips = ["Πιες νερό! 💧", "Περπάτημα στη φύση! 🌿", "Άκουσε μουσική! 🎵", "Χαλάρωσε ✨"]
    st.success(f"**💡 Συμβουλή:** {random.choice(tips)}")

    # --- 6. TABS ΜΕ ΟΛΟ ΤΟ ΠΕΡΙΕΧΟΜΕΝΟ ---
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🎒
