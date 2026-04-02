<!DOCTYPE html>
<html>
<body>
<div style="font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #0b0f1c 0%, #1a1f33 100%); color: #eef2ff; border-radius: 24px;">

<!-- HEADER SECTION -->
<div style="text-align: center; padding: 3rem 1rem 2rem 1rem;">
    <h1 style="font-size: 3.5rem; font-weight: 800; background: linear-gradient(135deg, #ff6b6b, #ffd93d); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0;">🎬 AI Movie Recommender</h1>
    <p style="font-size: 1.2rem; color: #a0a8c0; margin-top: 0.5rem;">Discover your next favorite film with intelligent similarity matching</p>
    <div style="margin-top: 1.5rem;">
        <a href="https://ai-movie-recommender-79jkgdcvpcsyi5uq4t9ept.streamlit.app" target="_blank" style="background: linear-gradient(135deg, #ff6b6b, #ff8e8e); color: white; padding: 12px 28px; border-radius: 50px; text-decoration: none; font-weight: 600; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(255,107,107,0.3); transition: all 0.3s ease; display: inline-block;">🚀 Live Demo</a>
    </div>
</div>

<!-- BADGES -->
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin: 20px 0 30px;">
    <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🎯 Python</span>
    <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">📊 Streamlit</span>
    <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🤖 Cosine Similarity</span>
    <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🎨 TMDB API</span>
    <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">☁️ Streamlit Cloud</span>
</div>

<hr style="border-color: #2a2f45; margin: 20px 0;">

<!-- DESCRIPTION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; box-shadow: 0 12px 24px rgba(0,0,0,0.3);">
    <h2 style="color: #ffd93d; margin-top: 0;">✨ Overview</h2>
    <p style="font-size: 1.05rem; line-height: 1.6;">The <strong>AI Movie Recommender</strong> is a content‑based filtering system that suggests movies similar to your selected title. It analyzes movie attributes (genres, keywords, cast, crew, etc.) and computes similarity using <strong>cosine distance</strong> on TF‑IDF vectors. The frontend is built with <strong>Streamlit</strong>, and all poster images are fetched live from <strong>TMDb</strong>. The app is deployed on <strong>Streamlit Community Cloud</strong> for instant access.</p>
</div>

<!-- FEATURES -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">⭐ Key Features</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <div style="background: #0b0f1c; padding: 1rem; border-radius: 16px;"><strong>🎯 Smart Similarity</strong><br>Uses cosine similarity on combined metadata (genres, keywords, cast, crew).</div>
        <div style="background: #0b0f1c; padding: 1rem; border-radius: 16px;"><strong>🖼️ Live Posters</strong><br>Fetches high‑resolution posters from TMDB API.</div>
        <div style="background: #0b0f1c; padding: 1rem; border-radius: 16px;"><strong>🔗 Clickable Cards</strong><br>Each movie card links directly to its TMDB page.</div>
        <div style="background: #0b0f1c; padding: 1rem; border-radius: 16px;"><strong>📱 Responsive Grid</strong><br>Beautiful movie grid that adapts to any screen size.</div>
        <div style="background: #0b0f1c; padding: 1rem; border-radius: 16px;"><strong>⚡ Fast & Cached</strong><br>Data loading and poster fetching are cached for performance.</div>
        <div style="background: #0b0f1c; padding: 1rem; border-radius: 16px;"><strong>🎨 Custom UI</strong><br>Modern dark gradient design with smooth hover animations.</div>
    </div>
</div>

<!-- TECH STACK -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">🛠️ Tech Stack</h2>
    <ul style="columns: 2; column-gap: 2rem; list-style: none; padding-left: 0;">
        <li>🐍 <strong>Python</strong> – core logic</li>
        <li>📊 <strong>Streamlit</strong> – interactive web framework</li>
        <li>🤖 <strong>scikit‑learn</strong> – TF‑IDF vectorization & cosine similarity</li>
        <li>🐼 <strong>Pandas</strong> – data manipulation</li>
        <li>🎬 <strong>TMDb API</strong> – poster images & movie links</li>
        <li>📦 <strong>Pickle</strong> – serialization of similarity matrix & movie data</li>
        <li>☁️ <strong>Streamlit Cloud</strong> – deployment & hosting</li>
    </ul>
</div>

