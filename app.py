import streamlit as st
import pickle
import pandas as pd
import gdown
import os

# Define a function to download files from Google Drive
def download_file_from_drive(file_id, output_path):
    gdown.download(f'https://drive.google.com/uc?id={file_id}', output_path, quiet=False)

# Define a method to load models
def load_models():
    # Check if models are already downloaded
    if not os.path.exists('movies.pkl'):
        st.write("Downloading movies dataset...")
        download_file_from_drive('1WQH3qCJmNnsaGVSc_UbCvp0Q6RRcUtNI', 'movies.pkl')
        
    if not os.path.exists('cosine_sim.pkl'):
        st.write("Downloading cosine similarity matrix...")
        download_file_from_drive('1PcVujSke6rTNnhBKqHz237fk9AXkY55m', 'cosine_sim.pkl')

    movies = pickle.load(open('movies.pkl', 'rb'))  # Movies dataset
    similarity = pickle.load(open('cosine_sim.pkl', 'rb'))  # Similarity matrix (cosine similarity)

    return movies, similarity

# Load the pre-trained movie model and similarity data
movies, similarity = load_models()

# Function to recommend movies based on the user's search input
def recommend_movies(search_query):
    # Search the movies that match the user's query
    search_query = search_query.lower()
    movie_indices = movies[movies['title'].str.lower().str.contains(search_query)].index.tolist()

    # If there are no movies that match, return a message
    if not movie_indices:
        return "No matching movies found."

    recommendations = []
    
    # Get the top 10 most similar movies based on cosine similarity
    for idx in movie_indices:
        similarity_scores = list(enumerate(similarity[idx]))
        sorted_similarities = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:11]  # top 10
        for movie_idx, score in sorted_similarities:
            recommendations.append({
                'title': movies['title'].iloc[movie_idx],
                'overview': movies['overview'].iloc[movie_idx],
                'release_date': movies['release_date'].iloc[movie_idx],
                'language': movies['original_language'].iloc[movie_idx]
            })

    return recommendations

# Streamlit app layout
st.title("Movie Recommendation System")
st.write("Enter a movie title to get recommendations")

# User input: search query
search_query = st.text_input("Search for a movie:")

# Suggestion button
if st.button('Get Recommendations'):
    if search_query:
        results = recommend_movies(search_query)
        if isinstance(results, list):
            for idx, movie in enumerate(results):
                st.write(f"**{movie['title']}**")
                st.write(f"Release Date: {movie['release_date']}")
                st.write(f"Language: {movie['language']}")
                st.write(f"Description: {movie['overview']}")
                st.write("---")
        else:
            st.write(results)  # If no matches found
    else:
        st.write("Please enter a movie title to search.")

# Suggest similar movies if no result is found
if not search_query:
    st.write("Please enter a movie title to search.")
