import streamlit as st
import datetime
import pandas as pd
import random

# --- ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="MyPregnancyGuide 🌸", page_icon="🌸", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
.welcome-box { background-color: white; padding: 25px; border-radius: 20px; border: 2px solid #9c27b0; text-align: center; box-shadow: 0 4px 12px rgba(156,39,176,0.1); margin-bottom: 25px; }
.card { background-color: white; padding: 20px; border-radius: 18px; border-left: 8px solid #9c27b0; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 18px; }
.link-button { display: inline-block; width: 100%; padding: 15px; background: linear-gradient(90deg, #9c27b0, #7b1fa2); color: white !important; text-decoration: none; border-radius: 12px; font-weight: bold; text-align: center; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0
if 'names' not in st.session_state: st.session_state.names = []
if 'dates' not in st.session_state: st.session_state.dates = []

# --- SIDEBAR ---
with st.sidebar:
    # Χρήση του κανονικού logo από το GitHub σου
    st.image("https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png", width=200)
    
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    
    st.subheader("💧 Ενυδάτωση")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        if st.button("🥛 Ήπια!"): st.session_state.water += 1
    with col_w2:
        if st.button("🔄 Μηδενισμός"): st.session_state.water = 0
    st.write(f"**Σύνολο:** {st.session_state.water} ποτήρια")

# --- ΚΑΛΩΣΟΡΙΣΜΑ & ΚΟΜΨΟ ΑΝΙΜΑΤΙΟΝ ---
st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
col_anim, col_txt = st.columns([1, 4])
with col_anim:
    # Κομψό animation καρδιάς (όχι παιδικό)
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

    # --- TABS ΜΕ ΟΛΟ ΤΟ ΠΕΡΙΕΧΟΜΕΝΟ ---
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🎒 Βαλίτσα", "💖 Ονόματα", "📅 Ραντεβού", "⚙️ Εργαλεία", "📋 Αναφορά"
    ])

    with tab1: # ΠΡΟΟΔΟΣ
        col_f1, col_f2 = st.columns([2, 1])
        with col_f1:
            st.markdown(f"""<div class="card">
                <h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3>
                <p style="font-size:18px;">Μένουν <b>{remaining}</b> ημέρες για τη συνάντηση!</p>
                <p>Πιθανή Ημερομηνία Τοκετού: <b>{edd.strftime('%d/%m/%Y')}</b></p>
            </div>""", unsafe_allow_html=True)
            
            if weeks < 13: fruit = "🍋 Λεμόνι"
            elif weeks < 28: fruit = "🍎 Μήλο"
            else: fruit = "🍉 Καρπούζι"
            st.info(f"Το μωρό σου έχει το μέγεθος από ένα **{fruit}**!")
        with col_f2:
            st.subheader("🔗 Σεμινάρια")
            st.markdown('<a href="https://www.youtube.com/watch?v=kYI9U8XyW04" target="_blank" class="link-button">🍼 Θηλασμός</a>', unsafe_allow_html=True)

    with tab2: # JOURNAL
        st.subheader("📸 Η εξέλιξη της κοιλιάς σου")
        st.file_uploader("Ανέβασε τη φωτογραφία της εβδομάδας", type=["jpg","png", "jpeg"])

    with tab3: # ΥΓΕΙΑ
        st.subheader("🧪 Μετρήσεις & Συμπτώματα")
        weight = st.number_input("Βάρος (kg):", 40.0, 150.0, 65.0)
        st.multiselect("Πώς νιώθεις σήμερα;", ["Ενέργεια ⚡", "Λιγούρες 🍏", "Κούραση 😴", "Ηρεμία 🧘"])

    with tab4: # ΒΑΛΙΤΣΑ
        st.subheader("🎒 Checklist Βαλίτσας Μαιευτηρίου")
        st.checkbox("
