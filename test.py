from tools import search_movies

results = search_movies(
    "dark sci-fi movies on a spaceship"
)

for movie in results:
    print(movie["title"])