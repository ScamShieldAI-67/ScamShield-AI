
import streamlit as st

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #071426, #101e35);
    color: white;
}
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}
h1, h2, h3, p, label {
    color: white !important;
}
.hero {
    background: linear-gradient(120deg, #142c50, #123d70);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #24558a;
    margin-bottom: 25px;
}
.hero h1 {
    font-size: 42px;
}
.hero p {
    color: #b9d7ff !important;
}
.stTextArea textarea {
    background-color: #13243c !important;
    color: white !important;
    border: 1px solid #32649a !important;
    border-radius: 12px !important;
}
.stButton button {
    background: linear-gradient(90deg, #087cf0, #16a5ed);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-weight: bold;
    width: 100%;
}
.info-card {
    background: #142640;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #294665;
    margin: 12px 0;
}
.footer {
    text-align: center;
    color: #91a9c7;
    padding: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🛡️ ScamShield AI</h1>
    <p>Think Before You Click. Let AI Check.</p>
    <p>Your smart companion for online safety.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("🔍 Detect Online Scams")
st.write("Paste a suspicious SMS, email or job offer below.")

message = st.text_area(
    "📩 Enter your message",
    placeholder="Paste your suspicious message here...",
    height=150
)

if st.button("🔍 ANALYSE MESSAGE"):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        text = message.lower()

        scam_words = [
    "won", "winner", "prize", "lottery",
    "urgent", "immediately", "claim now",
    "otp", "password", "bank details",
    "account blocked", "verify account",
    "click here", "limited time",
    "job offer", "registration fee",
    "pay now", "send money",

    # Hindi and Hinglish
    "inaam", "puraskar", "jeet gaye",
    "turant", "khata band", "account band",
    "otp bhejein", "otp batayein",
    "password batayein", "bank ki jankari",
    "paise bhejein", "paisa bhejo",
    "naukri ke liye fees",

    # Hindi script
    "इनाम", "पुरस्कार", "जीत गए",
    "तुरंत", "खाता बंद", "खाता ब्लॉक",
    "ओटीपी", "पासवर्ड", "बैंक विवरण",
    "पैसे भेजें", "भुगतान", "रजिस्ट्रेशन फीस",
    "लिंक पर क्लिक", "सत्यापित करें"
]

        warning_signs = []

        for word in scam_words:
            if word in text:
                warning_signs.append(word)

        # SCAM CATEGORY DETECTION
        categories = {
            "Banking Scam": [
                "bank", "otp", "account blocked",
                "bank details", "credit card"
            ],
            "Fake Job Scam": [
                "job offer", "work from home",
                "registration fee", "salary",
                "hiring", "job vacancy"
            ],
            "Lottery / Prize Scam": [
                "won", "winner", "prize",
                "lottery", "reward"
            ],
            "Phishing Scam": [
                "click here", "verify account",
                "login", "password", "suspended"
            ],
                        "Payment Scam": [
                "pay now", "send money",
                "payment", "transfer money",
                "processing fee"
            ],
            "Fake Delivery Scam": [
                "parcel", "delivery failed",
                "redelivery", "courier",
                "package", "customs fee",
                "delivery charge", "tracking number",
                "delivery fee", "pay to receive"
            ]
        }

        category_scores = {}

        for category, keywords in categories.items():
            score = sum(
                1 for word in keywords if word in text
            )
            category_scores[category] = score

        best_category = max(
            category_scores,
            key=category_scores.get
        )

        if category_scores[best_category] == 0:
            best_category = "Unknown / Other"

        # RISK DETECTION
        if len(warning_signs) >= 3:
            risk = "HIGH RISK"
            st.error("🚨 HIGH RISK - Be very careful!")

        elif len(warning_signs) >= 1:
            risk = "MEDIUM RISK"
            st.warning("⚠️ MEDIUM RISK - Check carefully.")

        else:
            risk = "LOW RISK"
            st.success("✅ LOW RISK - No matching warning words found.")

        st.divider()
        st.header("📊 Analysis Results")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f'<div class="info-card">'
                f'<h3>Risk Level</h3><p>{risk}</p></div>',
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f'<div class="info-card">'
                f'<h3>Scam Category</h3>'
                f'<p>{best_category}</p></div>',
                unsafe_allow_html=True
            )

        st.subheader("🚩 Suspicious Signs")

        if warning_signs:
            for word in warning_signs:
                st.write("🔸 " + word)
        else:
            st.write("No matching warning words were found.")

        st.subheader("🛡️ Safety Recommendations")
        st.write("• Never share your OTP or password.")
        st.write("• Avoid clicking unknown links.")
        st.write("• Verify offers through official sources.")
        st.write("• Never pay unexpected registration fees.")

        st.caption(
            "This is a rule-based assessment, not a guarantee "
            "that a message is safe or fraudulent."
        )

st.divider()

st.subheader("🔐 Stay Protected")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="info-card"><h3>🔑 Privacy</h3>'
        '<p>Never share passwords or OTPs.</p></div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="info-card"><h3>🔗 Safe Links</h3>'
        '<p>Avoid clicking unknown links.</p></div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="info-card"><h3>🛡️ Awareness</h3>'
        '<p>Think before trusting offers.</p></div>',
        unsafe_allow_html=True
    )

st.markdown("""
<div class="footer">
    🛡️ ScamShield AI | Your Digital Safety Companion
    <br>Stay Alert. Stay Protected.
</div>
""", unsafe_allow_html=True)
