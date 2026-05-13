type SearchBarProps = {
  query: string
  onQueryChange: (value: string) => void
  onSearch: () => void
}

export default function SearchBar({ query, onQueryChange, onSearch }: SearchBarProps) {
  return (
    <div className="search-bar">
      <input
        type="search"
        placeholder="Search movies by title, genre or keyword"
        value={query}
        onChange={(event) => onQueryChange(event.target.value)}
        aria-label="Search movies"
      />
      <button type="button" onClick={onSearch}>
        Search
      </button>
    </div>
  )
}
