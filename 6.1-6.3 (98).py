#6.1
#Store information about someone in a dictionary and print each piece of information.
# info = {'age': 15, 'name': 'Aditya', 'last_name': 'Singh', 'city': 'San Ramon'}
# print(info['name'])

#6.2
#Store different people's favorite numbers and print their name and favorite number

# favorite_number = {'bob': 4, 'david': 7, 'rob': 4}

# print('bob:', favorite_number['bob'])

#6.3
#Make a glossary with terms and definitions of words and fuctions you've learned from previosu chapters in Python

dictionary = {
    'if statement': 'a conditional to do something if if a certain condition is true',
    'boolean': 'a true or false condition',
    'for loop': 'a loop that checks if a condition is true and repeats until user commands to break'   
}
              
for Syntax, Definition in dictionary.items():
    print(f"\nSyntax: {Syntax}") 
    print(f"Definition: {Definition}")



# print('If statement:', dictionary['if statement'])



