import streamlit as st
import datetime
import pandas as pd

# --- ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(
   page_title="MyPregnancyGuide Ultra", 
   page_icon="🤰", 
   layout="wide"
)

# --- CUSTOM CSS ---
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
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ΜΕ ΤΟ LOGO ---
with st.sidebar:
    try:
        st.image("logo.png", width=200) 
    except:
        st.info("Εδώ θα εμφανιστεί το logo.png")
    
    st.header("📍 Ρυθμίσεις")
    # Η ΓΡΑΜΜΗ ΑΠΟ ΤΟ BACKUP ΠΟΥ ΛΥΝΕΙ ΤΟ ΗΜΕΡΟΛΟΓΙΟ
    last_period = st.date_input("Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    
    st.write("---")
    st.subheader("💧 Hydration Tracker")
    glasses = st.slider("Ποτήρια νερό σήμερα:", 0, 12, 4)

# --- 1. ΚΑΛΩΣΟΡΙΣΜΑ ---
st.markdown("""
<div class="welcome-box">
    <h1 style="color: #7b1fa2;">🌸 MyPregnancyGuide Ultra 🌸</h1>
    <p style="font-size: 19px; color: #555; line-height: 1.6;">
        Καλώς ήρθες Αφροδίτη! <br>
        <b>Το δικό σου ψηφιακό ημερολόγιο εγκυμοσύνης είναι έτοιμο.</b>
    </p>
</div>
""", unsafe_allow_html=True)

if last_period:
    today = datetime.date.today()
    edd = last_period + datetime.timedelta(days=280)
    weeks = (today - last_period).days // 7
    days = (today - last_period).days % 7
    remaining = (edd - today).days

    # ΠΡΟΣΘΗΚΗ ΤΑΒ ΓΙΑ ΑΝΑΦΟΡΑ
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📊 Πρόοδος", "📸 Photo Journal", "🧪 Υγεία", "🍎 Διατροφή", "⚙️ Εργαλεία", "📋 Αναφορά για Γιατρό"
    ])

    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"""<div class="card">
                <h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3>
                <p style="font-size:18px;">Μένουν <b>{remaining}</b> ημέρες για τη συνάντηση!</p>
                <p>Πιθανή Ημερομηνία Τοκετού: <b>{edd.strftime('%d/%m/%Y')}</b></p>
            </div>""", unsafe_allow_html=True)
            
            # Φρούτο
            if weeks < 5: fruit = "🌱 Σπόρος παπαρούνας"
            elif weeks < 12: fruit = "🍓 Φράουλα"
            elif weeks < 20: fruit = "🍋 Λεμόνι"
            elif weeks < 30: fruit = "🍌 Μπανάνα"
            else: fruit = "🍉 Καρπούζι"
            st.info(f"Το μωρό σου έχει το μέγεθος από ένα **{fruit}**!")

        with col2:
            st.subheader("🔗 Σεμινάρια")
            st.markdown('<a href="https://www.youtube.com/watch?v=kYI9U8XyW04" target="_blank" class="link-button">🍼 Θηλασμός</a>', unsafe_allow_html=True)
            st.markdown('<a href="https://www.youtube.com/watch?v=rA5S_R3H_94" target="_blank" class="link-button">🧘 Yoga</a>', unsafe_allow_html=True)

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

    with tab6:
        # Η ΝΕΑ ΣΕΛΙΔΑ ΑΝΑΦΟΡΑΣ
        st.subheader("📋 Στοιχεία για τον Γιατρό")
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border: 2px solid #9c27b0; border-radius: 15px;">
            <h3 style="color: #7b1fa2; text-align: center;">ΑΝΑΦΟΡΑ ΕΓΚΥΜΟΣΥΝΗΣ</h3>
            <p><b>Ημερομηνία Αναφοράς:</b> {datetime.date.today().strftime('%d/%m/%Y')}</p>
            <hr>
            <p><b>Στάδιο:</b> Εβδομάδα {weeks}η + {days} ημέρες</p>
            <p><b>Πιθανή Ημ/νία Τοκετού:</b> {edd.strftime('%d/%m/%Y')}</p>
            <p><b>Βάρος:</b> {weight} kg</p>
            <p><b>Σίδηρος:</b> {iron}</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 MyPregnancyGuide Ultra")
