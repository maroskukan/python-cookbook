current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christmas Vacation': '5:00pm'
}

print("We're showing the following movies:\n")
for movie in current_movies:
    print(f"\U0001f3ac {movie}")

movie = input('\nWhat movie would you like to showtime for?\n')

showtime = current_movies.get(movie)

if showtime:
    print(f"\n{movie} is playing at {showtime}")
else:
    print(f"\nSorry, we are not playing {movie} at the moment.")
