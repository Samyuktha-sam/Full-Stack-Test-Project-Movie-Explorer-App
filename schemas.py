from pydantic import BaseModel

class Movie (baseModel):
    title: str
    year: int
    genre: str
    imdb_rating: int
    poster_url: str
    plot: str

    class MovieCreate (BaseModel):
        pass
    class MovieUpdate (BaseModel):
        pass
    class MovieResponse (BaseModel):
        id: int

    class Config:
        orm_mode = True