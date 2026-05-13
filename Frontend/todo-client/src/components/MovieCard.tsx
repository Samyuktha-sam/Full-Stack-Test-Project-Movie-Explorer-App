type MovieCardProps = {
  poster: string
  title: string
  genre: string
  rating: string
  plot: string
}

export default function MovieCard({ poster, title, genre, rating, plot }: MovieCardProps) {
  return (
    <article className="movie-card">
      <div className="movie-card__poster">
        <img src={poster} alt={`${title} poster`} />
      </div>
      <div className="movie-card__content">
        <h2>{title}</h2>
        <p className="movie-card__meta">
          <strong>Genre:</strong> {genre}
        </p>
        <p className="movie-card__meta">
          <strong>Rating:</strong> {rating}
        </p>
        <p className="movie-card__plot">{plot}</p>
      </div>
    </article>
  )
}
