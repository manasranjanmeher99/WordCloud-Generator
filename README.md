# ☁️ NLP Word Cloud Generator

An interactive Streamlit web application that generates beautiful Word Clouds from custom text or uploaded text files. This project demonstrates basic Natural Language Processing (NLP), text visualization, and web application development using Streamlit.

---

## 🚀 Features

✅ Paste text directly into the application

✅ Upload `.txt` files

✅ Generate Word Clouds instantly

✅ Customize Word Cloud settings:

* Background Color
* Width
* Height
* Maximum Number of Words

✅ View the most frequent words in a table

✅ Download the generated Word Cloud as a PNG image

---

---

## 🛠️ Technologies Used

* Python
* Streamlit
* WordCloud
* Pandas
* Matplotlib
* Collections (Counter)

---

## 📂 Project Structure

```text
WordCloud-Generator/
│
├── app.py
├── requirements.txt
├── README.md
│
└── image/
    └── wordcloud.png
```

---

## 📋 How It Works

### Step 1: Input Text

Users can either:

* Paste text into the text area
* Upload a `.txt` file

---

### Step 2: Configure Settings

Customize the Word Cloud using sidebar controls:

* Background Color
* Maximum Words
* Width
* Height

---

### Step 3: Generate Word Cloud

The application:

* Reads the input text
* Counts word frequencies
* Creates a Word Cloud visualization

---

### Step 4: Analyze Top Words

The app displays a table containing the most frequently occurring words in the text.

---

### Step 5: Download

Download the generated Word Cloud image as:

```text
wordcloud.png
```

---

## 📊 Sample Workflow

```text
User Input
(Text/File)
      │
      ▼
Text Processing
      │
      ▼
Word Frequency Analysis
      │
      ▼
Word Cloud Generation
      │
      ▼
Display Visualization
      │
      ▼
Download Image
```

---


## 📦 Requirements

```text
streamlit
wordcloud
matplotlib
pandas
```

---

## 🎯 Learning Outcomes

This project helps you understand:

* Natural Language Processing (NLP)
* Word Frequency Analysis
* Text Visualization
* Streamlit Web Development
* Interactive Dashboards
* File Upload Handling
* Data Analysis using Pandas

---

## 🔮 Future Enhancements

* Stopword Removal
* Custom Color Themes
* Word Frequency Charts
* PDF Upload Support
* Sentiment-Based Word Clouds
* Dark Mode UI
* Word Cloud Shapes (Circle, Heart, Star, etc.)

---


## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
