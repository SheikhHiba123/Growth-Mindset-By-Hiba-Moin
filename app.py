import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="📘")

# Title and Intro
st.title("📘 Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Every step forward counts. Embrace effort, learn from experience, and believe in your ability to grow. This AI-powered app supports your mindset journey through challenges, reflection, and accomplishments! 🌟")

# Quote of the Day
st.header("💡 Daily Dose of Wisdom")
st.write("💬 *“Success is not final, failure is not fatal: it is the courage to continue that counts.”* — Winston Churchill")

# Challenge Section
st.header("🎯 What's Your Challenge Today?")
user_input = st.text_input("🌟 Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You are facing: **{user_input}** — That’s the first step! Keep moving forward. 🚀")
else:
    st.warning("📝 Please share a challenge to start your growth journey.")

# Reflection Section
st.header("🪞 Reflect on Your Learning")
reflection = st.text_area("💭 Share what you've learned or felt recently:")

if reflection:
    st.success(f"🧩 Insight recorded: **{reflection}** — Growth comes from awareness.")
else:
    st.info("✨ Reflection fuels progress. Take a moment to look back and learn.")

# Achievement Section
st.header("🏅 Celebrate Your Wins")
achievement = st.text_input("🎉 Share something you've recently accomplished:")

if achievement:
    st.success(f"🌈 Achievement unlocked: **{achievement}** — Be proud, you’ve earned it!")
else:
    st.info("🙌 No win is too small. Share something you’re proud of!")

# Footer
st.markdown("---")
st.markdown("🌟 *Growth takes time. Keep watering your mindset every day.*")
st.markdown('<div style="text-align: center; font-weight: bold;">🔧 Developed by Hiba Moin</div>', unsafe_allow_html=True)
