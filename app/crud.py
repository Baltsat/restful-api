from .database import get_db_connection
from .models import MovieCreate

def get_movies_from_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, year, director, length, rating FROM movies")
    movies = cursor.fetchall()
    conn.close()
    return [{"id": movie[0], "title": movie[1], "year": movie[2], "director": movie[3], "length": movie[4], "rating": movie[5]} for movie in movies]

def get_movie_by_id_from_db(movie_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, year, director, length, rating FROM movies WHERE id = ?", (movie_id,))
    movie = cursor.fetchone()
    conn.close()
    if movie:
        return {"id": movie[0], "title": movie[1], "year": movie[2], "director": movie[3], "length": movie[4], "rating": movie[5]}
    else:
        return None

def add_movie_to_db(movie: MovieCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, year, director, length, rating) VALUES (?, ?, ?, ?, ?)",
                   (movie.title, movie.year, movie.director, movie.length, movie.rating))
    conn.commit()
    movie_id = cursor.lastrowid
    conn.close()
    return movie_id

def delete_movie_from_db(movie_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    changes = cursor.rowcount
    conn.commit()
    conn.close()
    return changes
