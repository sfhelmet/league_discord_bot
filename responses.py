import random

def handle_response(message):
    p_message = message.lower()

    if p_message == "hello":
        return "Hello there!"
    elif p_message == "roll":
        return str(random.randint(1, 6))
    elif p_message == "!help":
        return "`This is a code box`"
    else:
        return "I don't understand."
