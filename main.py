import os

import httpx
import sqlalchemy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Database setup
DATABASE_URL = "sqlite:///./movies.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

# External OMDb API configuration
OMDB_API_URL = os.getenv("OMDB_API_URL", "http://www.omdbapi.com/")
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "8ab5255f")
DEFAULT_MOVIE_ID = os.getenv("DEFAULT_MOVIE_ID", "tt3896198")

@app.get('/movie')
async def get_movie_resource(movie_id: str = DEFAULT_MOVIE_ID):
    """Fetch a movie from OMDb using the configured endpoint and API key."""
    params = {
        "i": movie_id,
        "apikey": OMDB_API_KEY,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(OMDB_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    