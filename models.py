from sqlalchemy import Column, Integer, String
from database import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer, index=True)
    genre = Column(String, index=True)
    imdb_rating = Column (Integer, index=True)
    poster_url = Column(String, index=True)
    plot = Column(String, index=True)
    created_at = Column(DateTime, index=True)
    