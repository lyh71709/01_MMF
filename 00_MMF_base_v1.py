# import statements


# functions go here
# not_blank function here
def not_blank(question, error):
    valid = False

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


# Main rountine

# Set up dictionaries / lists needed to hold data
MAX_TICKETS = 5
name = ""
ticket_count = 0
ticket_sales = 0

# Ask user for if they have used the program before and show how to use it

# Loop to get ticket details

# Get name (can't be blank)
while name != "xxx" and ticket_count < MAX_TICKETS:

    # Makes sure there is no plural when there is 1 ticket left
    if MAX_TICKETS - ticket_count == 1:
        print("There is 1 seat left")
    else:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    # Get details
    name = not_blank("What is your name? ", "Sorry - this can't be blank, please enter your name")
    # Makes xxx not ticket_count as a ticket sold
    if name == "xxx":
        print()
        break

    # Get age (between 12 and 130)
    age = int_check("How old are you? ")

    # check valid age
    if age < 12:
        print("Sorry you are too young for this movie")
        print()
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        print()
        continue

    # Calculate ticket price
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    print("{} : ${:.2f} \n".format(name, ticket_price))

    ticket_count += 1
    ticket_sales += ticket_price

# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)


# Gives feedback after loop has ended
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
    print("Profit from Tickets: ${:.2f}".format(ticket_profit))
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if needed)

# Output data to text file

