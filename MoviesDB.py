import random

import Movie
from tinydb import TinyDB, Query


class MoviesDBWrapper:
    DB_PATH: str = 'movies_data_base.jason'
    DB: TinyDB = TinyDB(DB_PATH)

    @classmethod
    def movies_by_genre(cls, genres: list, limit: int = 10) -> list[Movie.Movie]:
        item = Query()
        movies = MoviesDBWrapper.DB.search(item.genres.all(genres))
        index = random.randrange(0, len(movies) - limit)
        movies = movies[index:index + limit]
        result = []
        for movie in movies:
            result.append(MoviesDBWrapper.__to_movie(movie))
        return result

    @classmethod
    def top_n_movies(cls, n: int = 10) -> list[Movie]:
        return [Movie.Movie("movie1", "9.5", ["comedy", "action"]), Movie.Movie("movie2", "9.1", ["fantasy", "action"])]

    @classmethod
    def movies_by_situations(cls, situation: str) -> list[Movie]:
        if situation == "Friends":
            return MoviesDBWrapper.movies_by_genre(['Comedy', 'Action', 'Adventure'])
        if situation == "Family":
            return MoviesDBWrapper.movies_by_genre(['Animation', 'Comedy', 'Adventure'])

    @classmethod
    def insert(cls, movie: Movie):
        MoviesDBWrapper.DB.insert({'title': movie.title, 'rating': movie.rating, 'genres': movie.genres})

    @classmethod
    def __to_movie(cls, data: dict) -> Movie:
        return Movie.Movie(data["title"], data["rating"], data["genres"])


print(MoviesDBWrapper.movies_by_genre(['Drama']))
