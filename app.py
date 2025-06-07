import streamlit as st
from post_generator import generate_post

st.set_page_config(page_title="Social Media Post Generator", page_icon="📝")

st.title("📝 Social Media Post Generator")
st.write("Generate catchy posts for your favorite platform using just a few inputs!")

# --- Form Inputs ---
with st.form("post_form"):
    platform = st.selectbox("Choose a platform", ["Instagram", "Twitter", "LinkedIn"])
    tone = st.selectbox("Select tone", ["Casual", "Professional", "Funny", "Inspirational"])
    topic = st.text_input("What's the post about?", placeholder="e.g., Importance of morning routine")
    custom_hashtags = st.text_input("Add custom hashtags (optional)", placeholder="#motivation #selfcare")
    submitted = st.form_submit_button("Generate Post")

# --- Post Output ---
if submitted:
    if not topic.strip():
        st.warning("Please enter a topic to generate a post.")
    else:
        post, hashtags = generate_post(platform, tone, topic, custom_hashtags)
        st.subheader("Generated Post:")
        st.code(post, language='markdown')
        if hashtags:
            st.markdown(f"**Suggested Hashtags:** {hashtags}")
