# Functions go here

def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error)
            print()

# Main Routine
name = not_blank("What is your name? ", "Sorry - this can't be blank, please enter your name")