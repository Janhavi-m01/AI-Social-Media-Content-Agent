import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# -------------------- PAGE SETUP --------------------
st.set_page_config(page_title="AI Social Media Content Agent", layout="centered")

# -------------------- LOGIN --------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Enter your name")
    if st.button("Login"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.warning("Please enter your name")
    st.stop()

st.success(f"Welcome, {st.session_state.username} 👋")

# -------------------- APP TITLE --------------------
st.title("🤖 AI Social Media Content Agent")
st.write("Create captions, hashtags, posting strategy & analyze engagement — **FREE**")

# -------------------- CONTENT INPUT --------------------
topic = st.text_input("📝 Enter your post topic")
platform = st.selectbox("📱 Choose platform", ["Instagram", "LinkedIn", "Twitter"])
tone = st.selectbox("🎭 Choose tone", ["Casual", "Professional", "Funny"])

# -------------------- CAPTION GENERATOR --------------------
def generate_caption(topic, tone, platform):
    if tone == "Casual":
        return f"✨ Loving the journey with {topic}! Stay tuned 🚀"
    elif tone == "Professional":
        return f"Exploring {topic} with focus, consistency, and growth 📈"
    else:
        return f"{topic} but make it legendary 😎🔥"

if st.button("✍️ Generate Caption"):
    if topic:
        st.session_state.caption = generate_caption(topic, tone, platform)
        st.success(st.session_state.caption)
    else:
        st.warning("Please enter a topic")

# -------------------- HASHTAG GENERATOR --------------------
def generate_hashtags(topic, platform):
    key = topic.replace(" ", "").lower()
    if platform == "Instagram":
        return f"#{key} #reels #instagrowth #creatorlife #trending"
    elif platform == "LinkedIn":
        return f"#{key} #professional #careerdevelopment #linkedinindia"
    else:
        return f"#{key} #twitterx #dailycontent #techtrends"

if st.button("🏷️ Generate Hashtags"):
    if topic:
        st.info(generate_hashtags(topic, platform))
    else:
        st.warning("Please enter a topic")

# -------------------- POSTING TIME --------------------
def best_time(platform):
    return {
        "Instagram": "🕖 7 PM – 9 PM",
        "LinkedIn": "🕗 8 AM – 10 AM",
        "Twitter": "🕛 12 PM – 1 PM"
    }[platform]

if st.button("⏰ Best Posting Time"):
    st.success(f"Best time to post on {platform}: {best_time(platform)}")

# -------------------- ENGAGEMENT ANALYZER --------------------
st.subheader("📊 Platform-wise Engagement Analyzer")

if platform == "Instagram":
    likes = st.number_input("❤️ Likes", min_value=0)
    comments = st.number_input("💬 Comments", min_value=0)
    shares = st.number_input("🔁 Shares", min_value=0)
    score = likes + (comments * 2) + (shares * 3)

elif platform == "LinkedIn":
    reactions = st.number_input("👍 Reactions", min_value=0)
    comments = st.number_input("💬 Comments", min_value=0)
    reposts = st.number_input("🔁 Reposts", min_value=0)
    score = reactions + (comments * 2) + (reposts * 3)

else:  # Twitter
    likes = st.number_input("❤️ Likes", min_value=0)
    replies = st.number_input("💬 Replies", min_value=0)
    retweets = st.number_input("🔁 Retweets", min_value=0)
    score = likes + (replies * 2) + (retweets * 3)

if st.button("📈 Analyze Engagement"):
    st.write(f"### Engagement Score: **{score}**")

    if score >= 100:
        st.success("🔥 Excellent engagement! Keep the same strategy.")
    elif score >= 50:
        st.info("👍 Good engagement. Try adding a question or emojis.")
    else:
        st.warning("😕 Low engagement detected")
        st.markdown("""
        **Improvement Suggestions:**
        - Use a hook in first line  
        - Add trending hashtags  
        - Post at suggested time  
        - Ask a question  
        - Use emojis strategically 🚀✨  
        """)

# -------------------- IMAGE UPLOAD --------------------
st.subheader("📷 Image-based Caption Generator")

uploaded_image = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    smart_caption = (
        "🚀 Turning ideas into impact 💡✨\n"
        "Consistency + Creativity = Growth 📈🤖\n"
        "#AI #TechLife #ContentCreator"
    )

    st.success("🧠 Smart Caption Generated")
    st.write(smart_caption)

    # Download button
    buffer = BytesIO()
    buffer.write(smart_caption.encode())
    st.download_button(
        label="⬇️ Download Caption",
        data=buffer,
        file_name="caption.txt",
        mime="text/plain"
    )

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("Built with ❤️ using Python & Streamlit | Zero-cost AI Project")
