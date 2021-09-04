import Movie
import urllib.request
import re


class YouTubeConnectorWrapper:
    @classmethod
    def get_trailer_url(cls, movie: Movie)-> str:
        search = movie + ' trailer'
        #search = movie.title + ' trailer'
        search_words = list(search.split(" "))
        query = "+".join(str(x) for x in search_words)
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+query)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        trailer_url = "https://www.youtube.com/watch?v=" + video_ids[0]
        return trailer_url


#YouTubeConnectorWrapper.get_trailer_url(Movie.Movie("movie1", "9.5", ["comedy", "action"]))
