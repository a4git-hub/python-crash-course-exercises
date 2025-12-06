# alien_color = ['green', 'blue', 'red']
# alien_color = input("Choose a color (Green, Red, or Blue): ")
# if alien_color == 'green':
#     print("You have earned 5 points.")
#     alien_color = input("Choose a color (Green, Red, or Blue): ")
# if alien_color == 'red':
#     print("You have earned 10 points.")
#     alien_color = input("Choose a color (Green, Red, or Blue): ")
# if alien_color == 'blue':
#     print("You have earned 15 points.")
#     alien_color = input("Choose a color (Green, Red, or Blue): ")
# else:
#     print("That is not a valid response.")



age = int(input("Enter your age: "))

if age < 0:
    print("You must be joking 😆.")
elif age <= 2:
    print("You are a baby.")
elif age <= 4:
    print("You are a toddler.")
elif age <= 12:
    print("You are a kid.")
elif age <= 17:
    print("You are a teenager.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are an elder.")
