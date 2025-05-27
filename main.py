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





