import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

st.set_page_config(
    page_title="Word Cloud Generator",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ NLP Word Cloud Generator")

st.write(
    "Generate beautiful Word Clouds from your text data."
)

# Text input
text_input = st.text_area(
    "Paste your text here:",
    height=200
)

# File Upload
uploaded_file = st.file_uploader(
    "Upload a text file",
    type=["txt"]
)

text = ""

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

elif text_input:
    text = text_input

# Sidebar Settings
st.sidebar.header("Settings")

bg_color = st.sidebar.selectbox(
    "Background Color",
    ["white", "black"]
)

max_words = st.sidebar.slider(
    "Maximum Words",
    50,
    500,
    200
)

width = st.sidebar.slider(
    "Width",
    500,
    2000,
    1000
)

height = st.sidebar.slider(
    "Height",
    300,
    1500,
    500
)

if st.button("Generate Word Cloud"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        wc = WordCloud(
            width=width,
            height=height,
            background_color=bg_color,
            max_words=max_words
        ).generate(text)

        st.subheader("Generated Word Cloud")

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")

        st.pyplot(fig)

        # Word Frequency Table
        words = text.lower().split()
        freq = Counter(words)

        df = pd.DataFrame(
            freq.items(),
            columns=["Word", "Frequency"]
        ).sort_values(
            by="Frequency",
            ascending=False
        )

        st.subheader("Top Words")

        st.dataframe(df.head(20))

        wc.to_file("wordcloud.png")

        with open("wordcloud.png", "rb") as file:
            st.download_button(
                label="Download Word Cloud",
                data=file,
                file_name="wordcloud.png",
                mime="image/png"
            )