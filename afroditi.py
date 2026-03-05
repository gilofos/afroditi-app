import streamlit as st
import datetime
import pandas as pd

# --- ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(
   page_title="Afroditi App",
   page_icon="https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png",
    layout="wide"
)

# --- CUSTOM CSS ΓΙΑ ΜΩΒ/ΡΟΖ STYLE ---
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
.welcome-box { 
    background-color: #ffffff; padding: 30px; border-radius: 25px; 
    border: 2px solid #9c27b0; text-align: center; 
    box-shadow: 0 4px 15px rgba(156, 39, 176, 0.1); margin-bottom: 30px; 
}
.mission-box { 
    background-color: #fdf2f2; padding: 25px; border-radius: 20px; 
    border-left: 10px solid #9c27b0; margin-bottom: 25px; 
    line-height: 1.7; font-size: 16px; color: #333;
}
.card { 
    background-color: white; padding: 25px; border-radius: 20px; 
    border-left: 10px solid #9c27b0; box-shadow: 0 5px 15px rgba(0,0,0,0.05); 
    margin-bottom: 20px; 
}
.link-button {
    display: inline-block; width: 100%; padding: 20px; 
    background: linear-gradient(90deg, #9c27b0, #7b1fa2);
    color: white !important; text-decoration: none; border-radius: 15px;
    font-weight: bold; font-size: 18px; text-align: center;
    margin-bottom: 10px; transition: 0.3s;
}
.link-button:hover { transform: scale(1.02); box-shadow: 0 6px 15px rgba(156, 39, 176, 0.4); }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ΜΕ ΤΟ LOGO ---
with st.sidebar:
    try:
        st.image("logo.png", width=200) 
    except:
        st.info("Εδώ θα εμφανιστεί το logo.png")
    
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input("Τελευταία Περίοδος (LMP):", datetime.date.today())
    st.subheader("💧 Hydration Tracker")
    glasses = st.slider("Ποτήρια νερό σήμερα:", 0, 12, 4)

# --- 1. ΚΑΛΩΣΟΡΙΣΜΑ ---
st.markdown("""
<div class="welcome-box">
    <h1 style="color: #7b1fa2;">🌸 MyPregnancyGuide 🌸</h1>
    <p style="font-size: 19px; color: #555; line-height: 1.6;">
        <b>Το δικό σου ψηφιακό ημερολόγιο εγκυμοσύνης είναι έτοιμο.</b>
    </p>
</div>
""", unsafe_allow_html=True)

# --- 2. Η ΦΙΛΟΣΟΦΙΑ ---
st.markdown("""
<div class="mission-box">
    Το <b>MyPregnancyGuide</b> είναι σχεδιασμένο από την αρχή για την Ελληνίδα έγκυο. 
    Κάθε λέξη, κάθε στάδιο ανάπτυξης και κάθε συμβουλή είναι γραμμένα σωστά και υπεύθυνα. 
    <br><br>
    <b>Ολοκληρωμένη Υποστήριξη:</b> Πέρα από τον υπολογισμό εβδομάδων, προσφέρουμε πρόσβαση σε σεμινάρια για τον τοκετό, 
    τον θηλασμό και τη φροντίδα του νεογνού, προσαρμοσμένα στα δεδομένα της χώρας μας. 
    <br><br>
    <b>Στόχος μας:</b> Να είμαστε ο δικός σας άνθρωπος σε αυτό το υπέροχο ταξίδι. 
    Γιατί η δική σας εγκυμοσύνη αξίζει κάτι παραπάνω.
</div>
""", unsafe_allow_html=True)

if last_period:
    today = datetime.date.today()
    edd = last_period + datetime.timedelta(days=280)
    weeks = (today - last_period).days // 7
    days = (today - last_period).days % 7
    remaining = (edd - today).days

    # --- TABS ---
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🎒 Βαλίτσα", "💖 Ονόματα", "📅 Ραντεβού", "⚙️ Εργαλεία"
    ])

    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"""<div class="card">
                <h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3>
                <p style="font-size:18px;">Μένουν <b>{remaining}</b> ημέρες για τη συνάντηση!</p>
                <p>Πιθανή Ημερομηνία Τοκετού: <b>{edd.strftime('%d/%m/%Y')}</b></p>
            </div>""", unsafe_allow_html=True)
            
            # Δυναμικό μέγεθος φρούτου
            if weeks < 5: fruit = "🌱 Σπόρος παπαρούνας"
            elif weeks < 9: fruit = "🍇 Σταφύλι"
            elif weeks < 13: fruit = "🍋 Λεμόνι"
            elif weeks < 18: fruit = "🍎 Μήλο"
            elif weeks < 23: fruit = "🥭 Μάνγκο"
            elif weeks < 28: fruit = "🍆 Μελιτζάνα"
            elif weeks < 33: fruit = "🍍 Ανανάς"
            elif weeks < 37: fruit = "🍉 Καρπούζι"
            else: fruit = "🎃 Κολοκύθα"
            
            st.info(f"Το μωρό σου έχει το μέγεθος από ένα **{fruit}**!")
            
        with col2:
            st.subheader("🔗 Σεμινάρια")
            st.markdown('<a href="https://www.youtube.com/watch?v=kYI9U8XyW04" target="_blank" class="link-button">🍼 Θηλασμός</a>', unsafe_allow_html=True)
            st.markdown('<a href="https://www.youtube.com/watch?v=rA5S_R3H_94" target="_blank" class="link-button">🧘 Yoga</a>', unsafe_allow_html=True)

    with tab2:
        st.subheader("📸 Η εξέλιξη της κοιλιάς σου")
        st.file_uploader("Ανέβασε τη φωτογραφία της εβδομάδας", type=["jpg","png", "jpeg"])

    with tab3:
        cw1, cw2 = st.columns(2)
        with cw1:
            st.subheader("⚖️ Weight Tracker")
            weight = st.number_input("Βάρος (kg):", 40.0, 150.0, 65.0)
            st.metric("Τρέχον Βάρος", f"{weight} kg")
        with cw2:
            st.subheader("🏥 Εξετάσεις")
            iron = st.number_input("Σίδηρος (Iron):", 0, 300, 110)
            st.bar_chart(pd.DataFrame({'Τιμή': [iron]}, index=['Σίδηρος']))

    with tab4:
        st.subheader("🎒 Checklist Βαλίτσας Μαιευτηρίου")
        st.checkbox("Νυχτικά & Ρόμπα")
        st.checkbox("Φορμάκια & Πάνες")
        st.checkbox("Ταυτότητα & ΑΜΚΑ")

    with tab5:
        st.subheader("💖 Λίστα Ονομάτων")
        if 'names' not in st.session_state: st.session_state.names = []
        new_name = st.text_input("Πρότεινε ένα όνομα:")
        if st.button("Προσθήκη"):
            if new_name: 
                st.session_state.names.append(new_name)
                st.rerun()
        for n in st.session_state.names: st.write(f"✨ {n}")

    with tab6:
        st.subheader("📅 Επόμενα Ραντεβού")
        if 'dates' not in st.session_state: 
            st.session_state.dates = []
        d_input = st.date_input("Ημερομηνία")
        t_input = st.text_input("Εξέταση")
        if st.button("Αποθήκευση Ραντεβού"):
            st.session_state.dates.append(f"{d_input.strftime('%d/%m/%Y')}: {t_input}")
            st.rerun()
        for d in st.session_state.dates: 
            st.write(f"🗓️ {d}")

    with tab7:
        ct1, ct2 = st.columns(2)
        with ct1:
            st.subheader("👣 Kick Counter")
            if 'kicks' not in st.session_state: 
                st.session_state.kicks = 0
            col_k1, col_k2 = st.columns(2)
            with col_k1:
                if st.button("Μόλις κλώτσησε! ✅"): 
                    st.session_state.kicks += 1
            with col_k2:
                if st.button("Reset 🔄"): 
                    st.session_state.kicks = 0
            st.metric("Κινήσεις σήμερα", st.session_state.kicks)
        with ct2:
            st.subheader("⏱️ Συσπάσεις")
            if st.button("Έναρξη Μέτρησης"):
                st.warning(f"Καταγραφή: {datetime.datetime.now().strftime('%H:%M:%S')}")

# --- FOOTER ---
st.write("---")

st.caption("© 2026 MyPregnancyGuide")



