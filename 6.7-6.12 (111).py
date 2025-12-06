# 6.7
# Use code you used in 6.1 except make 2 new dictionaries and store the 3 dictionaries in a list and loop through it

# person_1 = {
#     'age': 15,
#     'first': 'Aditya',
#     'last_name': 'Singh'
# }

# person_2 = {
#     'age': 7,
#     'first': 'Arjun',
#     'last_name': 'Singh'
# }

# person_3 = {
#     'age': 47,
#     'first': 'Bhupender',
#     'last_name': 'Singh'
# }

# info = [person_1, person_2, person_3]

# for infos in info:
#     print(infos)

#6.8
#Same thing as last exercise except with pets

# pet_1 = {
#     'name': 'bob',
#     'type': 'dog'
# }

# pet_2 = {
#     'name': 'ryan',
#     'type': 'cat'
# }

# pet_3 = {
#     'name': 'adi',
#     'type': 'parrot'
# }

# pets = [pet_1, pet_2, pet_3]

# for pet in pets:
#     for key, value in pet.items():
#         print(f"{key.title()}: {value.title()}")
#     print()
    
#6.9
#same thing as last time basically except more than one value per key

# favorite_places = {
#     'bob': ['maldives', 'usa'],
#     'dan': ['india'],
#     'ron': ['argentina', 'russia', 'china']
# }

# for name in favorite_places:
    # for key, value in places.items():
        # print(f"{key.title()}'s favorite places are {value}.")
    # print(f"Favorite places for {name}: ")
    # for place in favorite_places[name]:
    #     print(place)

#6.10 
#Same thing except modifying excercise 6.2 so each person has more than one favorite number

# favorite_number = {'bob': [4, 3], 'david': [7, 2, 9], 'rob': [1, 6, 5]}

# for key, value in favorite_number.items():
#     print(f"{key.title()}'s favorite number are {value}")


#6.11
#Make a dictionary called cities and store information

nyc_info = {
    'country': 'usa',
    'population': '8.478 million',
    'fact': 'its the most linguistically diverse city in the world'
}

la_info = {
    'country': 'usa',
    'population': '3.879 million',
    'fact': 'Los Angeles County is the first in the nation to reach 10 million residents'
}

new_delhi_info = {
    'country': 'india',
    'population': '33.8 million',
    'fact': 'is the capital of india'
}

cities = {
    'nyc': nyc_info,
    'la': la_info,
    'new delhi': new_delhi_info
}

print(cities)