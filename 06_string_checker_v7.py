import re


# Fucntion goes here
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

# Gets list of snacks
def get_snack():

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list
    # with valid options for each snack <full name,
    # letter code (a - e), and possible abbreviations etc>

    # Has all valid snacks that a user can get
    valid_snacks = [["popcorn", "p", "corn", "a"],
                    ["M&M's", "m&m's", "mms", "m", "b"],
                    ["pita chips", "chips", "pc", "pita", "c"],
                    ["water", "w", "d"],
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

        # add snack and amount to list
        amount_snack = "{} {}".format(amount, snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(amount_snack)

# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]]

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no)

# Ensures that the snack is valid
if check_snack == "Yes":
    get_order = get_snack()
else:
    get_order = []


# Show snack orders
print()
if len(get_order) == 0:
    print("Snacks Ordered: None")
else:
    print("Snacks Ordered:")

    '''for item in snack_order:
        print(item)'''
        
    print(get_order)


