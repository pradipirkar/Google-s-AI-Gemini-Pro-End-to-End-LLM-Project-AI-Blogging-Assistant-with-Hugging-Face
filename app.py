
import streamlit as st
import base64
import os
import requests
from PIL import Image
from io import BytesIO
from google import genai
from google.genai import types
from apikey import google_gemini_api_key

# Set API key
os.environ["google_gemini_api_key"] = google_gemini_api_key


# Set app to wide mode
st.set_page_config(layout="wide")

# Title and subtitle
st.title('Blogcraft: Your AI Writing Companion')
st.subheader("Now you can craft perfect blogs with the help of AI — Blogcraft is your New AI Blog Companion")

# Sidebar for input
with st.sidebar:
    st.title("Input your blog detail")
    st.subheader("Enter details of the blog you want to generate")

    blog_title = st.text_input("Blog Title")
    keyword = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of words", min_value=250, max_value=1000, step=250)
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

# Submit button
submit_button = st.button("Generate Blog")

# Only run if submit button is clicked
if submit_button:
    # Initialize Gemini client
    client = genai.Client(api_key=os.environ.get("google_gemini_api_key"))
    model = "gemini-2.5-pro"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""
Generate a comprehensive, engaging blog post relevant to the given title and keywords: \"{blog_title}, {keyword}\".
Make sure to incorporate these keywords. The blog should be approximately {num_words} words in length, suitable for an online audience.
Ensure the content is original, informative, and maintains a consistent tone throughout.
"""),
            ],
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=0.9,
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        response_mime_type="text/plain",
    )

    # Capture generated blog content
    blog_output = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        blog_output += chunk.text

    # Display the blog in Streamlit
    st.subheader("📝 Your AI-Generated Blog:")
    st.write(blog_output)

    # Generate prompt for image
    image_prompt = f"Create a blog image based on this topic: {blog_title}, using themes from keywords: {keyword}"

    st.subheader("🖼️ AI-Generated Images:")

    for i in range(num_images):
        hf_headers = {
            "Authorization": f"Bearer {huggingface_api_key}"
        }
        hf_payload = {
            "inputs": image_prompt,
            "options": {"wait_for_model": True}
        }

        response = requests.post(
            "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4",
            headers=hf_headers,
            json=hf_payload
        )

        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            try:
                img = Image.open(image_bytes)
                st.image(img, caption=f"Image {i+1} for: {blog_title}")
            except Exception as e:
                st.warning(f"Image {i+1} couldn't be processed: {e}")
        else:
            st.warning(f"Image {i+1} failed: {response.status_code} - {response.text}")