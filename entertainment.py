import media
import fresh_tomatoes

toystory = media.Movie("ty title","ty story","https://en.wikipedia.org/wiki/File:Toy_Story.jpg","https://www.youtube.com/watch?v=NTdKQzVFeis")
movies = [toystory]
print(toystory.title)
fresh_tomatoes.open_movies_page(movies)
