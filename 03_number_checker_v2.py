# function goes here

def int_check(question):

    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine
age = int_check("How old are you? ")
