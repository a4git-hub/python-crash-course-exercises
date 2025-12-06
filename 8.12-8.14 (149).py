#8.12
#Write a function that accepts a list of items a person wants on a sandwich. The function should have one
#parameter that collects as many items as the function call provides, and it should print a summary
#of the sandwich that is being ordered. Call the function three times, using a different number
#of arguments each time.

# def make_sandwich(*items):
#     print("You have ordered a sandwich with the following items:")
#     for item in items:
#         print(f"-{item.title()}")

# make_sandwich('ham', 'cheese', 'lettuce')

#8.13
#Start with copy of program on page 148. Build a profile of yourself by calling build_profile(),
#using your first and last names and three other key-value pairs that describe you.

# def build_profile(first, last, **build_info):
#     build_info['first_name']= first
#     build_info['last_name']= last
#     return build_info

# my_profile = build_profile('Aditya', 'Singh', location='India', field='Computer Science', hobby='Reading')
# print(my_profile)

#8.14
#Write a function that stores information about a car in a dictionary. The function should always
#receive a manufacturer and a model name. It should then accept an arbitrary number of keyword
#arguments. Call the function with the required information and two other name-value pairs, such
#as a color or an optional feature.

def car_info(manafactuerer, model, **car_specs):
    car_specs['manafactuerer'] = manafactuerer
    car_specs['model'] = model
    return car_specs

my_car = car_info('Lexus', 'TX', color='Black', year=2025, sunroof = 'True',)
print(my_car)