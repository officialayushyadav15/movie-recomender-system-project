# 🎬 Movie Recommender System 🍿

## 🔍 Project Overview

The **Movie Recommender System** is a content-based filtering web app built using Python and Streamlit. It utilizes **IMDb and TMDB metadata**, **NLP-based similarity scoring**, and the **OMDb API** to suggest movies similar to a selected title.

🚀 **Live Demo**: [https://movie-recomender-system-nxga.onrender.com](https://movie-recomender-system-nxga.onrender.com)

📦 **Dataset Source**: [Kaggle - IMDb and TMDb Movie Metadata (1M+)](https://www.kaggle.com/datasets/shubhamchandra235/imdb-and-tmdb-movie-metadata-big-dataset-1m?utm_source=chatgpt.com)

---

## 🤖 Model Overview

This project follows the pipeline:

1. **Data Ingestion**: Load data from TMDB & IMDb datasets.
2. **Preprocessing**: Clean, merge, and enrich metadata.
3. **Feature Engineering**: Combine genres, keywords, cast, crew into a “tags” column.
4. **Similarity Calculation**: Use TF-IDF and cosine similarity to compute closeness between movies.
5. **Model Saving**: Save computed similarity matrix as `similarity.pkl`.
6. **Web Deployment**: Build a Streamlit app for real-time recommendations.

---

## 🌟 Features

* 📌 Recommend top 5 similar movies based on selected title
* 🖼 Movie posters via **OMDb API**
* 🔍 Search bar to look up any movie
* 💾 Persistent hosting of large model file (`similarity.pkl`)
* ☁️ One-click deployment on Render

---

## 🛠 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/movie_recomender_system_project.git
cd movie_recomender_system_project
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
movie_recomender_system_project/
│
├── model/
│   ├── dataset/
│   │   ├── tmdb_5000_credits.csv
│   │   ├── tmdb_5000_moviess.csv
│   │   └── data.csv
│   ├── dataset_train.py
│   └── movie_recomender_system.py
│
├── app.py
├── requirements.txt
├── movie_dict.pkl
├── similarity.pkl  ← Downloaded at runtime (see below)
```

### File Descriptions

* **app.py**: Main Streamlit frontend for movie search and recommendations
* **movie\_recomender\_system.py**: Core logic for recommendation engine
* **dataset\_train.py**: Preprocessing and dataset merging logic
* **movie\_dict.pkl**: Serialized movie data dictionary
* **similarity.pkl**: Cosine similarity matrix (accessed from Google Drive)

---

## 📚 Libraries and Dependencies

* [Streamlit](https://docs.streamlit.io/) – UI framework for building web apps
* [Pandas](https://pandas.pydata.org/docs/) – Data handling
* [Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) – TF-IDF and similarity
* [Requests](https://docs.python-requests.org/en/latest/) – API calls
* [Pickle](https://docs.python.org/3/library/pickle.html) – Model serialization
* [gdown](https://pypi.org/project/gdown/) – For downloading `similarity.pkl` from Google Drive

---



## 🚀 How to Run the Application

To run the **Movie Recommender System**, follow these steps:

### ✅ Step 1: Activate Virtual Environment

Make sure you have created and activated your virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### ✅ Step 2: Install Project Dependencies

Install all the necessary Python packages using:

```bash
pip install -r requirements.txt
```

### 📦 Step 3: Download `similarity.pkl` at Runtime

> ⚠️ `similarity.pkl` is larger than 100MB and cannot be stored on GitHub. It is hosted on **Google Drive** and downloaded dynamically.

Add this snippet at the start of your `app.py` to ensure the file is downloaded if missing:

```python
import gdown
import os

if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1htdP0IFthOGfDTmhfVtY7nN3uFk_xtqx"
    gdown.download(url, "similarity.pkl", quiet=False)
```

### ▶️ Step 4: Run the Application

Once dependencies are installed and `similarity.pkl` is downloaded, run the application using Streamlit:

```bash
streamlit run app.py
```

---

## 🔐 How to Get Your OMDb API Key

This project uses the **OMDb API** to fetch movie posters and details. You’ll need a personal API key.

### 🔗 Get Your OMDb API Key Here:

👉 [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

### 📋 Steps to Obtain the API Key:

1. Visit the link above.
2. Choose a plan:

   * **Free** (for personal use)
   * **Paid** (for commercial/heavy use)
3. Fill in the form with:

   * Your **email address**
   * **Usage type**
4. Click **Submit**
5. Check your inbox for the API key.

### 🔍 Test Your Key

You can test the key by replacing `YOUR_API_KEY` in the URL below:

```bash
https://www.omdbapi.com/?t=Inception&apikey=YOUR_API_KEY
```

> 🎯 Be sure to replace `YOUR_API_KEY` in `app.py` with your actual key.

---

## ☁️ Deploying the App on Render

You can host your Streamlit app for free using [Render](https://render.com). Here's how:

### 🌐 Step-by-Step Deployment Guide:

1. Go to 👉 [https://render.com](https://render.com)

2. Sign in using your GitHub account.

3. Click on **New Web Service**.

4. Connect your GitHub repository.

5. Configure the following:

   * **Build Command**:

     ```bash
     pip install -r requirements.txt
     ```

   * **Start Command**:

     ```bash
     streamlit run app.py
     ```

6. Choose the **Free Plan**.

7. Wait for the build to finish. Your live website will be available at:

   🔗 **Live Demo**: [https://movie-recomender-system-nxga.onrender.com](https://movie-recomender-system-nxga.onrender.com)

---

## 📁 Hosting Large Files Externally

### 🔄 Using Google Drive for `similarity.pkl`

GitHub restricts file uploads to 100MB. To work around this:

1. Upload `similarity.pkl` to **Google Drive**.
2. Make the file public or accessible via link.
3. Get the file ID from the shared link.
4. Use the following code to download it at runtime:

```python
import gdown
import os

if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1htdP0IFthOGfDTmhfVtY7nN3uFk_xtqx"
    gdown.download(url, "similarity.pkl", quiet=False)
```

> ✅ You can also use other services like **Dropbox**, **AWS S3**, or **Streamlit file uploader** for temporary hosting.

---




## 📋 Requirements File (`requirements.txt`)

This project requires the following Python packages:

```
streamlit
pandas
scikit-learn
requests
gdown
numpy
```

Make sure to install all dependencies by running:

```bash
pip install -r requirements.txt
```



---

## 📸 Output Screenshots

> Add some screenshots of:
>
> * Homepage
> * Recommendations for a movie
> * API key error handling
> * Deployed version

*(Upload these to `/screenshots` folder and link them here if available.)*

---

## 🎥 Demo Video

> *(Optional: Upload a YouTube demo video and link it here)*

---

## 🙋‍♂️ About Me

I'm Ayush Yadav, a passionate developer with an interest in computer vision, automation, and innovative tech solutions.  
Always exploring new technologies and building things that matter.

### Let’s connect:

- 📧 **Email:** [officialayushyadav15@gmail.com](mailto:officialayushyadav15@gmail.com)
- 💼 **GitHub:** [@officialayushyadav15](https://github.com/officialayushyadav15)
- 🔗 **LinkedIn:** [Ayush Yadav](https://www.linkedin.com/in/ayush-yadav-408924230/)

---

## 🤝 Contributions

Feel free to open issues or submit pull requests. Any improvements or gesture additions are welcome!

---


### 🚀 Happy Coding and Gesture-Controlling! 👋


