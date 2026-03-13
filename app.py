import streamlit as st
import pandas as pd
import pickle
import requests
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API")

# PAGE CONFIG 
st.set_page_config(
    page_title="AI Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0b0f1c 0%, #1a1f33 100%);
    }

    .title-container {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ff6b6b, #ffd93d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #a0a8c0;
    }

    .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600;
        font-size: 1.1rem;
    }
    .stSelectbox > div > div {
        background-color: #fff45;         
        border: 1px solid #3e435a;
        border-radius: 12px;
        color: rgba(0,0,0,0.3);
    }

    .num-selector {
        background: #2a2f45;
        padding: 1rem 2rem;
        border-radius: 16px;
        margin: 1rem 0 2rem 0;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    .num-selector label {
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        margin-right: 1rem;
    }

    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
        transition: all 0.3s ease;
        width: auto;
        min-width: 250px;
        margin: 0 auto;
        display: block;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.5);
        background: linear-gradient(135deg, #ff5252, #ff7676);
    }

    /* Movie card styling - now clickable */
    .movie-card-link {
        text-decoration: none;
        color: inherit;
        display: block;
        height: 100%;
    }
    .movie-card {
        background: #1e2338;
        border-radius: 16px;
        padding: 1rem;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .movie-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 30px rgba(0,0,0,0.6);
    }
    .movie-title {
        font-weight: 600;
        font-size: 1rem;
        margin-top: 0.8rem;
        color: #f0f0f0;
        line-height: 1.4;
        flex-grow: 1;
    }
    .poster-img {
        border-radius: 12px;
        width: 100%;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }

    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 2rem 0;
        color: #6f7a9e;
        border-top: 1px solid #2a2f45;
    }
    .footer a {
        color: #ff8e8e;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }

    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        .subtitle {
            font-size: 1rem;
        }
        .stButton > button {
            min-width: 200px;
            font-size: 1rem;
        }
        .movie-title {
            font-size: 0.9rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="title-container">
    <div class="main-title">🎬 AI Movie Recommender</div>
    <div class="subtitle">Discover your next favorite film</div>
</div>
""", unsafe_allow_html=True)

# LOAD DATA 
@st.cache_data(show_spinner=False)
def load_data():
    with st.spinner("Loading movie database..."):
        sleep(1)  # remove in production
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)
        similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

# MOVIE SELECTION
selected_movie = st.selectbox(
    "🎥 Choose a movie you like",
    movies['title'].values,
    index=0,
    help="Start typing to search"
)

# NUMBER OF RECOMMENDATIONS 
st.markdown('<div class="num-selector">', unsafe_allow_html=True)
num_recommendations = st.selectbox(
    "How many recommendations?",
    options=[5, 10, 20, 50],
    index=0,
    help="Select the number of similar movies to display"
)
st.markdown('</div>', unsafe_allow_html=True)

# POSTER FETCH FUNCTION
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# RECOMMEND FUNCTION 
def get_recommendations(movie, num_movies):
    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]
    
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:num_movies+1]

    titles = []
    posters = []
    tmdb_links = []

    for i, _ in movies_list:
        movie_id = movies.iloc[i].movie_id
        titles.append(movies.iloc[i].title)
        posters.append(fetch_poster(movie_id))
        tmdb_links.append(f"https://www.themoviedb.org/movie/{movie_id}")

    return titles, posters, tmdb_links

# RECOMMEND BUTTON
if st.button("🔍 Get Recommendations", use_container_width=False):
    if selected_movie:
        with st.spinner("Fetching recommendations..."):
            titles, posters, tmdb_links = get_recommendations(selected_movie, num_recommendations)
        
        st.success(f"Here are your {num_recommendations} recommendations!")
        
        # Responsive grid (4 columns)
        num_cols = 4
        rows_titles = [titles[i:i+num_cols] for i in range(0, len(titles), num_cols)]
        rows_posters = [posters[i:i+num_cols] for i in range(0, len(posters), num_cols)]
        rows_links = [tmdb_links[i:i+num_cols] for i in range(0, len(tmdb_links), num_cols)]

        for row_titles, row_posters, row_links in zip(rows_titles, rows_posters, rows_links):
            cols = st.columns(len(row_titles))
            for idx, col in enumerate(cols):
                with col:
                    # Clickable card: entire card is a link
                    st.markdown(f"""
                    <a href="{row_links[idx]}" target="_blank" class="movie-card-link">
                        <div class="movie-card">
                            <img src="{row_posters[idx]}" class="poster-img" alt="{row_titles[idx]}">
                            <div class="movie-title">{row_titles[idx]}</div>
                        </div>
                    </a>
                    """, unsafe_allow_html=True)
    else:
        st.warning("Please select a movie first.")

# FOOTER 
st.markdown("""
<div class="footer">
    Built By Rehman Ahmad using <a href="https://streamlit.io" target="_blank">Streamlit</a> • 
    Data from <a href="https://www.themoviedb.org/" target="_blank">TMDb</a>
</div>
""", unsafe_allow_html=True)