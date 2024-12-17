favorite_movies = [
    {"name": "The Lion King", "year": 1994},
    {"name": "Aladdin", "year": 1992},
    {"name": "Beauty and the Beast", "year": 1991},
    {"name": "Frozen", "year": 2013},
    {"name": "Moana", "year": 2016},
    {"name": "Toy Story", "year": 1995},
    {"name": "Zootopia", "year": 2016},
    {"name": "Interstellar", "year": 2014}
]

def check_movie_release(movie):
    if movie["year"] < 2000:
        print(f"{movie['name']} was released before 2000.")
    else:
        print(f"{movie['name']} was released after 2000.")
        return movie["name"]  
    return None  

recent_movies = []

for movie in favorite_movies:
    result = check_movie_release(movie)
    if result is not None:
        recent_movies.append(result)

print("\nMovies released after 2000:")
print(recent_movies)
