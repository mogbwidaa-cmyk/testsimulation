import streamlit as st

# --- الثوابت (بيانات المنصة والمهندس) ---
# ملاحظة: تم تنظيف الكود من أي علامات مرجعية لتجنب NameError
NAME = "Mogahed Bashir"
TITLE = "Mechanical Engineer"
LOCATION = "Madinah, Saudi Arabia"
PHONE = "+966501318054"
EMAIL = "mog.b.widaa@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
PLATFORM_NAME = "ثوابت"

# إعدادات الصفحة
st.set_page_config(page_title=f"{PLATFORM_NAME} - {NAME}", page_icon="⚙️")

# --- التنسيق الجانبي (Sidebar) ---
st.sidebar.title(f"منصة {PLATFORM_NAME}")
st.sidebar.markdown(f"**المهندس:** {NAME}")
st.sidebar.markdown("---")
st.sidebar.write(f"📞 {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/{PHONE})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- المحتوى الأساسي ---
st.title("🌡️ محاكاة بوابة التمدد الحراري")
st.write("نظام ميكانيكي يعتمد على الشريحة ثنائية المعدن لفتح التهوية تلقائياً عند 35°C.")

# شريط التحكم بالحرارة
temp = st.slider("عدل درجة الحرارة (°C)", 20, 50, 25)

target_temp = 35

# منطق عمل البوابة
st.subheader("حالة النظام الميكانيكي")
if temp >= target_temp:
    angle = min(90, (temp - target_temp) * 6)
    st.success(f"البوابة: مفتوحة ✅")
    st.info(f"زاوية الفتح الناتجة عن التمدد: {angle} درجة")
    
else:
    st.error("البوابة: مغلقة 🛑")
    st.info("الحرارة أقل من 35°C، القوة الميكانيكية غير كافية للفتح.")

# توضيح هندسي
st.divider()
st.markdown("### 💡 التحليل الهندسي (Mechanical Insight)")
st.write(f"""
عند وصول درجة الحرارة إلى {target_temp}°C، تتولد قوة دفع ميكانيكية نتيجة تمدد الشريحة 
ثنائية المعدن (Bimetallic Strip). هذا التصميم يحاكي أنظمة الصيانة التنبؤية التي 
يعمل عليها المهندس {NAME} لضمان استمرارية العمل دون تدخل بشري.
""")
