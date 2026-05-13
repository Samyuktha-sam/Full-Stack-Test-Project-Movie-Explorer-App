type SavedMovie = {
  id: string
  poster: string
  title: string
  genre: string
  rating: string
  plot: string
}

type SavedMoviesListProps = {
  movies: SavedMovie[]
}

export default function SavedMoviesList({ movies }: SavedMoviesListProps) {
  if (movies.length === 0) {
    return <div className="saved-movies-empty">No saved movies yet.</div>
  }

  return (
    <section className="saved-movies-list">
      <h3>Saved Movies</h3>
      <div className="saved-movies-grid">
        {movies.map((movie) => (
          <article className="saved-movie" key={movie.id}>
            <img src={movie.poster} alt={`${movie.title} poster`} />
            <div>
              <h4>{movie.title}</h4>
              <p>{movie.genre}</p>
              <p>{movie.rating}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  )
}
