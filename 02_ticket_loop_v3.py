# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

# Start of the loop
while name != "xxx" and count < MAX_TICKETS:

    # Makes sure there is no plural when there is 1 ticket left
    if MAX_TICKETS - count == 1:
        print("You have 1 seat left")
    else:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # Get details
    count += 1
    name = input("What is your name? ")
    # Makes xxx not count as a ticket sold
    if name == "xxx":
        count -= 1
    print()

# Gives feedback after loop has ended
if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(count, MAX_TICKETS - count))