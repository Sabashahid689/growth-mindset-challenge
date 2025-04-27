import streamlit as st
import random
from datetime import date

# Title and Header
st.title("🌱 Growth Mindset Challenge")
st.markdown("Boost your mindset one challenge at a time!")

# List of Challenges
challenges = [
    "Write down 3 things you learned today.",
    "Do something outside your comfort zone.",
    "Ask someone for feedback and reflect on it.",
    "Turn a recent mistake into a learning moment.",
    "Compliment someone’s effort instead of their result.",
    "Try a new strategy for something that’s not working.",
    "Read or watch something that inspires you.",
    "Teach someone something new today.",
    "Reframe a negative thought into a growth opportunity.",
    "Celebrate small wins today."
]

# List of Affirmations
affirmations = [
    "I am capable of growth and change.",
    "Challenges help me grow.",
    "My effort today creates my future.",
    "I learn from feedback and use it to improve.",
    "I am not afraid to make mistakes.",
    "Every day is a chance to improve.",
    "I believe in my ability to learn new things."
]

# Today's challenge & affirmation (consistent per day)
today = date.today()
random.seed(str(today))  # Seed by date for consistency

daily_challenge = random.choice(challenges)
daily_affirmation = random.choice(affirmations)

# Display Challenge
st.header("📝 Today's Challenge")
st.write(f"{daily_challenge}")

# Display Affirmation
st.header("💬 Today's Affirmation")
st.success(f"💡 {daily_affirmation}")

# Optional Progress Tracker
if "completed" not in st.session_state:
    st.session_state.completed = False

if not st.session_state.completed:
    if st.button("✅ I completed today's challenge!"):
        st.session_state.completed = True
        st.balloons()
else:
    st.markdown("🎉 You completed today’s challenge! Come back tomorrow for more!")

# Footer
st.markdown("---")
st.caption("Made with ❤ for a better mindset using Streamlit")
