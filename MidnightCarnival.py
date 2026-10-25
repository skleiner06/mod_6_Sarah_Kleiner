"""
Name: Sarah Kleiner
Assignment: The Midnight Carnival
"""
# The Carnival Entrance
# Set accumulators to use at the end
admissions = 0
visitors = 0
total_ticket = 0
total_points = 0

# Start a while loop to keep track of visitors
while True:
    name = input("Please enter your name, or done when you are finished: ").capitalize().strip()

    if name == 'Done': # Sentinel
        break
    age = int(input("Please enter your age: "))
    vip_pass = input("Do you have a VIP pass? yes/no: ").strip().lower()


    if age < 8:
        print("Visitors younger than 8 must be accompanied by an adult.")
        continue

    elif (age >= 8 and age <= 17) and vip_pass == 'no':
        print(f"Welcome, {name}! Admission will cost $5.")
        admissions += 5
        visitors += 1

    elif age >= 18 and vip_pass == 'no':
        print(f"Welcome, {name}! Admission will cost $10.")
        admissions += 10
        visitors += 1

    elif age >= 8 and vip_pass == 'yes':
        print(f"Welcome, {name}! You have free admission!")
        visitors += 1

    # The Ticket Booth
    # Start another while loop to ask for amount of tickets, within a range
    while True:
        try:
            tickets = int(input("How many tickets do you want to buy? "))

            if tickets < 1 or tickets > 20:
                raise ValueError("Please enter a number between 1 and 20.")

        except ValueError as e:
            print("Invalid input:", e)

        else:
            print("Valid purchase.")
            break # When a valid number is entered, loop breaks to print ticket price and add that to the visitors charge

    ticket_price = 2 * tickets
    total_ticket += ticket_price

    print(f"Total: ${ticket_price}")
    # Adds the visitors ticket price to their admission price
    if vip_pass == "yes":
        print(f"Total charges: ${ticket_price}")
    elif age <= 17:
        print(f"Total charges: ${ticket_price + 5}")
    else:
        print(f"Total charges: ${ticket_price + 10}")

    # The Lucky Number Game
    # Accumulator for visitor's individual points
    points = 0

    for ticket in range(tickets):

        guess = int(input("Guess a number between 1 and 5: "))

        if guess == 3:
            points += 10

        elif guess == 1 or guess == 2 or guess == 4 or guess == 5:
            points += 2

        elif guess < 1 or guess > 5:
            points += 0

    print(f"You have earned {points} points!")
    total_points += points # Adds individual points to the total points

    # The Mystery Prize Board

    row = 1
    col = 1
    count = 0
    # Run the loop for 5 rows and columns and then break
    while row <= 5:
        while col <= 5:
            count += 1 # Accumulator to keep track of how many positions are examined

            if row == col or row + col == 6: # For every positon where row and column are equal, and for the positions where together they equal 6, print *.
                print("*", end = " ")

            else:
                print("_", end = " " )

            col += 1

        print()
        row += 1 # Keeps going to the next row and starts from column 1
        col = 1
    print("Total positions examined:", count)

    # Closing Time
final_total = admissions + total_ticket # Calculates final charges
# The final report is printed
print("Report: ")
print("Visitors: ", visitors)
print(f"Admission Revenue: ${admissions}")
print(f"Ticket Revenue: ${total_ticket}")
print("Total Prize Points: ", total_points)
print(f"Total Revenue: ${final_total}")

# Testing Record

# Test 1: Denied Visitor
# Input: Name = Sarah, Age = 7, VIP pass = no, then done
# Expected: Visitors younger than 8 must be accompanied by an adult.
# No tickets or games offered.
# Report: 0 visitors, $0 admission, $0 tickets, 0 points, $0 total.

# Test 2: VIP Visitor
# Input: Name = Sarah, Age = 16, VIP pass = yes
# Tickets = 2, Guesses = 3, 5, then done
# Expected: Welcome, Rachel! You have free admission!
# Total: $4
# Total charges: $4
# You have earned 12 points!
# Total positions examined: 25

# Test 3: Invalid Ticket Quantity
# Input: Name = Sarah, Age = 18, VIP pass = no
# Tickets = 25, then 5, Guesses = 3, 1, 2, 4, 5, then done
# Expected: Invalid input: Please enter a number between 1 and 20.
# Valid purchase.
# Total: $10
# Total charges: $20
# You have earned 18 points!

# Test 4: Nonnumeric Ticket Entry
# Input: Name = Sarah, Age = 15, VIP pass = no
# Tickets = abc, then 3, Guesses = 3, 2, 8, then done
# Expected: Invalid input: invalid literal for int() with base 10: 'abc'
# Valid purchase.
# Total: $6
# Total charges: $11
# You have earned 12 points!

# Test 5: Multiple Visitors and Closing
# Input: Name = Sarah, Age = 16, VIP pass = no
# Tickets = 1, Guess = 3
# Next visitor: Rachel, Age = 20, VIP pass = yes
# Tickets = 2, Guesses = 1, 5
# Next name = done
# Expected Report:
# Visitors: 2
# Admission Revenue: $5
# Ticket Revenue: $6
# Total Prize Points: 14
# Total Revenue: $11