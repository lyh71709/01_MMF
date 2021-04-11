
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


def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? ")
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("Mega Movie Fundraiser Instructions")
        print()
        print("1. Cannot cancel order (NO REFUNDS!)\n2. Enter 'xxx' in to skip or cancel the question")
        print("3. When ordering snacks if you want more than one of a snack put the number in front (For example 3pita chips or 3 water")
        print("======== Pricing ========")
        print("Minor Ticket(12 - 16yrs) - $7.50)
        print("Adult Ticket(16 - 65)")

    return ""


# Main Routine goes here
# list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]]

# Ask if instructions are needed
instructions(yes_no)
print()
print("Program launches...")
