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