# import statements
import re
import pandas

# functions go here


# not_blank function here
def not_blank(question):
    valid = False
    error = "Sorry - this can't be blank, please enter your name"

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error)
            print()


# int_check function here
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


# check_tickets function here
def check_tickets(ticket_sold, ticket_limit):

    # Makes sure there is no plural when there is 1 ticket left
    if MAX_TICKETS - ticket_count == 1:
        print("!!!  There is 1 seat left    !!!")
    else:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    return ""


# get_ticket_price function here
def get_ticket_price():

    # Get age (between 12 and 130)
    age = int_check("How old are you? ")

    # check valid age
    if age < 12:
        print("Sorry you are too young for this movie\n")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake\n")
        return "invalid ticket price"

    # Calculate ticket price
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price

# Main routine

# Set up dictionaries / lists needed to hold data
MAX_TICKETS = 5
name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# Get name (can't be blank)
while name != "xxx" and ticket_count < MAX_TICKETS:

    check_tickets(ticket_count, MAX_TICKETS)

    # Get details
    name = not_blank("What is your name? ")
    # Makes xxx not ticket_count as a ticket sold
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()
    # If age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # Add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks

    # Get payment method (ie: work out if surcharge is needed

# End of tickets / snacks / payment loop

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
print()
print(movie_frame)

# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("\nProfit from Tickets: ${:.2f}".format(ticket_profit))

# Gives feedback after loop has ended
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))
