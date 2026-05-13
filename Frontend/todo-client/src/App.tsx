import { useState } from 'react'
import './App.css'
import SearchBar from './components/SearchBar'
import MovieCard from './components/MovieCard'
import SavedMoviesList from './components/SavedMoviesList'

type Movie = {
  id: string
  poster: string
  title: string
  genre: string
  rating: string
  plot: string
}

const sampleMovie: Movie = {
  id: '1',
  poster: 'https://via.placeholder.com/240x360?text=Movie+Poster',
  title: 'The Adventure Begins',
  genre: 'Action, Adventure',
  rating: '8.2',
  plot: 'A young hero sets off on a thrilling journey to save the city and uncover buried secrets.',
}

const savedMovies: Movie[] = [
  {
    id: '2',
    poster: 'https://via.placeholder.com/120x180?text=Saved+Movie',
    title: 'Moonlight Journey',
    genre: 'Drama, Sci-Fi',
    rating: '7.8',
    plot: 'A daring astronaut discovers what it means to belong on a mission across the stars.',
  },
  {
    id: '3',
    poster: 'https://via.placeholder.com/120x180?text=Saved+Movie',
    title: 'City of Dreams',
    genre: 'Romance, Comedy',
    rating: '8.0',
    plot: 'Two strangers find unexpected love while chasing their ambitions in a busy city.',
  },
]

function App() {
  const [query, setQuery] = useState('')

  function handleSearch() {
    console.log('Searching for:', query)
  }

  return (
    <main className="app-shell">
      <header className="hero-banner">
        <div>
          <h1>Movie Explorer</h1>
          <p>Search for films and keep track of favourites in one place.</p>
        </div>
        <SearchBar query={query} onQueryChange={setQuery} onSearch={handleSearch} />
      </header>

      <section className="featured-movie">
        <h2>Featured Movie</h2>
        <MovieCard
          poster={sampleMovie.poster}
          title={sampleMovie.title}
          genre={sampleMovie.genre}
          rating={sampleMovie.rating}
          plot={sampleMovie.plot}
        />
      </section>

      <SavedMoviesList movies={savedMovies} />
    </main>
  )
}

export default App
