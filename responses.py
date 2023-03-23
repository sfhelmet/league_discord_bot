import random

def handle_response(message):
    message = message.lower()

    if message == "hello":
        return "Hello there!"
    elif message == "roll":
        return str(random.randint(1, 6))
    elif message == "!help":
        return "`This is a code box`"
