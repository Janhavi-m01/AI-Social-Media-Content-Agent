import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import io

# -------------------- LOGIN --------------------
st.set_page_config(page_title="AI Social Media Agent", page_icon="🤖")

st.title("🤖 AI Social Media Content Agent")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("👤 Enter your name", key="login_name")
    if st.button("Login 🚀"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.warning("⚠️ Please enter your name")
    st.stop()

st.success(f"Welcome, {st.session_state.username} 👋")
st.markdown("---")

# -------------------- CONTENT GENERATOR --------------------
st.header("📝 Content Generator")

topic = st.text_input("💡 Enter your post topic", key="topic")
platform = st.selectbox("📱 Platform", ["Instagram", "LinkedIn", "Twitter"])
tone = st.selectbox("🎭 Tone", ["Casual", "Professional", "Funny"])

def generate_caption(topic, tone):
    if tone == "Casual":
        return f"✨ Just vibing with **{topic}** — stay tuned! 😎"
    elif tone == "Professional":
        return f"🚀 Exploring **{topic}** with focus, growth & consistency."
    else:
        return f"😂 {topic} but make it legendary! Who relates? 👀🔥"

def generate_hashtags(topic, platform):
    clean = topic.replace(" ", "").lower()
    if platform == "Instagram":
        return f"#{clean} #reels #instagrowth #creatorlife #trending 🔥"
    elif platform == "LinkedIn":
        return f"#{clean} #careergrowth #professional #linkedinindia 💼"
    else:
        return f"#{clean} #twitter #dailycontent #techtrends 🧠"

caption = ""
hashtags = ""

if st.button("✨ Generate Content"):
    if topic:
        caption = generate_caption(topic, tone)
        hashtags = generate_hashtags(topic, platform)
        st.success(caption)
        st.info(hashtags)
    else:
        st.warning("⚠️ Please enter a topic")

# -------------------- POSTING TIME --------------------
st.markdown("---")
st.header("⏰ Best Posting Time")

def suggest_time(platform):
    return {
        "Instagram": "📈 7 PM – 9 PM (High engagement)",
        "LinkedIn": "📈 8 AM – 10 AM (Professional hours)",
        "Twitter": "📈 12 PM – 1 PM (Peak scroll time)"
    }[platform]

st.success(suggest_time(platform))

# -------------------- IMAGE UPLOAD --------------------
st.markdown("---")
st.header("📷 Smart Image Captioning")

uploaded_image = st.file_uploader("Upload post image", type=["jpg", "jpeg", "png"])

smart_caption = ""

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Smart rule-based caption
    if platform == "Instagram":
        smart_caption = "📸 Every picture tells a story — what’s yours? ✨👇"
    elif platform == "LinkedIn":
        smart_caption = "📊 Visuals that reflect growth, learning & professionalism."
    else:
        smart_caption = "👀 This image says more than words. What do you think?"

    st.info("🧠 Smart Caption Suggestion")
    st.write(smart_caption)

# -------------------- ENGAGEMENT ANALYZER --------------------
st.markdown("---")
st.header("📊 Engagement Analyzer")

likes = st.number_input("👍 Likes", min_value=0)
comments = st.number_input("💬 Comments", min_value=0)
shares = st.number_input("🔁 Shares", min_value=0)

def analyze(l, c, s):
    score = l + (c * 2) + (s * 3)
    if score >= 100:
        return score, "🔥 Excellent engagement!"
    elif score >= 50:
        return score, "👍 Good engagement. Add CTA or emojis."
    else:
        return score, "⚠️ Low engagement – improvement needed."

if st.button("Analyze Engagement 📊"):
    score, msg = analyze(likes, comments, shares)
    st.write(f"📌 Engagement Score: **{score}**")
    st.info(msg)

    if score < 50:
        st.error("🔧 AI Improvement Suggestions")
        st.write("🔥 **Improved Caption:**")
        st.write("Don’t just scroll — react ❤️, comment 💬, and share 🔁!")
        st.write("🚀 **Improved Hashtags:**")
        st.write("#viral #explore #engagementboost #contentcreator #techai 🤖")

    df = pd.DataFrame({
        "Metric": ["Likes", "Comments", "Shares"],
        "Count": [likes, comments, shares]
    })

    fig, ax = plt.subplots()
    ax.bar(df["Metric"], df["Count"])
    ax.set_title("Engagement Breakdown")
    st.pyplot(fig)

# -------------------- DOWNLOAD BUTTON --------------------
st.markdown("---")
st.header("⬇️ Download Content")

download_text = f"""
CAPTION:
{caption or smart_caption}

HASHTAGS:
{hashtags}

Generated using AI Social Media Content Agent 🤖
"""

buffer = io.BytesIO()
buffer.write(download_text.encode())
buffer.seek(0)

st.download_button(
    label="📥 Download Caption & Hashtags",
    data=buffer,
    file_name="social_media_content.txt",
    mime="text/plain"
)
