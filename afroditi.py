import streamlit as st
import datetime
import pandas as pd
import random

# --- 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ ---
st.set_page_config(
    page_title="MyPregnancyGuide 🌸",
    page_icon="🌸",
    layout="wide"
)

# --- 2. CUSTOM CSS ΓΙΑ ΜΩΒ/ΡΟΖ STYLE ---
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #f3e5f5 0%, #ffffff 100%); }
.welcome-box { 
    background-color: #ffffff; padding: 25px; border-radius: 20px; 
    border: 2px solid #9c27b0; text-align: center; 
    box-shadow: 0 4px 12px rgba(156, 39, 176, 0.1); margin-bottom: 25px; 
}
.card { 
    background-color: white; padding: 20px; border-radius: 18px; 
    border-left: 8px solid #9c27b0; box-shadow: 0 4px 10px rgba(0,0,0,0.05); 
    margin-bottom: 18px; 
}
</style>
""", unsafe_allow_html=True)

# --- 3. INITIALIZE SESSION STATE ---
if 'kicks' not in st.session_state: st.session_state.kicks = 0
if 'water' not in st.session_state: st.session_state.water = 0

# --- 4. SIDEBAR (Ρυθμίσεις & SOS) ---
with st.sidebar:
    st.header("📍 Ρυθμίσεις")
    last_period = st.date_input("📅 Τελευταία Περίοδος (LMP):", datetime.date(2025, 10, 1))
    
    st.subheader("💧 Ενυδάτωση")
    if st.button("🥛 Ήπια ένα ποτήρι!"):
        st.session_state.water += 1
    st.write(f"**Σύνολο:** {st.session_state.water} ποτήρια")
    
    st.error("🆘 SOS Επαφές")
    st.write("📞 Γιατρός: 210-XXXXXXX")
    st.write("📞 Μαία: 69XXXXXXXX")

# --- 5. ΚΑΛΩΣΟΡΙΣΜΑ ΜΕ ΚΙΝΗΣΗ (Animation χωρίς βιβλιοθήκη) ---
st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
col_anim, col_txt = st.columns([1, 3])
with col_anim:
    # Εισαγωγή κίνησης μέσω HTML για να αποφύγουμε τα ModuleErrors
    st.markdown('<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXF3bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1z/3o7TKVUn7iM8FMEU24/giphy.gif" width="120">', unsafe_allow_html=True)
with col_txt:
    st.markdown('<h1 style="color: #7b1fa2;">🌸 MyPregnancyGuide</h1>', unsafe_allow_html=True)
    st.write("Το δικό σου ψηφιακό ημερολόγιο εγκυμοσύνης.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. ΣΥΜΒΟΥΛΗ ΤΗΣ ΗΜΕΡΑΣ ---
tips = [
    "Πιες ένα φρέσκο χυμό πορτοκάλι! 🍊",
    "Άκουσε την αγαπημένη σου μουσική και χαλάρωσε. 🎵",
    "Λίγο περπάτημα στη φύση κάνει καλό! 🌿",
    "Σήμερα είναι μια υπέροχη μέρα για όνειρα! ✨"
]
st.success(f"**💡 Συμβουλή:** {random.choice(tips)}")

# --- 7. ΚΥΡΙΩΣ ΠΕΡΙΕΧΟΜΕΝΟ ---
if last_period:
    today = datetime.date.today()
    weeks = (today - last_period).days // 7
    days = (today - last_period).days % 7
    edd = last_period + datetime.timedelta(days=280)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📊 Πρόοδος", "📸 Journal", "🧪 Υγεία", "🎒 Βαλίτσα", "💖 Ονόματα", "📅 Ραντεβού", "⚙️ Εργαλεία", "📋 Αναφορά"
    ])

    with tab1:
        st.markdown(f"""<div class="card">
            <h3>📈 Εβδομάδα {weeks}η + {days} ημέρες</h3>
            <p>Πιθανή Ημερομηνία Τοκετού: <b>{edd.strftime('%d/%m/%Y')}</b></p>
        </div>""", unsafe_allow_html=True)

    with tab3: # ΥΓΕΙΑ & ΣΥΜΠΤΩΜΑΤΑ
        st.subheader("🧪 Πώς νιώθεις σήμερα;")
        st.multiselect("Επίλεξε κατάσταση:", ["Ενέργεια ⚡", "Λιγούρες 🍏", "Κούραση 😴", "Ηρεμία 🧘"])
        # Animation υγείας
        st.markdown('<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExemZ6ZzR0bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0bmZ6ZzR0JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1z/3o7TKVUn7iM8FMEU24/giphy.gif" width="80">', unsafe_allow_html=True)

    with tab7: # ΕΡΓΑΛΕΙΑ & ΚΙΝΗΣΕΙΣ
        st.subheader("👣 Καταγραφή Δραστηριότητας")
        col_k1, col_k2 = st.columns(2)
        with col_k1:
            if st.button("Αισθάνθηκα μια κίνηση ✨"):
                st.session_state.kicks += 1
        with col_k2:
            if st.button("Μηδενισμός 🔄"):
                st.session_state.kicks = 0
        st.metric("Κινήσεις σήμερα", st.session_state.kicks)

# --- 8. FOOTER ---
st.write("---")
st.caption("© 2026 MyPregnancyGuide | Σχεδιασμένο για την Ελληνίδα έγκυο")
