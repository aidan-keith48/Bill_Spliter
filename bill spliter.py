import random


def store_party_people():
    num_attending = int(input("Enter the number of people attending: \n"))

    if num_attending <= 0:
        print("No one is joining for the party")
        return

    table = {}

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_attending):
        attending = input().strip()
        table[attending] = 0  # Initialize everyone's bill to 0

    total_bill = float(input("\nEnter the total bill value: "))

    lucky_one = luck_one(table)  # Check if we are picking a lucky one

    if lucky_one:  # If someone is lucky, update the bill split
        update_new_bill(table, total_bill, num_attending, lucky_one)
    else:
        update_bill(table, total_bill, num_attending)

    return table


def luck_one(table):
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ').strip().lower()

    if lucky_choice == "yes":
        lucky_person = random.choice(list(table.keys()))
        print(f"{lucky_person} is the lucky one!")
        return lucky_person  # Return the lucky person's name
    else:
        print("No one is going to be lucky")
        return


def update_new_bill(table, total_bill, num_attending, lucky_one):
    split_bill = round(total_bill / (num_attending - 1), 2)  # Exclude lucky one

    for name in table:
        table[name] = split_bill if name != lucky_one else 0  # Set lucky one's bill to 0


def update_bill(table, total_bill, num_attending):
    split_bill = round(total_bill / num_attending, 2)
    for name in table:
        table[name] = split_bill

    return table


result = store_party_people()
if result is not None:
    print(result)
