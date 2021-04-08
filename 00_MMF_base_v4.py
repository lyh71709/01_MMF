# import statements
import re
import pandas

# functions go here


# get_snack function goes here
def get_snack():

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list
    # with valid options for each snack <full name,
    # letter code (a - e), and possible abbreviations etc>

    # Has all valid snacks that a user can get
    valid_snacks = [["popcorn", "p", "pop", "corn", "a"],
                    ["M&M's", "m&m's", "mms", "m", "b"],
                    ["pita chips", "chips", "pc", "pita", "c"],
                    ["water", "h20", "w", "d"],
                    ["orange juice", "oj", "o", "juice", "e"]]

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

        if amount >= 5:
            print("Sorry - we have a four snack limit")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_row.append(snack_choice)

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

# valid pay methods
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]
# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]]


popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]
surcharge_mult_list = []

# Lists to store summary data...
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]

summary_data = []

summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
}

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
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
    snack_order = get_snack()

    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
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

    surcharge_mult_list.append(surcharge_multiplier)

# End of tickets / snacks / payment loop

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and tickets

movie_frame["Snacks"] = \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['Water'] * price_dict['Water'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# Shorten column names
movie_frame = movie_frame.rename(columns={'Pita Chips': 'Chips',
                                          'Orange juice': 'OJ',
                                          'Surcharge_Multiplier': 'SM'})
# Set up summary dataframe
# populate snack items
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# Get ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_price)

total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# Create summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# Set up columns to be printed
pandas.set_option("display.max_columns", None)

# Display numbers to 2 dp
pandas.set_option('precision', 2)

print()
print("*** Ticket / Snack Information ***")
print("Note: for full details, please see the excel file called")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])
print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)

# Gives feedback after loop has ended
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))
