import streamlit as st
import matplotlib.pyplot as plt

# --- البيانات المستخلصة من ملف السيرة الذاتية ---
NAME = "Mogahed Bashir" [cite: 1]
TITLE = "Mechanical Engineer" [cite: 1]
LOCATION = "Madinah, Saudi Arabia" [cite: 2]
PHONE = "+966 50 131 8054" [cite: 3]
EMAIL = "mog.b.widaa@gmail.com" [cite: 4]
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/" [cite: 5]
PORTFOLIO = "https://mechanical-ai-monitor-pnmzwcurylxwwxzl6aznkn.streamlit.app/" [cite: 6]

# إعدادات الصفحة
st.set_page_config(page_title=f"منصة ثوابت - {NAME}", page_icon="⚙️")

# --- التنسيق الجانبي (Sidebar) ---
st.sidebar.header("منصة ثوابت")
st.sidebar.subheader(NAME) [cite: 1]
st.sidebar.info(f"📍 {LOCATION}") [cite: 2]

# أزرار التواصل الثابتة
st.sidebar.markdown(f"### تواصل معنا")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/{PHONE.replace(' ', '')})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")
st.sidebar.write(f"📞 {PHONE}") [cite: 3]
st.sidebar.write(f"📧 {EMAIL}") [cite: 4]

# --- المحتوى الأساسي للمحاكاة ---
st.title("🌡️ محاكاة بوابة التمدد الحراري الذكية")
st.markdown(f"**إشراف المهندس:** {NAME} ")
st.write("نظام ميكانيكي يعمل ذاتياً بدون طاقة كهربائية، مصمم لفتح بوابات التهوية عند 35°C.")

# لوحة التحكم
st.subheader("لوحة التحكم في درجة الحرارة")
temp = st.slider("درجة الحرارة المحيطة (°C)", 20, 50, 25)

# منطق المحاكاة (Bimetallic Strip Logic)
target_temp = 35


col1, col2 = st.columns(2)

with col1:
    st.metric(label="الحرارة الحالية", value=f"{temp} °C")

with col2:
    if temp >= target_temp:
        # زاوية الفتح تتناسب مع زيادة الحرارة فوق 35
        angle = min(90, (temp - target_temp) * 6)
        st.success(f"حالة البوابة: مفتوحة")
        st.write(f"زاوية الفتح الميكانيكي: {angle}°")
    else:
        st.error("حالة البوابة: مغلقة")
        st.write("السبب: الحرارة دون عتبة التمدد (35°C)")

# ربطها بخلفيتك في الصيانة التنبؤية [cite: 15]
st.divider()
st.subheader("💡 رؤية هندسية")
st.write(f"هذا التصميم يعتمد على مبادئ الهندسة الميكانيكية  التي أطبقها في مشروعي {PORTFOLIO} [cite: 6] لمراقبة المعدات.")

# زر لتحميل التقارير (محاكاة لميزتك في التقارير التلقائية )
if st.button("توليد تقرير تقني (PDF)"):
    st.info("جاري إعداد التقرير بناءً على معايير ISO 10816...") [cite: 16]
