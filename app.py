import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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
