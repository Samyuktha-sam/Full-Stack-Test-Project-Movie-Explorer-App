from fastapi import APIRouter, Depends ,HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models import Movie
from app.schemas import MovieCeate, MovieUpdate, MovieResponse

router = APIRouter(prefix="/movies", tags=["movies"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MovieResponse)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

               
@router.get("/", response_model=List[MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return movies

@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.put("/{movie_id}", response_model=MovieResponse )
def update_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in movie.dict(exclude_unset=True).items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(db_movie)
    db.commit()
    return {"detail": "Movie deleted successfully"}
