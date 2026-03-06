import streamlit as st
import datetime
import pandas as pd
import random

# --- 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="MyPregnancyGuide Ultra 🌸", page_icon="🤰", layout="wide")

# --- 2. CSS ΓΙΑ ΤΟ ULTRA STYLE ---
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
    .welcome-box { 
        background-color: white; padding: 30px; border-radius: 25px; 
        border: 2px solid #9c27b0; text-align: center; 
        box-shadow: 0 4px 15px rgba(156, 39, 176, 0.1); margin-bottom: 25px; 
    }
    .card { background: white; padding: 20px; border-radius: 20px; border-left: 10px solid #9c27b0; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .link-button {
        display: inline-block; width: 100%; padding: 15px; background: linear-gradient(90deg, #9c27b0, #7b1fa2);
        color: white !important; text-decoration: none; border-radius: 12px;
        font-weight: bold; font-size: 16px; text-align: center; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. STATE ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png", width=180)
    st.error("🆘 ΕΠΑΦΕΣ ΑΝΑΓΚΗΣ")
    st.markdown("**📞 Γιατρός:** 210-XXXXXXX\n\n**📞 Μαία:** 69XXXXXXXX")
    st.write("---")
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    water = st.slider("💧 Ποτήρια νερό σήμερα:", 0, 15, 5)

# --- 5. ΚΥΡΙΩΣ ΠΕΡΙΕΧΟΜΕΝΟ ---
st.markdown(f"""
<div class="welcome-box">
    <h1 style="color: #7b1fa2;">🌸 MyPregnancyGuide Ultra</h1>
    <p style="font-size: 18px; color: #333;">
        Σχεδιασμένο υπεύθυνα για την Ελληνίδα έγκυο.<br>
        <b>Στόχος μας:</b> Να είμαστε ο δικός σας άνθρωπος σε αυτό το υπέροχο ταξίδι.
    </p>
</div>
""", unsafe_allow_html=True)

if last_period:
    today = datetime.date.today()
    edd = last_period + datetime.timedelta(days=280)
    weeks = (today - last_period).days // 7
    days = (today - last_period).days % 7
    remaining = (edd - today).days

    t1, t2, t3, t4, t5, t6 = st.tabs(["📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🥗 Διατροφή", "💖 Ονόματα", "⚙️ Εργαλεία"])

    with t1:
        c1, c2 = st.columns([2,1])
        with c1:
            st.markdown(f"""<div class="card">
                <h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3>
                <p>Μένουν {remaining} ημέρες για τον τοκετό στις {edd.strftime('%d/%m/%Y')}</p>
            </div>""", unsafe_allow_html=True)
            fruit = "🍓 Φράουλα" if weeks < 12 else "🍋 Λεμόνι" if weeks < 20 else "🍌 Μπανάνα"
            st.info(f"Το μωρό σου έχει το μέγεθος από ένα **{fruit}**!")
        with c2:
            st.markdown('<a href="https://youtube.com" class="link-button">🍼 Σεμινάριο Θηλασμού</a>', unsafe_allow_html=True)
            st.markdown('<a href="https://youtube.com" class="link-button">🧘 Yoga Εγκυμοσύνης</a>', unsafe_allow_html=True)

    with t2:
        st.subheader("📸 Φωτογραφία Εβδομάδας")
        st.file_uploader("Ανέβασε τη φωτό σου", type=["jpg", "png"])

    with t3:
        weight = st.number_input("Βάρος (kg):", 40.0, 150.0, 65.0)
        st.metric("Τρέχον Βάρος", f"{weight} kg")

    with t4:
        st.success("🥗 Συμβουλή: Προτίμησε πράσινα φυλλώδη λαχανικά (καλά πλυμένα)!")

    with t5:
        name = st.text_input("Πρόσθεσε όνομα που σου αρέσει:")
        if st.button("Προσθήκη ✨"): st.write(f"Το όνομα '{name}' μπήκε στη λίστα!")

    with t6:
        col_k1, col_k2 = st.columns(2)
        with col_k1:
            if st.button("Κλώτσησε! ✅"): st.session_state.kicks += 1
            st.metric("Κινήσεις σήμερα", st.session_state.kicks)
        with col_k2:
            if st.button("Reset 🔄"): st.session_state.kicks = 0

st.write("---")
st.caption("© 2026 MyPregnancyGuide Ultra | Σταθμός: Ghilofos")
