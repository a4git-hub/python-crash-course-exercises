#7.4 Pizza Toppings
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' valu.
#As they enter each topping, print a message saying you'll add that topping to their pizza

# prompt = "Enter a topping for your pizza (Enter 'quit' to exit) "

# while True:
#     toppings = input(prompt)

#     if toppings == 'quit':
#         break
#     else: print(f"Sure, I'll add {toppings}")

#7.5 Movie Tickets:
#Asks user for age using while loop, based on that, prices change

# age = "Enter your age: "

# while True:
#     value = int(input(age))

#     if value < 3:
#         print("Your ticket is free!")
    
#     elif value <= 12:
#         print("Your ticket is $10.")

#     elif value > 12:
#         print("Your ticket is $15.")
    
#     else:
#         print("Please enter a valid age number.")

#7.6 Three exits
#Write different versions of either Exercise 7.4-7.5 that do each of the folowing at least once:
# - Use a conditional test in the while stament to stop the loop
# - Use an active variable to control how long the loop runs
# - Use a break statement to exit the loop when the users enters a 'quit' value

# Altering 7.5 exercise

age = "Enter your age: "

while True:
    value = int(input(age))

    if value < 3:
        print("Your ticket is free!")
    
    elif value <= 12:
        print("Your ticket is $10.")

    elif value > 12:
        print("Your ticket is $15.")
    
    else:
        print("Please enter a valid age number.")