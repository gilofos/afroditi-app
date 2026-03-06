import streamlit as st
import datetime
import random

# --- 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="MyPregnancyGuide🌸", layout="wide")

# --- 2. CSS ΣΤΥΛ ---
st.markdown("""<style>
    .stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
    .welcome-box { background: white; padding: 30px; border-radius: 20px; border: 2px solid #9c27b0; text-align: center; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(156,39,176,0.1); }
    .card { background: white; padding: 15px; border-radius: 15px; border-left: 8px solid #9c27b0; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    h1 { color: #7b1fa2; font-size: 32px; margin-bottom: 15px; }
    .custom-text { font-size: 18px; color: #333; line-height: 1.7; text-align: center; }
</style>""", unsafe_allow_html=True)

# --- 3. ΔΙΑΤΗΡΗΣΗ ΔΕΔΟΜΕΝΩΝ ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0

# --- 4. SIDEBAR (ΓΙΑΤΡΟΣ, ΜΑΙΑ, ΡΥΘΜΙΣΕΙΣ, ΝΕΡΟ) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png", width=180)
    
    st.error("🆘 ΕΠΑΦΕΣ ΑΝΑΓΚΗΣ")
    st.markdown("**📞 Γιατρός:** 210-XXXXXXX")
    st.markdown("**📞 Μαία:** 69XXXXXXXX")
    st.markdown("---")
    
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    
    st.subheader("💧 Hydration Tracker")
    c_w1, c_w2 = st.columns(2)
    with c_w1:
        if st.button("🥛 Ήπια!"): st.session_state.water += 1
    with c_w2:
        if st.button("🔄 Reset"): st.session_state.water = 0
    st.write(f"**Σύνολο:** {st.session_state.water} ποτήρια")

# --- 5. ΚΥΡΙΩΣ ΟΘΟΝΗ ΜΕ ΤΟ ΚΕΙΜΕΝΟ ΣΟΥ ---
st.markdown(f"""
<div class="welcome-box">
    <h1>🌸 MyPregnancyGuide</h1>
    <div class="custom-text">
        Το <b>MyPregnancyGuide</b> είναι σχεδιασμένο από την αρχή για την Ελληνίδα έγκυο. 
        Κάθε λέξη, κάθε στάδιο ανάπτυξης και κάθε συμβουλή είναι γραμμένα σωστά και υπεύθυνα. 
        <br><br>
        <b>Ολοκληρωμένη Υποστήριξη:</b> Πέρα από τον υπολογισμό εβδομάδων, προσφέρουμε πρόσβαση σε σεμινάρια 
        για τον τοκετό, τον θηλασμό και τη φροντίδα του νεογνού, προσαρμοσμένα στα δεδομένα της χώρας μας. 
        <br><br>
        <b>Στόχος μας:</b> Να είμαστε ο δικός σας άνθρωπος σε αυτό το υπέροχο ταξίδι. 
        Γιατί η δική σας εγκυμοσύνη αξίζει κάτι παραπάνω.
    </div>
</div>
""", unsafe_allow_html=True)

st.success(f"**💡 Συμβουλή:** {random.choice(['Πιες νερό! 💧', 'Περπάτημα στη φύση! 🌿', 'Χαλάρωσε ✨', 'Άκουσε μουσική! 🎵'])}")

if last_period:
    days_diff = (datetime.date.today() - last_period).days
    weeks, days = days_diff // 7, days_diff % 7
    edd = last_period + datetime.timedelta(days=280)

    # ΤΑ 8 TABS
    t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs([
        "📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🎒 Βαλίτσα", 
        "💖 Ονόματα", "📅 Ραντεβού", "⚙️ Εργαλεία", "📋 Αναφορά"
    ])

    with t1:
        st.markdown(f'<div class="card"><h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3><p>Πιθανή Ημερομηνία Τοκετού: {edd.strftime("%d/%m/%Y")}</p></div>', unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("🎓 Premium Σεμινάρια & Yoga")
        # ΠΡΟΣΘΗΚΗ ΚΩΔΙΚΟΥ (ΠΛΗΡΩΜΗ)
        access_code = st.text_input("Εισάγετε τον κωδικό πρόσβασης για τα σεμινάρια:", type="password")
        if access_code == "1234":
            st.success("Η πρόσβαση ξεκλειδώθηκε!")
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                st.video("https://www.youtube.com/watch?v=kYI9U8XyW04")
                st.caption("🍼 Σεμινάριο Θηλασμού")
            with col_s2:
                st.video("https://www.youtube.com/watch?v=rA5S_R3H_94")
                st.caption("🧘 Yoga για την Εγκυμοσύνη")
        elif access_code != "":
            st.error("Λάθος κωδικός. Επικοινωνήστε με τη μαία σας για την πληρωμή.")

    with t2:
        st.subheader("📸 Φωτογραφία Εβδομάδας")
        st.file_uploader("Ανέβασε τη φωτογραφία σου", type=["jpg", "png"])

    with t3:
        st.subheader("🧪 Μετρήσεις & Συμπτώματα")
        st.number_input("Βάρος (kg):", 40.0, 150.0, 65.0)
        st.multiselect("Πώς νιώθεις σήμερα;", ["Ενέργεια ⚡", "Λιγούρες 🍏", "Κούραση 😴", "Ηρεμία 🧘"])

    with t4:
        st.subheader("🎒 Checklist Βαλίτσας")
        st.checkbox("👘 Νυχτικά & Ρόμπα"); st.checkbox("👶 Φορμάκια & Πάνες"); st.checkbox("🪪 Ταυτότητα & ΑΜΚΑ")

    with t5:
        st.subheader("💖 Λίστα Ονομάτων")
        new_name = st.text_input("Πρόσθεσε όνομα:")
        if st.button("Αποθήκευση"):
            if 'names' not in st.session_state: st.session_state.names = []
            if new_name: st.session_state.names.append(new_name); st.rerun()
        if 'names' in st.session_state:
            for n in st.session_state.names: st.write(f"✨ {n}")

    with t6:
        st.subheader("📅 Επόμενα Ραντεβού")
        st.date_input("Ημερομηνία Εξέτασης")
        st.text_input("Τύπος Εξέτασης")

    with t7:
        st.subheader("⚙️ Εργαλεία Καταγραφής")
        col_k1, col_k2 = st.columns(2)
        with col_k1:
            if st.button("Αισθάνθηκα μια κίνηση ✨"): st.session_state.kicks += 1
            st.metric("Κινήσεις σήμερα", st.session_state.kicks)
        with col_k2:
            if st.button("Reset Κινήσεων 🔄"): st.session_state.kicks = 0
            st.button("Έναρξη Συσπάσεων ⏱️")

    with t8:
        st.subheader("📋 Αναφορά")
        if st.button("📊 Εξαγωγή Δεδομένων"):
            st.info(f"Στάδιο: {weeks}βδ | Κινήσεις: {st.session_state.kicks} | Νερό: {st.session_state.water}")

st.write("---")
st.caption("© 2026 MyPregnancyGuide | Ghilofos Station")
