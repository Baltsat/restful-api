import sqlite3

def get_db_connection():
    conn = sqlite3.connect('movies.db')
    return conn

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            director TEXT NOT NULL,
            length TEXT NOT NULL,
            rating INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_sample_movies():
    conn = get_db_connection()
    cursor = conn.cursor()
    sample_movies = [
        (1, "Example movie 1", 2018, "Somebody", "02:30:00", 8),
        (2, "Example movie 2", 2020, "Anyone", "01:45:00", 7)
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO movies (id, title, year, director, length, rating) VALUES (?, ?, ?, ?, ?, ?)",
        sample_movies)
    conn.commit()
    conn.close()