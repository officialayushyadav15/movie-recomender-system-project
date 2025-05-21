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

1. Make sure the virtual environment is activated and dependencies installed.
2. Download `similarity.pkl` from Google Drive at runtime.

### 🔗 Use External Hosting for `similarity.pkl`

Since `similarity.pkl` exceeds GitHub’s file size limit (100MB), it is stored externally.

```python
import gdown
import os

if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1htdP0IFthOGfDTmhfVtY7nN3uFk_xtqx"
    gdown.download(url, "similarity.pkl", quiet=False)
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🔑 Steps to Get OMDb API Key

You’ll need an OMDb API key to fetch movie posters and details.

👉 Go to [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

### Follow These Steps:

1. Choose a plan: Free (for personal) or Paid (for commercial use)
2. Fill in the form (email + usage type)
3. Submit and check your email for your API key
4. Test the key:

```bash
https://www.omdbapi.com/?t=Inception&apikey=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual key in `app.py`.

---

## ✅ Deploying on Render

1. Go to 👉 [https://render.com](https://render.com)
2. Sign in with GitHub
3. Click on **New Web Service**
4. Connect your GitHub repository
5. Set the **Build Command**:

   ```bash
   pip install -r requirements.txt
   ```
6. Set the **Start Command**:

   ```bash
   streamlit run app.py
   ```
7. Choose the **Free Plan**
8. Done! Your app will be live like this:
   👉 [Live Demo](https://movie-recomender-system-nxga.onrender.com)

---

## 📋 Requirements File (`requirements.txt`)

Includes:

```
streamlit
pandas
scikit-learn
requests
gdown
numpy
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

## 🛠 Contributing

Feel free to fork this repo and submit pull requests.
Suggestions, improvements, and bug reports are welcome!

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 📧 **Contact & Support**

* GitHub: [officialayushyadav15](https://github.com/officialayushyadav15)
* Project Issues: [Open here](https://github.com/officialayushyadav15/movie_recomender_system_project/issues)


