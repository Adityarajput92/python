 balance = 5000
pin = 1234
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("Login successful")

        while True:
            print("""
1. WITHDRAW
2. CHECK BALANCE
3. EXIT
""")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = int(input("Enter amount: "))
                if amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= amount
                    print("Withdraw successful! Remaining balance:", balance)

            elif choice == "2":
                print("Total balance:", balance)

            elif choice == "3":
                print("exit:")
                break

            else:
                print("Invalid choice, try again.")
   break  

    else:
        attempts += 1
        print("Incorrect PIN! Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Login failed, too many attempts:")