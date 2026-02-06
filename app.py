import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import io

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI Social Media Content Agent",
    page_icon="🤖",
    layout="centered"
)

# -------------------- LOGIN --------------------
st.title("🤖 AI Social Media Content Agent")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("### 🔐 User Login")
    username = st.text_input("Enter your name", key="login_name")
    if st.button("Login 🚀"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.warning("Please enter your name")
    st.stop()

st.success(f"Welcome, {st.session_state.username} 👋")

# -------------------- SIDEBAR --------------------
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "📝 Content Generator",
        "📷 Image Captioning",
        "📊 Engagement Analyzer",
        "⬇️ Download"
    ]
)

# -------------------- COMMON INPUTS --------------------
st.sidebar.markdown("---")
platform = st.sidebar.selectbox(
    "📱 Platform",
    ["Instagram", "LinkedIn", "Twitter"]
)

tone = st.sidebar.selectbox(
    "🎭 Tone",
    ["Casual", "Professional", "Funny"]
)

# -------------------- LOGIC FUNCTIONS --------------------
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

def best_time(platform):
    return {
        "Instagram": "7 PM – 9 PM",
        "LinkedIn": "8 AM – 10 AM",
        "Twitter": "12 PM – 1 PM"
    }[platform]

# -------------------- SECTION 1 --------------------
if section == "📝 Content Generator":
    st.header("📝 Content Generator")
    st.caption("Generate captions, hashtags & posting strategy")

    topic = st.text_input("💡 Enter post topic")

    if st.button("✨ Generate Content"):
        if topic:
            caption = generate_caption(topic, tone)
            hashtags = generate_hashtags(topic, platform)

            st.success("📌 Caption")
            st.write(caption)

            st.info("🏷️ Hashtags")
            st.write(hashtags)

            st.success(f"⏰ Best Time to Post: **{best_time(platform)}**")
            st.session_state.caption = caption
            st.session_state.hashtags = hashtags
        else:
            st.warning("Please enter a topic")

# -------------------- SECTION 2 --------------------
elif section == "📷 Image Captioning":
    st.header("📷 Smart Image Captioning")
    st.caption("Rule-based AI caption from image + platform")

    uploaded_image = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, use_column_width=True)

        if platform == "Instagram":
            smart_caption = "📸 Every picture tells a story — what’s yours? ✨👇"
        elif platform == "LinkedIn":
            smart_caption = "📊 Visuals that reflect growth, learning & professionalism."
        else:
            smart_caption = "👀 This image says more than words. What do you think?"

        st.success("🧠 Smart Caption")
        st.write(smart_caption)
        st.session_state.caption = smart_caption

# -------------------- SECTION 3 --------------------
elif section == "📊 Engagement Analyzer":
    st.header("📊 Engagement Analyzer")
    st.caption("Analyze & improve engagement automatically")

    likes = st.number_input("👍 Likes", min_value=0)
    comments = st.number_input("💬 Comments", min_value=0)
    shares = st.number_input("🔁 Shares", min_value=0)

    if st.button("Analyze Engagement"):
        score = likes + (comments * 2) + (shares * 3)
        st.metric("Engagement Score", score)

        if score >= 100:
            st.success("🔥 Excellent engagement!")
        elif score >= 50:
            st.info("👍 Good engagement. Add CTA or emojis.")
        else:
            st.error("⚠️ Low engagement detected")
            st.write("**Improved Caption:**")
            st.write("Don’t just scroll — react ❤️, comment 💬, and share 🔁!")
            st.write("**Improved Hashtags:**")
            st.write("#viral #explore #engagementboost #contentcreator #techai 🤖")

        df = pd.DataFrame({
            "Metric": ["Likes", "Comments", "Shares"],
            "Count": [likes, comments, shares]
        })

        fig, ax = plt.subplots()
        ax.bar(df["Metric"], df["Count"])
        ax.set_title("Engagement Breakdown")
        st.pyplot(fig)

# -------------------- SECTION 4 --------------------
elif section == "⬇️ Download":
    st.header("⬇️ Download Content")
    st.caption("Export generated content")

    caption = st.session_state.get("caption", "")
    hashtags = st.session_state.get("hashtags", "")

    if caption or hashtags:
        text = f"""
CAPTION:
{caption}

HASHTAGS:
{hashtags}

Generated using AI Social Media Content Agent 🤖
"""
        buffer = io.BytesIO()
        buffer.write(text.encode())
        buffer.seek(0)

        st.download_button(
            "📥 Download as Text File",
            buffer,
            file_name="social_media_content.txt",
            mime="text/plain"
        )
    else:
        st.info("Generate content first to download")
