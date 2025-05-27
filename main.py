import streamlit as st
from ScriptSquad_1_LibraryCatalog import (
    add_book, search_by_author, search_by_genre,
    books_by_year, genre_summary, catalog
)

st.title("📚 Library Catalog App")

st.header("Add a New Book")

with st.form("add_book_form"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Year (4 digits)")
    genres = st.text_input("Genres (comma-separated)")

    submitted = st.form_submit_button("Add Book")
    if submitted:
        genre_list = [g.strip() for g in genres.split(",") if g.strip()]
        success = add_book(title, author, year, genre_list)
        if success:
            st.success(f"Book '{title}' by {author} added!")
        else:
            st.error("Failed to add book. Check title/year format or duplicate entry.")

st.header("Search Books")

search_type = st.radio("Search by:", ["Author", "Genre", "Year"])

query = st.text_input("Enter your search term")

if st.button("Search"):
    if search_type == "Author":
        results = search_by_author(query)
    elif search_type == "Genre":
        results = search_by_genre(query)
    else:
        results = books_by_year(query)

    if results:
        st.write(f"Found {len(results)} book(s):")
        for book in results:
            st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) — Genres: {', '.join(book['genres'])}")
    else:
        st.write("No books found.")

st.header("Genre Summary")
summary = genre_summary()
if summary:
    for genre, count in summary.items():
        st.write(f"- {genre}: {count} book(s)")
else:
    st.write("No books in the catalog yet.")






import re

catalog = []

def is_valid_year(year_str):
    return re.match(r'^\d{4}$', year_str) is not None

def is_valid_title(title):
    return re.match(r"^[\w\s.,!?':;-]+$", title) is not None

def add_book(title, author, year, genres):
    for book in catalog:
        if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
            return False
    if not (is_valid_year(year) and is_valid_title(title)):
        return False
    catalog.append({
        'title': title,
        'author': author,
        'year': int(year),
        'genres': genres
    })
    return True

def search_by_author(author_name):
    return [
        book for book in catalog
        if author_name.lower() in book['author'].lower()
    ]

def search_by_genre(genre_name):
    return [
        book for book in catalog
        if any(genre_name.lower() in genre.lower() for genre in book['genres'])
    ]

def books_by_year(year):
    return [
        book for book in catalog
        if book['year'] == int(year)
    ]

def genre_summary():
    summary = {}
    for book in catalog:
        for genre in book['genres']:
            genre = genre.strip()
            summary[genre] = summary.get(genre, 0) + 1
    return summary
