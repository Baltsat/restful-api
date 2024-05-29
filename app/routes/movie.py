from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Movie, MovieCreate
from ..crud import get_movies_from_db, get_movie_by_id_from_db, add_movie_to_db, delete_movie_from_db

router = APIRouter()

@router.get("/api/movies", response_model=List[Movie])
def get_movies():
    movies = get_movies_from_db()
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found")
    return movies

@router.get("/api/movies/{id}", response_model=Movie)
def get_movie_by_id(id: int):
    movie = get_movie_by_id_from_db(id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/api/movies", response_model=Movie, status_code=201)
def create_movie(movie: MovieCreate):
    movie_id = add_movie_to_db(movie)
    new_movie = get_movie_by_id_from_db(movie_id)
    return new_movie

@router.delete("/api/movies/{id}", status_code=202)
def delete_movie(id: int):
    changes = delete_movie_from_db(id)
    if changes == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"status": 202, "message": "Movie deleted successfully"}
