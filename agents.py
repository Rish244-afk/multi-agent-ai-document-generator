import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyAPyuVwacDwgKweb_tEhd3jWpHlhgAJ4EY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def writer(topic):
    prompt = f"""
    Write a well-structured article on {topic}.
    Include:
    - Introduction
    - Key points with examples
    - Conclusion
    """
    response = model.generate_content(prompt)
    return response.text


def reviewer(text):
    prompt = f"""
    Analyze the following content and give:
    - Strengths
    - Weaknesses
    - Suggestions for improvement

    Content:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text


def improver(text, review):
    prompt = f"""
    Improve the content using the review.

    Make it:
    - More clear
    - Better structured
    - More engaging

    Content:
    {text}

    Review:
    {review}
    """
    response = model.generate_content(prompt)
    return response.text