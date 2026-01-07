import streamlit as st
import matplotlib.pyplot as plt

# --- ثوابت المنصة ---
ST_PLATFORM_NAME = "ثوابت"
# ------------------

st.title(f"🌡️ محاكاة بوابة التمدد الحراري - {ST_PLATFORM_NAME}")

# شريط التحكم في درجة الحرارة
temp = st.slider("قم بتغيير درجة الحرارة لمحاكاة التمدد", 20, 50, 25)

target_temp = 35

st.subheader(f"الحرارة الحالية: {temp}°C")

if temp >= target_temp:
    opening_degree = min(90, (temp - target_temp) * 6)
    st.success(f"✅ البوابة مفتوحة بزاوية: {opening_degree} درجة")
    st.info("الشريحة ثنائية المعدن (Bimetallic Strip) في حالة تمدد.")
else:
    st.error("🛑 البوابة مغلقة")
    st.info("درجة الحرارة أقل من 35°C، الشريحة منكمشة.")

# --- قسم التواصل (الثوابت) ---
st.sidebar.markdown(f"### منصة {ST_PLATFORM_NAME}")
st.sidebar.button("واتساب 🟢")
st.sidebar.button("لينكد إن 🔵")
st.sidebar.write("رقم التواصل: [رقمك هنا]")
