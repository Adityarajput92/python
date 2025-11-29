print(" Movie Ticket Booking Site")

movies = {
    1: {"name": "Maa", "price": 250},
    2: {"name": "Hindustaan", "price": 350},
    3: {"name": "Tera Ishq Main", "price": 300}
}

print("Available Movies:")
print("1. Maa – Rs 250")
print("2. Hindustaan – Rs 350")
print("3. Tera Ishq Main – Rs 300")

choice = int(input("Enter movie number to book ticket: "))

if choice not in movies:
    print("Invalid choice! Please restart.")
    exit()

movie_name = movies[choice]["name"]
ticket_price = movies[choice]["price"]

seats = {
    1: {"type": "Silver", "extra": 0},
    2: {"type": "Gold", "extra": 50},
    3: {"type": "Platinum", "extra": 100}
}

print("""
Seat Types:
1. Silver(+0 Rs)
2. Gold(+50 Rs)
3. Platinum(+100 Rs)
""")

seat_choice = int(input("Enter seat type number: "))

if seat_choice not in seats:
    print("Invalid seat type!")
    exit()

seat_type = seats[seat_choice]["type"]
extra_charge = seats[seat_choice]["extra"]

tickets = int(input("Enter number of tickets: "))

if tickets <= 0:
    print("Invalid number of tickets!")
    exit()

total_amount = (ticket_price + extra_charge) * tickets

print(" BILL ")
print("Movie:", movie_name)
print("Seat Type:", seat_type)
print("Tickets:", tickets)
print("Price per Ticket:", ticket_price)
print("Extra charge per Ticket:", extra_charge)
print("Total Amount:", total_amount)