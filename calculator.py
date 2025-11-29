  print ("""
    1. Addition
    2. Subtraction
    3. multiplication
    4. exit
    """)
    choice = input (" Enter your choice :")
    if choice == "1":
        num1 = int (input ("Enter Number 1 "))
        num2 = int (input ("Enter Number 1 "))
        print("Addition is ", num1 + num2)
        
    elif choice== "2":
        num1 = int (input ("Enter Number 1 "))
        num2 = int (input ("Enter Number 1 "))
        print("substraction is ", num1 - num2)
        
    elif choice== "3":
        num1 = int (input ("Enter Number 1 "))
        num2 = int (input ("Enter Number 1 "))
        print("multiplication is ", num1 * num2)
        
    else : 
        print("Invalid")