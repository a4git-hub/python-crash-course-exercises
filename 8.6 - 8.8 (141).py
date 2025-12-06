#8.6
#Write a function that takes in the anme of a city and its country the function returns a string

# def city_country(city, country):
#     full_name = f"{city.title()}, {country.title()}"
#     return full_name

# x = city_country('san ramon', 'united states')
# print(x)

# y = city_country('san diego', 'united states')
# print(y)

# z = city_country('delhi', 'india')
# print(z)

#8.7
#Make a functiont aht returns a dictionary desscribing a music album. Use None as an optional parameter of the # of songs in the album

# def make_album(artist_name, album_title, num_of_songs = None):
#     album = {'artist': artist_name, 'album': album_title}
#     if num_of_songs:
#         album['num_of_songs'] = num_of_songs
#     return album

# cool_album = make_album('aditya', 'fein', num_of_songs=15)
# print(cool_album)

#8.8
#Same thing as 8.7 but integrate a while loop and store values in a dictionary

# def make_album():
#     while True:
#         artist = input("Enter the album's artist (press q to quit): ")
#         if artist == 'q':
#             break
#         title = input("Enter the album's title: ")
#         album = {'Album Artist': artist, 'Title': title}
#         print(album)

# make_album()
