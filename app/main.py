from fastapi import FastAPI
from .database import initialize_db, add_sample_movies
from .routes import movie

app = FastAPI()

app.include_router(movie.router)

initialize_db()
add_sample_movies()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)