<!-- HOW IT WORKS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">🧠 How It Works</h2>
    <ol style="line-height: 1.7;">
        <li><strong>Data Preprocessing</strong> – The TMDB dataset (movies metadata) is cleaned in Jupyter Notebook. Features like genres, keywords, cast, and crew are combined into a single text "tags" column.</li>
        <li><strong>Vectorization</strong> – The tags are converted into numerical vectors using <strong>TF‑IDF Vectorizer</strong> (Term Frequency‑Inverse Document Frequency).</li>
        <li><strong>Similarity Computation</strong> – Cosine similarity is calculated between all movies, creating a <strong>similarity matrix</strong> (saved as <code>similarity.pkl</code>).</li>
        <li><strong>Recommendation Logic</strong> – When you select a movie, the app fetches its index, retrieves the most similar movies from the matrix (excluding itself), and returns top N results.</li>
        <li><strong>Frontend & API</strong> – Streamlit displays the results in a responsive grid. Each poster is fetched live from TMDB using the movie ID.</li>
    </ol>
</div>

<!-- INSTALLATION & RUN LOCALLY -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">💻 Run Locally</h2>
    <p>Follow these steps to get the project up and running on your machine.</p>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de;">
<code># 1. Clone the repository
git clone https://github.com/yourusername/ai-movie-recommender.git
cd ai-movie-recommender

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your TMDB API key
# Create a .env file in the root directory and write:
API=your_tmdb_api_key_here

# 5. Run the Streamlit app
streamlit run app.py
</code></pre>
    <p>🎯 The app will open at <code>http://localhost:8501</code></p>
</div>

<!-- FILE STRUCTURE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">📁 Project Structure</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto;">
📦 ai-movie-recommender
 ┣ 📜 app.py                 # Main Streamlit application
 ┣ 📜 movies_dict.pkl        # Serialized DataFrame (movie titles & IDs)
 ┣ 📜 similarity.pkl         # Precomputed cosine similarity matrix
 ┣ 📜 requirements.txt       # Python dependencies
 ┣ 📜 .env                   # TMDB API key (gitignored)
 ┗ 📜 README.md              # Project documentation
    </pre>
</div>

<!-- DEPLOYMENT ON STREAMLIT CLOUD -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">☁️ Deployment on Streamlit Cloud</h2>
    <p>The app is live at: <strong><a href="https://ai-movie-recommender-79jkgdcvpcsyi5uq4t9ept.streamlit.app" target="_blank" style="color: #ff8e8e;">https://ai-movie-recommender-79jkgdcvpcsyi5uq4t9ept.streamlit.app</a></strong></p>
    <p>To deploy your own version:</p>
    <ol>
        <li>Push your code to a <strong>GitHub repository</strong> (including <code>movies_dict.pkl</code>, <code>similarity.pkl</code>, and <code>app.py</code>).</li>
        <li>Go to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> and sign in with GitHub.</li>
        <li>Select your repo, branch, and main file (<code>app.py</code>).</li>
        <li>Add your <strong>secret</strong>: in the Streamlit Cloud dashboard → Settings → Secrets, add <code>API = "your_tmdb_api_key"</code>.</li>
        <li>Click <strong>Deploy</strong> 🚀</li>
    </ol>
</div>

<!-- FUTURE ENHANCEMENTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">🔮 Future Enhancements</h2>
    <ul>
        <li>✨ Hybrid recommendation system (collaborative + content‑based)</li>
        <li>✨ User ratings & “rate this movie” feature</li>
        <li>✨ Filter by genre, year, or language</li>
        <li>✨ Save favorite movies list (session state or database)</li>
        <li>✨ Add movie trailers (YouTube API)</li>
        <li>✨ Docker container for easy deployment</li>
    </ul>
</div>

<!-- CONTRIBUTING -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #ffd93d; margin-top: 0;">🤝 Contributing</h2>
    <p>Contributions, issues, and feature requests are welcome!<br>
    Feel free to check the <a href="#" style="color: #ff8e8e;">issues page</a> or submit a pull request.</p>
</div>

<!-- LICENSE & AUTHOR -->
<div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px; background: #0b0f1c; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <div>
        <h3 style="color: #ffd93d; margin: 0 0 8px 0;">📄 License</h3>
        <p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>
    </div>
    <div>
        <h3 style="color: #ffd93d; margin: 0 0 8px 0;">👤 Author</h3>
        <p><strong>Rehman Ahmad</strong><br>
        🔗 <a href="https://github.com/rehmanahmad" style="color: #ff8e8e;">GitHub</a> • 
        💼 <a href="https://www.linkedin.com/in/rehman-ahmad-9a5b17384/" style="color: #ff8e8e;">LinkedIn</a> • 
        📧 rahmanahmadcheema07@example.com</p>
    </div>
</div>

<!-- FOOTER -->
<div style="text-align: center; padding: 1.5rem 0; border-top: 1px solid #2a2f45; margin-top: 30px; color: #6f7a9e;">
    <p>Built with ❤️ using Streamlit & TMDB | © 2025 Rehman Ahmad</p>
</div>

</div>
</body>
</html>