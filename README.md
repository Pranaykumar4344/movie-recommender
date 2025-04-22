
# 🎬 Movie Recommendation System

A smart and simple **Movie Recommendation System** built with **Streamlit** and powered by **cosine similarity** using TMDB's 5000 Movies & Credits dataset.

> ✨ Find similar movies, discover new favorites, and explore movie details – all in a sleek UI!

---

## 🌟 Features

- 🔍 **Search a movie** and get top 10 similar recommendations
- 🎥 Includes **title, language, release date, cast**, and **description**
- 💬 Smart fallback if user misspells a movie name
- 📱 Sleek and responsive **Streamlit-based UI**
- 📦 Easy to deploy and use!

---

## 🖼️ UI Preview
![UI Preview of Movie Recommendation System](image.png)


---

## 🧠 How it works

- The app loads a **pickled movie dataset** and **cosine similarity matrix**
- When you search a movie, it matches the name (even partial)
- Recommends the **top 10 most similar movies**
- Display movie details in a clean and minimal layout

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**, **Scikit-learn**
- **Streamlit**
- **TMDB 5000 Movies Dataset**

---

## 📂 Project Structure

```
movie-recommender/
│
├── app.py                 # Streamlit app code
├── requirements.txt       # All Python dependencies
└── README.md              # You're reading it!
```

---

## ⚙️ Installation (Local)

1. Clone the repository

```bash
git clone https://github.com/Pranaykumar4344/movie-recommender.git
cd movie-recommender
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment on Streamlit Cloud

1. Push your project to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Choose `app.py` as the main file
5. Done! 🎉

---

## 📊 Dataset Info

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Originally available from Kaggle:
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 🙋‍♂️ Author

**J Pranay Kumar **  
📧 JPranaykumar1205@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/pranay-kumar-5897a828a/)

---

## ⭐️ Show Your Support

If you found this helpful:

🌟 Give it a star on [GitHub](https://github.com/Pranaykumar4344/movie-recommender)  
📣 Share with your friends  
✏️ Fork and improve it!
