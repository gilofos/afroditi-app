import streamlit as st
import datetime
import pandas as pd
import random
import requests
from streamlit_lottie import st_lottie

# --- ΣΥΝΑΡΤΗΣΗ ΓΙΑ ANIMATIONS (Lottie) ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- ΦΟΡΤΩΣΗ ANIMATIONS (Lottie URLs) ---
# 1. Animation για το Καλωσόρισμα (Μωράκι)
lottie_welcome = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_m6cu96p6.json")
# 2. Animation για το Tab "Υγεία" (Καρδιά που χτυπάει)
lottie_health = load_lottieurl("https://assets.lottiefiles.com/packages/lf20_4wz85t4b.json")
# 3. Animation για το Tab "Εργαλεία" (Πατουσάκια)
lottie_tools = load_lottieurl("https://assets.lottiefiles.com/packages/lf20_at4w5n3q.json")

# --- ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(
   page_title="MyPregnancyGuide 🌸",
   page_icon="https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png",
   layout="wide"
)

# --- CUSTOM CSS ΓΙΑ ΜΩΒ/ΡΟΖ STYLE ---
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
.welcome-box { 
    background-color: #ffffff; padding: 25px; border-radius: 20px; 
    border: 2px solid #9c27b0; text-align: center; 
    box-shadow: 0 4px 12px rgba(156, 39, 176, 0.1); margin-bottom: 25px; 
}
.mission-box { 
    background-color: #fdf2f2; padding: 20px; border-radius: 18px; 
    border-left: 8px solid #9c27b0; margin-bottom: 20px; 
    line-height: 1.6; font-size: 15px; color: #333;
}
.card { 
    background-color: white; padding: 20px; border-radius: 18px; 
    border-left: 8px solid #9c27b0; box-shadow: 0 4px 10px rgba(0,0,0,0.05); 
    margin-bottom: 18px; 
}
.link-button {
    display: inline-block; width: 100%; padding: 18px; 
    background: linear-gradient(90deg, #9c27b0, #7b1fa2);
    color: white !important; text-decoration: none; border-radius: 12px;
    font-weight: bold; font-size: 17px; text-align: center;
    margin-bottom: 8px; transition: 0.3s;
}
.link-button:hover { transform: scale(1.02); box-shadow: 0 5px 12px rgba(156, 39, 176, 0.3); }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0

# --- SIDEBAR (Με SOS Επαφές) ---
with st.sidebar:
    try:
        st.image("logo.png", width=200) 
    except:
        st.info("🌸 MyPregnancyGuide")
    
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input(
        "📅 Τελευταία Περίοδος (LMP):", 
        datetime.date(2025, 10, 1)
    )
    
    st.subheader("💧 Ενυδάτωση")
    c_w1, c_w2 = st.columns([1, 2])
    with c_w1:
        if st.button("🥛 Ήπια!"): st.session_state.water += 1
    with c_w2:
        st.write(f"**Σύνολο:** {st.session_state.water} ποτήρια")
    
    st.error("🆘 SOS Επαφές")
    doctor_phone = st.text_input("📞 Γιατρός:", "210-XXXXXXX")
    midwife_phone = st.text_input("📞 Μαία:", "69XXXXXXXX")

# --- 1. ΚΑΛΩΣΟΡΙΣΜΑ & ANIMATION ---
st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
col_lottie, col_text = st.columns([1, 3])
with col_lottie:
    if lottie_welcome: st_lottie(lottie_welcome, height=130, key="baby_welcome")
with col_text:
    st.markdown('<h1 style="color: #7b1fa2;">🌸 MyPregnancyGuide 🌸</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 18px; color: #555;"><b>Το δικό σου ψηφιακό ημερολόγιο εγκυμοσύνης.</b></p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 2. ΣΥΜΒΟΥΛΗ ΤΗΣ ΗΜΕΡΑΣ ---
tips = [
    "Πιες ένα φρέσκο χυμό πορτοκάλι! 🍊",
    "Άκουσε κλασική μουσική και χαλάρωσε. 🎵",
    "Λίγο περπάτημα στη φύση κάνει καλό! 🌿",
    "Μην ξεχνάς τις βιταμίνες σου σήμερα. 💊",
    "Κάνε ένα χλιαρό μπάνιο για χαλάρωση. 🛁",
    "Ονειρέψου το μέλλον με το μωράκι σου! ✨"
]
st.success(f"**💡 Συμβουλή:** {random.choice(tips)}")

# --- ΥΠΟΛΟΓΙΣΜΟΙ ΕΒΔΟΜΑΔΩΝ ---
if last_period:
    today = datetime.date.today()
    edd = last_period + datetime.timedelta(days=280)
    weeks = (today - last_period).days // 7
    days = (today - last_period).days % 7
    remaining = (edd - today).days

    # --- ΤΟ ΜΩΡΟ ΜΟΥ ΑΥΤΗ ΤΗΝ ΕΒΔΟΜΑΔΑ (Smart Info) ---
    if weeks < 5: baby_info = "🌱 Το μωράκι σου είναι ένας σπόρος παπαρούνας!"
    elif weeks < 13: baby_info = "👶 Τα όργανά του αρχίζουν να σχηματίζονται!"
    elif weeks < 20: baby_info = "✨ Αναπτύσσει τις αισθήσεις του και κουνιέται!"
    elif weeks < 28: baby_info = "💖 Ανοίγει τα μάτια του και ακούει τη φωνή σου!"
    elif weeks < 36: baby_info = "🍉 Παίρνει βάρος και ετοιμάζεται για τον κόσμο!"
    else: baby_info = "🎃 Είναι έτοιμο να σε συναντήσει!"
    
    st.info(f"**ℹ️ Εβδομάδα {weeks}:** {baby_info}")

    # --- TABS (Με Εικονίδια) ---
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🎒 Βαλίτσα", "💖 Ονόματα", "📅 Ραντεβού", "⚙️ Εργαλεία", "📋 Αναφορά"
    ])

    # Tab 1: Πρόοδος
    with tab1:
        st.markdown(f"""<div class="card">
            <h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3>
            <p style="font-size:18px;">📅 Πιθανή Ημερομηνία Τοκετού: <b>{edd.strftime('%d/%m/%Y')}</b></p>
            <p>⏳ Μένουν <b>{remaining}</b> ημέρες για τη συνάντηση!</p>
        </div>""", unsafe_allow_html=True)

    # Tab 3: Υγεία (Με Animation & Συμπτώματα)
    with tab3:
        st.subheader("🧪 Μετρήσεις & Διάθεση")
        col_lottie_h, col_content_h = st.columns([1, 2])
        with col_lottie_h:
            if lottie_health: st_lottie(lottie_health, height=130, key="heart_health")
        with col_content_h:
            weight = st.number_input("⚖️ Βάρος (kg):", 40.0, 150.0, 65.0)
            symptoms = st.multiselect(
                "😊 Πώς νιώθεις σήμερα;",
                ["Πολλή ενέργεια ⚡", "Λιγούρες 🍏", "Κούραση 😴", "Ηρεμία 🧘", "Ανυπομονησία ✨"]
            )

    # Tab 7: Εργαλεία (Με Animation & Κινήσεις)
    with tab7:
        st.subheader("⚙️ Χρήσιμα Εργαλεία")
        col_lottie_t, col_content_t = st.columns([1, 2])
        with col_lottie_t:
            if lottie_tools: st_lottie(lottie_tools, height=130, key="feet_tools")
        with col_content_t:
            st.markdown("<h3>👣 Καταγραφή Δραστηριότητας</h3>", unsafe_allow_html=True)
            col_k1, col_k2 = st.columns(2)
            with col_k1:
                if st.button("Αισθάνθηκα μια κίνηση ✨"): st.session_state.kicks += 1
            with col_k2:
                if st.button("Μηδενισμός 🔄"): st.session_state.kicks = 0
            st.metric("Σύνολο κινήσεων σήμερα", st.session_state.kicks)

    # (Οι υπόλοιπες καρτέλες Journal, Βαλίτσα κλπ παραμένουν ως είχαν στον κώδικά σου)
    # Προσθήκη εικονιδίων στις υπόλοιπες για ομοιομορφία
    with tab4:
        st.subheader("🎒 Checklist Βαλίτσας Μαιευτηρίου")
        st.checkbox("👘 Νυχτικά & Ρόμπα")
        st.checkbox("👶 Φορμάκια & Πάνες")
        st.checkbox("🪪 Ταυτότητα & ΑΜΚΑ")

    with tab8:
        st.subheader("📋 Αναφορά για τον Γιατρό")
        if st.button("Προβολή Αναφοράς 📄"):
            st.success(f"Η αναφορά δημιουργήθηκε επιτυχώς!")
            st.markdown(f"""
            <div style="background-color: white; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                <h3 style="color: #7b1fa2; text-align: center;">ΑΝΑΦΟΡΑ ΕΓΚΥΜΟΣΥΝΗΣ</h3>
                <hr>
                <p><b>Στάδιο:</b> Εβδομάδα {weeks}η + {days} ημέρες</p>
                <p><b>👣 Κινήσεις σήμερα:</b> {st.session_state.kicks}</p>
                <p><b>💧 Νερό:</b> {st.session_state.water} ποτήρια</p>
                <p><b>📞 SOS Γιατρός:</b> {doctor_phone}</p>
            </div>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 MyPregnancyGuide | Σχεδιασμένο για την Ελληνίδα έγκυο | Ready for the Store")
