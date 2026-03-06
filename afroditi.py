import streamlit as st
import datetime
import pandas as pd
import random

# --- 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(
    page_title="MyPregnancyGuide Ultra 🌸", 
    page_icon="🤰", 
    layout="wide"
)

# --- 2. CUSTOM CSS (ΜΩΒ/ΡΟΖ STYLE) ---
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
.welcome-box { 
    background-color: #ffffff; padding: 30px; border-radius: 25px; 
    border: 2px solid #9c27b0; text-align: center; 
    box-shadow: 0 4px 15px rgba(156, 39, 176, 0.1); margin-bottom: 30px; 
}
.card { background-color: white; padding: 25px; border-radius: 20px; border-left: 10px solid #9c27b0; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
.link-button {
    display: inline-block; width: 100%; padding: 20px; background: linear-gradient(90deg, #9c27b0, #7b1fa2);
    color: white !important; text-decoration: none; border-radius: 15px;
    font-weight: bold; font-size: 18px; text-align: center;
    margin-bottom: 10px; transition: 0.3s;
}
.link-button:hover { transform: scale(1.02); box-shadow: 0 6px 15px rgba(156, 39, 176, 0.4); }
.custom-text { font-size: 18px; color: #333; line-height: 1.7; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 3. ΔΙΑΤΗΡΗΣΗ ΔΕΔΟΜΕΝΩΝ ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0

# --- 4. SIDEBAR ---
with st.sidebar:
    try:
        st.image("https://raw.githubusercontent.com/gilofos/afroditi-app/main/logo.png", width=200)
    except:
        st.info("Εδώ θα εμφανιστεί το logo.png")
    
    st.error("🆘 ΕΠΑΦΕΣ ΑΝΑΓΚΗΣ")
    st.markdown("**📞 Γιατρός:** 210-XXXXXXX")
    st.markdown("**📞 Μαία:** 69XXXXXXXX")
    st.write("---")
    
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    
    st.subheader("💧 Hydration Tracker")
    st.session_state.water = st.slider("Ποτήρια νερό σήμερα:", 0, 12, st.session_state.water)

# --- 5. ΚΑΛΩΣΟΡΙΣΜΑ ΜΕ ΤΟ ΚΕΙΜΕΝΟ ΣΟΥ ---
st.markdown("""
<div class="welcome-box">
    <h1 style="color: #7b1fa2;">🌸 MyPregnancyGuide Ultra 🌸</h1>
    <div class="custom-text">
        Καλώς ήρθες <b>Αφροδίτη</b>! <br>
        Το <b>MyPregnancyGuide</b> είναι σχεδιασμένο από την αρχή για την Ελληνίδα έγκυο. 
        Κάθε λέξη, κάθε στάδιο ανάπτυξης και κάθε συμβουλή είναι γραμμένα σωστά και υπεύθυνα. 
        <br><br>
        <b>Στόχος μας:</b> Να είμαστε ο δικός σας άνθρωπος σε αυτό το υπέροχο ταξίδι. 
    </div>
</div>
""", unsafe_allow_html=True)

st.success(f"**💡 Συμβουλή:** {random.choice(['Πιες νερό! 💧', 'Περπάτημα στη φύση! 🌿', 'Χαλάρωσε ✨', 'Άκουσε μουσική! 🎵'])}")

if last_period:
    today = datetime.date.today()
    edd = last_period + datetime.timedelta(days=280)
    days_diff = (today - last_period).days
    weeks, days = days_diff // 7, days_diff % 7
    remaining = (edd - today).days

    # ΤΑ 8 TABS (ΣΥΝΔΥΑΣΜΟΣ)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📊 Πρόοδος", "📸 Photo Journal", "🧪 Υγεία", "🍎 Διατροφή", "💖 Ονόματα", "📅 Ραντεβού", "⚙️ Εργαλεία"
    ])

    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"""<div class="card">
                <h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3>
                <p style="font-size:18px;">Μένουν <b>{remaining}</b> ημέρες για τη συνάντηση!</p>
                <p>Πιθανή Ημερομηνία Τοκετού: <b>{edd.strftime('%d/%m/%Y')}</b></p>
            </div>""", unsafe_allow_html=True)
            
            # Μέγεθος φρούτου
            fruit = "🍓 Φράουλα" if weeks < 12 else "🍋 Λεμόνι" if weeks < 20 else "🍌 Μπανάνα"
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
        st.subheader("🥗 Διατροφή")
        st.success("✅ Φρόντισε να τρως μικρά και συχνά γεύματα!")
        st.warning("⚠️ Απόφυγε τα μη παστεριωμένα τυριά.")

    with tab5:
        st.subheader("💖 Λίστα Ονομάτων")
        new_name = st.text_input("Πρόσθεσε όνομα:")
        if st.button("Αποθήκευση"):
            if 'names' not in st.session_state: st.session_state.names = []
            if new_name: st.session_state.names.append(new_name); st.rerun()
        if 'names' in st.session_state:
            for n in st.session_state.names: st.write(f"✨ {n}")

    with tab7:
        ct1, ct2 = st.columns(2)
        with ct1:
            st.subheader("👣 Kick Counter")
            if st.button("Μόλις κλώτσησε! ✅"): st.session_state.kicks += 1
            st.metric("Κινήσεις σήμερα", st.session_state.kicks)
        with ct2:
            st.subheader("⏱️ Συσπάσεις")
            if st.button("Έναρξη Μέτρησης"):
                st.warning(f"Καταγραφή: {datetime.datetime.now().strftime('%H:%M:%S')}")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 MyPregnancyGuide Ultra")
