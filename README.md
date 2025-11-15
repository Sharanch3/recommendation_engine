## 🚀 Project Overview
The goal of this system is to analyze both **textual** and **categorical** movie metadata to understand how similar films are to each other—and then recommend the closest matches.
This is achieved through **feature engineering**, **NLP-based vectorization**, and **cosine similarity** computed over **high-dimensional vectors**.

---

**🌐 Demo:** https://recommendationengine-101.streamlit.app/

---

## 🧠 What the System Does

### 🔹 1. Unified Metadata Pipeline

A combined textual representation was engineered by merging:

* **Genres**
* **Keywords**
* **Cast**
* **Crew**
* **Overview**

This produces a rich, descriptive **contextual fingerprint** for every movie.

---

### 🔹 2. Vectorization Using NLP

The unified text was transformed into numerical vectors using:

* **TF–IDF Vectorizer**
* **CountVectorizer**

These methods produce **efficient**, **sparse**, and **high-dimensional** matrices ideal for similarity computation.

---

### 🔹 3. Cosine Similarity Computation

Cosine similarity was applied to all movie vectors to quantify **movie-to-movie closeness** within the feature space.

---

### 🔹 4. Recommendation Engine

For any given movie, the system:

1. Retrieves its vector
2. Compares it against all other movie vectors
3. Sorts similarity scores in descending order
4. Returns the **Top 5 most similar movies**

---

### 🔹 5. Large-Scale Optimization

To ensure performance on thousands of movies, the system uses:

* **Sparse vector representations**
* **Optimized similarity lookup**
* **Elimination of redundant computation**

---



