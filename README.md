# Google-s-AI-Gemini-Pro-End-to-End-LLM-Project-AI-Blogging-Assistant-with-Hugging-Face
Blogcraft is an **AI-powered blog creation tool** that helps you generate high-quality blog posts and matching AI-generated images in minutes.  
It uses **Google Gemini** for natural language content creation and **Hugging Face Stable Diffusion** for image generation, all wrapped in a sleek **Streamlit** web app.

---

## 🚀 Features
- **AI Blog Writing**: Generates engaging, SEO-friendly blog posts based on your title and keywords.
- **Custom Word Count**: Choose blog length from 250 to 1000 words.
- **AI Image Generation**: Creates blog-relevant images using Stable Diffusion.
- **Interactive UI**: Simple and intuitive interface built with Streamlit.
- **Keyword Integration**: Ensures your provided keywords are incorporated into the blog.
- **Multi-Image Support**: Generate up to 5 images per blog post.

---

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Content Generation**: [Google Gemini API](https://ai.google.dev/)
- **Image Generation**: [Hugging Face Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4)
- **Languages**: Python
- **Other Libraries**: PIL, Requests, Base64, IO

---

## 📂 Project Structure
Blogcraft/

-  app.py # Main Streamlit app
-  apikey.py # API keys file 
-  requirements.txt # Required Python packages
-  README.md # Project documentation

---

## 🔑 Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/YOUR-USERNAME/Blogcraft.git
cd Blogcraft

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create apikey.py
Create a file named apikey.py in the root directory and add:

python
google_gemini_api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
huggingface_api_key = "YOUR_HUGGINGFACE_API_KEY"

4️⃣ Run the App
streamlit run app.py

---
##📸 Screenshots
Main Interface
<img width="1901" height="839" alt="Screenshot 2025-08-10 153137" src="https://github.com/user-attachments/assets/cf7dd3cf-25fa-4f76-bb55-2fff2aff2c12" />

Generated Blog Example
<img width="1916" height="852" alt="Screenshot 2025-08-10 153112" src="https://github.com/user-attachments/assets/14a99f62-04b1-4cd6-82e0-993466bea31d" />

AI-Generated Images
<img width="932" height="510" alt="image" src="https://github.com/user-attachments/assets/23ee253c-3194-446c-9159-cb0f74b730c7" />

---

##🌟 Use Cases
Content writers & bloggers looking to speed up blog creation.
SEO specialists needing keyword-focused content.
Small businesses wanting quick blog & visual assets.


##💡 Future Improvements
Support for multiple AI models (GPT-4, Claude, etc.)

Multi-language blog generation.

Direct blog export to Markdown/HTML.

User authentication & API usage tracking.
