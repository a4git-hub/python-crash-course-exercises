# sports = 'basketball'

# print("Guess the sport!")
# print("Is the sport soccer?")
# print(sports == 'soccer')

# print("Try Again!")
# print("Is the sport basketball? I think it is.")
# print(sports == 'basketball')




print("Please choose a username.")
username = (input("Enter your username: "))
if username == 'a4gaming':
    print("Sorry, that username is already in use. Please use another.")
    input("Enter your new username: ")
else:
    print("Continue with the registration.")
    
email = input("Please enter your email: ")
str1 = '@gmail.com'
index = email.find(str1)
if index != -1:
    print("The next part is confirming your age")
else:
    print("Enter a vaid email address.")
    input("Please enter your email: ")

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to register.")
else:
    print("Sorry, you are not old enough to register.")
captcha = input("If you think this is a mistake, please enter the captcha sent to your email address: ")
if captcha == 'Td4eva':
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("Your account has been made.")
    else: 
        print("Sorry, you have reached the maximum amount of tries to register.")
else:print("Sorry, you have reached the maximum amount of tries to register.")




