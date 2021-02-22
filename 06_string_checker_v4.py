
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

    #if snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list
# with valid options for each snack <full name,
# letter code (a - e), and possible abbreviations etc>

valid_snacks = [["popcorn", "p", "corn", "a"],
                ["M&M's", "m&m's", "mms", "m", "b"],
                ["pita chips", "chips", "pc", "pita", "c"],
                ["water", "w", "d"]]

yes_no = [
    ["yes", "y"],
    ["no", "n"],]

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no)

# loop siz times to make testing quicker
for item in range(0, 6):

    # ask user for desired snack and put it lowercase
    desired_snack = input("Snack: ").lower()

    # Check is snack is vaild
    snack_choice = string_checker(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)