import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import os
import gdown

load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

def fetch_poster(movie_title):
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_url = data.get('Poster')
        return poster_url if poster_url and poster_url != "N/A" else "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"OMDb API error for '{movie_title}': {e}")
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:7]
    
    recommend_movies = []
    recommended_posters = []
    
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommend_movies.append(title)
        recommended_posters.append(fetch_poster(title))
    
    return recommend_movies, recommended_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
# Download if not already present
if not os.path.exists("similarity.pkl"):
    file_id = "1htdP0IFthOGfDTmhfVtY7nN3uFk_xtqx"  # e.g., 1A2B3C4D5E6F7G8H9I
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, "similarity.pkl", quiet=False)

# Load the similarity matrix
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

#UI Configuration
st.set_page_config(page_title="CineMatch")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@400;600&display=swap');

    :root {
        --primary: #e50914;
        --hover: #b20710;
    }

    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        font-family: 'Poppins', sans-serif !important;
        padding-top: 30px;
    }

    h1 {
        text-align: center;
        color: #FFC300 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 3.5rem !important;
        letter-spacing: 3px;
        margin-bottom: 30px;
    }

    div[role="combobox"] input {
        background: #1a1a1a !important;
        color: #fff !important;
        border-radius: 8px !important;
        max-width: 600px;
        margin: 0 auto;
        padding: 12px 20px !important;
    }

    div[role="combobox"] input::placeholder {
        color: #888 !important;
    }

    button[class*="stButton"] {
        background: var(--primary) !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        border: none !important;
        padding: 12px 24px !important;
        display: block;
        margin: 20px auto;
    }

    button[class*="stButton"]:hover {
        background: var(--hover) !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.4);
    }

    .movie-card {
        position: relative;
        transition: transform 0.3s ease;
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .movie-card img {
        border-radius: 12px !important;
        box-shadow: 0 8px 20px rgba(229, 9, 20, 0.6);
        margin-bottom: 0.3rem;
        max-height: 150px;
        max-width: 100%;
        width: 50%;
        object-fit: cover;
        margin: 0 auto;
        transition: box-shadow 0.3s ease;
    }

    .movie-card:hover img {
        box-shadow: 0 12px 30px rgba(229, 9, 20, 0.9);
    }

    .movie-card p {
        color: #d1d1d1 !important;
        font-weight: 500;
        margin-top: 0.4rem;
        font-size: 0.9rem;
    }

    .movie-card::after {
        content: attr(data-rating);
        position: absolute;
        top: 10px;
        right: 10px;
        background: rgba(0, 0, 0, 0.6);
        color: #FFC300;
        padding: 4px 8px;
        font-size: 0.75rem;
        border-radius: 4px;
    }

    .loader {
        border: 5px solid #f3f3f3;
        border-top: 5px solid var(--primary);
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: auto;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @media (max-width: 768px) {
        .stColumns {
            flex-wrap: wrap !important;
            gap: 1rem !important;
        }
        .stColumn {
            flex: 1 1 45% !important;
            min-width: 45% !important;
        }
        .stApp {
            padding-top: 40px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Centered title with Orbitron font and gold color
st.title("CineMatch")



selected_movie = st.selectbox(
    ' ',
    movies['title'].values,
    key="movie_select"
)

if st.button('🍿 Get Recommendations'):
    with st.spinner('Finding perfect matches...'):
        titles, posters = recommend(selected_movie)
        
        # Create two rows of 6 columns each
        cols = st.columns(6)
        for idx in range(6):
            with cols[idx]:
                st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                st.image(posters[idx], use_container_width=True)
                st.caption(titles[idx])
                st.markdown('</div>', unsafe_allow_html=True)
        
