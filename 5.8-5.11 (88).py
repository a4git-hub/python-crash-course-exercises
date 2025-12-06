# 5.8:
# usernames = ['admin', 'jaden', 'alex', 'steve']
# input("Please enter username: ")
# if usernames == 'admin':
#      print("Hello admin, would you like to see a status report?")
# else:
#      print("Hello user, thank you for logging in again.")

#5.9
# users = []
# inputs = input("Please enter your username: ")
# if inputs == '':
#      print("Please enter a username: ")
     
# else:
#      print("Welcome back")
#      users.append(inputs)
# print("List length: ", inputs)

#5.10

current_users = ['John', 'Bob', 'Jack', 'Lily', 'Muhammed']
current_user_lower = ['john', 'bob', 'jack', 'lily', 'muhammed']
current_users_upper = ['JOHN', 'BOB', 'JACK', 'LILY', 'MUHAMMED']

availible_users = ['Thomas', 'Henry', 'Ladadee']

inputs = input("Please enter your username: ")
if inputs in current_users:
    print(f"Sorry, {inputs} is already in use.")
    input("Please enter new username: ")
    print(f"The username {availible_users} are/is available.")

if inputs in current_user_lower:
    print(f"Sorry, you can not use {inputs} as it is similar to a used username")
    input("Please enter new username: ")
    print(f"The username {availible_users} are/is available.")
if inputs in current_users_upper:
    print(f"Sorry, you can not use {inputs} as it is similar to a used username")
    input("Please enter new username: ")
    print(f"The username(s) {availible_users} are/is available.")
else: 
    print("You have selected a username.")
        