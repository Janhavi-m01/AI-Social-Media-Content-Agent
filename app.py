import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
st.title("AI Social Media Content Agent")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("👤 Enter your name")
    if st.button("Login"):
        if username.strip() != "":
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.warning("Please enter your name")
    st.stop()
st.success(f"Welcome, {st.session_state.username} 👋")



st.title(" AI Social Media Content Agent")
st.write("Create captions, hashtags & posting strategy for FREE!")

topic = st.text_input("Enter your post topic:")
platform = st.selectbox("Choose platform", ["Instagram", "LinkedIn", "Twitter"])
tone = st.selectbox("Choose tone", ["Casual", "Professional", "Funny"])

def generate_caption(topic, tone):
    if tone == "Casual":
        return f"Just vibing with {topic}  Stay tuned!"
    elif tone == "Professional":
        return f"Introducing {topic}. Focused on growth and consistency."
    elif tone == "Funny":
        return f"{topic} but make it legendary "

if st.button("Generate Caption"):
    if topic:
        st.success(generate_caption(topic, tone))
    else:
        st.warning("Please enter a topic first.")
st.subheader(" Hashtag Generator")

def generate_hashtags(topic, platform):
    clean_topic = topic.replace(" ", "").lower()

    if platform == "Instagram":
        return f"#{clean_topic} #instagood #contentcreator #reels #trending"
    elif platform == "LinkedIn":
        return f"#{clean_topic} #professional #careergrowth #linkedinindia"
    else:
        return f"#{clean_topic} #twitter #dailycontent #trends"

if st.button("Generate Hashtags"):
    if topic:
        st.info(generate_hashtags(topic, platform))
    else:
        st.warning("Please enter a topic first.")

st.subheader(" Best Posting Time")

def suggest_posting_time(platform):
    if platform == "Instagram":
        return "📈 Best time: 7 PM – 9 PM (High engagement)"
    elif platform == "LinkedIn":
        return "📈 Best time: 8 AM – 10 AM (Professional hours)"
    else:
        return "📈 Best time: 12 PM – 1 PM (Peak scrolling time)"

if st.button("Suggest Posting Time"):
    st.success(suggest_posting_time(platform))
st.subheader("📊 Engagement Analyzer")

likes = st.number_input("Likes", min_value=0)
comments = st.number_input("Comments", min_value=0)
shares = st.number_input("Shares", min_value=0)

def analyze_engagement(likes, comments, shares):
    score = likes + (comments * 2) + (shares * 3)

    if score >= 100:
        return score, "🔥 Excellent engagement! Keep the same content style."
    elif score >= 50:
        return score, "👍 Good engagement. Try adding emojis or a question."
    else:
        return score, "😕 Low engagement. Improve caption and posting time."

if st.button("Analyze Engagement"):
    score, feedback = analyze_engagement(likes, comments, shares)

    st.write(f"📌 Engagement Score: **{score}**")
    st.info(feedback)

    # Graph
    data = {
        "Likes": likes,
        "Comments": comments,
        "Shares": shares
    }

    df = pd.DataFrame(list(data.items()), columns=["Type", "Count"])

    plt.figure()
    plt.bar(df["Type"], df["Count"])
    plt.title("Engagement Breakdown")
    st.pyplot(plt)
st.subheader("📊 Engagement Analyzer")

likes = st.number_input("Likes", min_value=0, key="likes_input")
comments = st.number_input("Comments", min_value=0, key="comments_input")
shares = st.number_input("Shares", min_value=0, key="shares_input")

engagement_score = likes + (comments * 2) + (shares * 3)

st.write(f"Engagement Score: **{engagement_score}**")


st.subheader("📷 Upload Image")

uploaded_image = st.file_uploader(
    "Upload an image for your post",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.info("Suggested Caption based on image:")
    st.write("✨ A moment worth sharing. Stay inspired and keep creating! ✨")

