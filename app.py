import streamlit as st
from agents import writer, reviewer, improver

st.set_page_config(page_title="Multi-Agent AI System")

st.title("🤖 Multi-Agent AI Document Generator")

def word_count(text):
    return len(text.split())

def improvement_score(original, improved):
    return round((len(improved) - len(original)) / len(original) * 100, 2)

topic = st.text_input("Enter a topic")

if st.button("Generate"):
    with st.spinner("Agents are working..."):

        st.subheader("✍️ Writer Agent")
        draft = writer(topic)
        st.write(draft)

        st.subheader("🔍 Reviewer Agent")
        review = reviewer(draft)
        st.write(review)

        st.subheader("✅ Improver Agent")
        final = improver(draft, review)
        st.write(final)

        st.subheader("📊 Metrics")

        wc_original = word_count(draft)
        wc_final = word_count(final)
        score = improvement_score(draft, final)

        st.write(f"Original Word Count: {wc_original}")
        st.write(f"Final Word Count: {wc_final}")
        st.write(f"Improvement Score: {score}%")

        st.download_button("📥 Download Final Output", final)