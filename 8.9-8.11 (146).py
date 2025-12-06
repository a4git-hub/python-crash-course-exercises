#8.9
#Make a list and pass the list to a function called show_messages(), which prints each message in the list
# msgs = ['Hello, world!', 'Python is fun.', 'I love coding.']

# def show_messages(messages):
#     for msg in messages:
#         print(msg)

# show_messages(msgs)

#8.10
#Start with a copy of your program from 8.9. Write a function called send _messages() that prints each message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

# msgs = ['Hello, world!', 'Python is fun.', 'I love coding.']
# def show_messages(messages):
#     for msg in messages:
#         print(msg)

# def send_messages(messages, sent_messages):
#     while messages:
#         current_msg = messages.pop(0)
#         print(current_msg)
#         sent_messages.append(current_msg)

# send_messages(msgs[:], [])  # Pass a copy of msgs to preserve the original list