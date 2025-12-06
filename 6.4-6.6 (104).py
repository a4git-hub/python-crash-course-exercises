#6.4
#Clean up the code from previous exercise 6.3 by replacing print calls with a loop and add 5 more definitions

# dictionary = {
#     'if statement': 'a conditional to do something if if a certain condition is true',
#     'boolean': 'a true or false condition',
#     'for loop': 'a loop that checks if a condition is true and repeats until user commands to break',
#     'list': 'a list of items that you can access',
#     'dictionary': 'like a list, except has key-value pairs',
#     'variable': 'character or integer that represents something'   
# }
              
# for k, v in dictionary.items():
#     print(f"\nSyntax: {k}") 
#     print(f"Definition: {v}")

#6.5
#Make a dictionary containing 3 major rivers and the country they run through
#Use a loop to print a sentence about each river "The Nile runs through Egypt"
#Loop through the name of each river in the dictionary
#Loop through to print the name of each country

# rivers = {'nile': 'egypt', 'yellow': 'china', 'amazon': 'brazil'}

# for river, country in rivers.items():
#     print(f"The {river.title()} River runs through {country.title()}.")

# for river in rivers:
#     print(river.title())

# for country in rivers.values():
#     print(country.title())

#6.6
#Make a list of  people who should take the favorite languages poll
#Loop through the list, if they have already taken the poll, print a message for them, and same for if not

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }

taken = ['jen', 'sarah', 'edward', 'phil']

poll = ['jen', 'sarah', 'edward', 'roy', 'david']

for index in poll:
    if poll in taken:
        print(f"Thank you {poll} for taking the survery")
    else:
        print(f"{poll}, please take the servey!")