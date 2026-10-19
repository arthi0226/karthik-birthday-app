
import streamlit as st
from datetime import date

# Page configuration adjustments
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="centered")

# 1. Birthday fixed target initialization configuration
birthday_date = date(2026, 10, 24)  
current_date = date.today()         

# 2. Mathematical countdown calculations
days_left = (birthday_date - current_date).days

# Header Layout Structure
st.markdown("<h1 style='text-align: center; color: #ff4b4b; font-family: Georgia, serif;'>❤️ The Love Capsule ❤️</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #ff4b4b;'>", unsafe_allow_html=True)

if days_left > 0:
    # Pre-birthday Locked View Screen
    st.markdown("<h3 style='text-align: center; color: #555555;'>🔒 This message is securely locked until your special day...</h3>", unsafe_allow_html=True)
    st.info(f"🤫 Shhh! Your special surprise is safely sealed inside this digital time capsule. Come back exactly on your birthday to unlock it!")
    st.metric(label="Countdown to Your Birthday", value=f"{days_left} Days Remaining")
else:
    # Birthday Celebration Unlocked View Screen
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #ff4b4b; animation: pulse 2s infinite;'>🎉 HAPPY BIRTHDAY, MY LOVE! 🎉</h1>", unsafe_allow_html=True)
    
    # The polished corporate romantic letter display block
    st.markdown("""
    <div style='background-color: #fff0f2; padding: 25px; border-radius: 15px; border-left: 5px solid #ff4b4b; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);'>
        <p style='font-size: 18px; font-family: "Lucida Sans", sans-serif; color: #333333; line-height: 1.8;'>
            Happy birthday, my love! ❤️ <br><br>
            You are truly the best person in the entire world, and I love you to the absolute core of my heart. <br><br>
            To be completely honest, when I first saw you, I felt like you were not really my type. But as time went by, you changed everything—and now, you are the only one I ever want in my life. <br><br>
            We have spent three beautiful years together, building a  wonderful memories to cherish for a lifetime. As you turn a year older today, I want you to know that I want to be right by your side for all the rest of your birthdays, spending our entire lives together. <br><br>
            Happy birthday, baby! Yours forever. 😘
        </p>
    </div>
    """, unsafe_allow_html=True)
 
