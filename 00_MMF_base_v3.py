# import statements
import re
import pandas

# functions go here

# get_snack function goes here


# Gets list of snacks
def get_snack():

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list
    # with valid options for each snack <full name,
    # letter code (a - e), and possible abbreviations etc>

    # Has all valid snacks that a user can get
    valid_snacks = [["bPopcorn", "popcorn", "p", "corn", "a"],
                    ["eM&Ms", "M&M's", "m&m's", "mms", "m", "b"],
                    ["dPita Chips", "pita chips", "chips", "pc", "pita", "c"],
                    ["cWater", "water", "w", "d"],
                    ["fOrange Juice", "orange juice", "oj", "o", "juice", "e"]]

    # holds snack order fpr a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []
        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # Check that snack is vaild
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack  # Can't argue with that

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_checker(desired_snack, valid_snacks)
        print(snack_choice)

        if amount >= 5:
            print("Sorry - we have a four snack limit")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # add snack and amount to list
        amount_snack = "{} {}".format(amount, snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


# string_checker function goes here
def string_checker(choice, options):
    for var_list in options:

        # if the snack is in one of the lists, return the full list
        if choice in var_list:

            # Get full name of snack and put it in title case
            # so it looks nice when out putted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set snack_ok to no
        else:
            is_valid = "no"

    # If snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option\n")
        return "invalid choice"


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
# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]]

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Aticket': all_tickets,
    'Bpopcorn': popcorn,
    'Cwater': water,
    'Dpita Chips': pita_chips,
    'Em&ms': mms,
    'Forange Juice': orange_juice
}

# cost of each snack
price_dict = {
    'Bpopcorn': 2.5,
    'Cwater': 2,
    'Dpita Chips': 4.5,
    'Em&ms': 3,
    'Forange Juice': 3.25
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
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_checker(want_snack, yes_no)

    # Ensures that the snack is valid
    if check_snack == "Yes":
        get_order = get_snack()
    else:
        get_order = []

    print(get_order)

    count = 0
    for client_order in get_order:

        # Assume no snacks have been bought...
        for item in snack_lists:
            item.append(0)

        # print(snack_lists)

        # get order (hard coded for easy testing)
        snack_order = get_order[count]
        count += 1

        for item in get_order:
            if len(item) > 0:
                to_find = (item[1])
                amount = (item[0])
                add_list = movie_data_dict[to_find]
                add_list[-1] = amount

    # Get payment method (ie: work out if surcharge is needed
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit)? ").lower()
        how_pay = string_checker(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

# End of tickets / snacks / payment loop

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and tickets

movie_frame["Sub Total"] = \
    movie_frame['aTicket'] + \
    movie_frame['bPopcorn']*price_dict['bPopcorn'] + \
    movie_frame['cWater']*price_dict['cWater'] + \
    movie_frame['dPita Chips']*price_dict['dPita Chips'] + \
    movie_frame['eM&Ms']*price_dict['eM&Ms'] + \
    movie_frame['fOrange Juice']*price_dict['fOrange Juice']

# Shorten column names
movie_frame = movie_frame.rename(columns={'aTicket': 'Ticket','bPopcorn': 'Popcorn', 'cWater': 'Water', 'dPita Chips': 'Chips', 'eM&Ms': 'M&Ms', 'fOrange Juice': 'OJ'})

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
