# Paytm User

#Dictionairy of saved Login ID's
users = {"parth": {"password": "9797", "balance": 2000},
         "adarsh": {"password": "8780", "balance": 3000},
         "nisharg": {"password": "7143", "balance": 4000}}

#Writing a login Function
def login():
    while True:
        print()
        username = input("Enter username: ")
        if username in users:
            password = input("Enter password: ")
            if password == users[username]["password"]:
                return username
        print("Invalid username or password. Please try again.")

#Writing a User interface Functions (Scan&Pay,To mobile&contact,To UPI app,To Bank,Add Money,Balance&History)
def scan_and_pay(username):
    balance = users[username]["balance"]
    print(f"Your current balance is: {balance} $")
    payment_amount = float(input("Enter payment amount: "))
    if payment_amount > balance:
        print("Insufficient balance.")
    else:
        users[username]["balance"] -= payment_amount
        print(f"Payment successful. Your new balance is: {users[username]['balance']} $")

def to_mobile_or_contact(username):
    balance = users[username]["balance"]
    print(f"Your current balance is: {balance}")
    payment_amount = float(input("Enter payment amount: "))
    if payment_amount > balance:
        print("Insufficient balance.")
    else:
        users[username]["balance"] -= payment_amount
        print(f"Payment successful. Your new balance is: {users[username]['balance']} $")

def to_upi_apps(username):
    balance = users[username]["balance"]
    print(f"Your current balance is: {balance} $")
    payment_amount = float(input("Enter payment amount: "))
    if payment_amount > balance:
        print("Insufficient balance.")
    else:
        users[username]["balance"] -= payment_amount
        print(f"Payment successful. Your new balance is: {users[username]['balance']} $")

def to_bank(username):
    balance = users[username]["balance"]
    print(f"Your current balance is: {balance} $")
    payment_amount = float(input("Enter payment amount: "))
    if payment_amount > balance:
        print("Insufficient balance.")
    else:
        users[username]["balance"] -= payment_amount
        print(f"Payment successful. Your new balance is: {users[username]['balance']} $")

def add_money(username):
    balance = users[username]["balance"]
    print(f"Your current balance is: {balance} $")
    add_amount = float(input("Enter amount to be added: "))
    users[username]["balance"] += add_amount
    print(f"Money added successfully. Your new balance is: {users[username]['balance']} $")

def check_balance(username):
    balance = users[username]["balance"]
    print(f"Your current balance is: {balance} $")

while True:
    username = login()
    if username is not None:
        while True:
            print("\n****Select Service****")
            print("Press-1: Scan & Pay")
            print("Press-2: To Mobile or Contact")
            print("Press-3: To UPI's Apps")
            print("Press-4: To Bank")
            print("Press-5: Add Money to Wallet")
            print("Press-6: Balance & History")

            ser = int(input("\nSelect Services:"))

            if ser == 1:
                num = input("Enter Name Or Number: ")
                scan_and_pay(username)

            elif ser == 2:
                num = input("Enter Name Or Number: ")
                to_mobile_or_contact(username)

            elif ser == 3:
                num = input("Enter UPI ID: ")
                to_upi_apps(username)

            elif ser == 4:
                num = input("Enter Bank Name: ")
                num2 = int(input("Enter Account Number: "))
                to_bank(username)

            elif ser == 5:
                add_money(username)

            elif ser == 6:
                check_balance(username)

            choice = input("Enter 'y' to Continue or 'q' to quit: ")
            if choice.lower() == 'y':
                pass
            elif choice.lower() == 'q':
                exit()
            else:
                print(f"Please Enter Valid Input!!")