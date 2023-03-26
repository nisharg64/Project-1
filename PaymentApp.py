#Online Payment App

#Creat a Class
class Paymentapp:
    #Creat a Init Function to get User-Data
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    #Use to make payment
    def scan_and_pay(self):
        num = input("Enter Name or Number: ")
        balance = self.balance
        print(f"Your current balance is:{balance} $")
        payment_amount = float(input("Enter Payment Amount: "))
        if payment_amount > balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - payment_amount
            print(f"\nPayment successful. Your Account balance is: {self.balance} $")

    #Use to Add money to wallet
    def add_money(self):
        num = input("Enter Name or Number: ")
        balance = self.balance
        print(f"Your current balance is:{balance} $")

        add_amount = float(input("Enter Amount to be Add:"))
        self.balance = self.balance + add_amount
        print(f"\nMoney added successfully. Your Account balance is: {self.balance} $")

    #Use to check Available Balance
    def check_balance(self):
        balance = self.balance
        print(f"\nYour current balance is:{balance} $")

    #To Show Menu os service
    def show_menu(self):
        print("\n ** Select Service **")
        print("Press-1: Scan & Pay")
        print("Press-2: Add Money to Wallet")
        print("Press-3: Balance & History")

    #To Select Service option
    def select_option(self):
        self.show_menu()
        self.op = int(input("Select Service: "))

        if self.op == 1:
            self.scan_and_pay()
        elif self.op == 2:
            self.add_money()
        elif self.op == 3:
            self.check_balance()
        else:
            print(f"Please Enter Valid Input!!")

        self.wanna_continue()

    #Use to Continue the process in loop
    def wanna_continue(self):
        self.is_continue = input("\nEnter Y:Continue & Q:Quit: ")

        if self.is_continue.lower() == 'y':
            self.select_option()
        else:
            print("\n*** --Thank You For Exit--  ***")

    #Make Login Function Using @staticmethod
    @staticmethod
    def login(users):
        user = input("Enter User Name: ")
        pwd = input("Enter Password: ")

        if user in users and users[user].password == pwd:
            print("\n*** Login Successfully ***")
            users[user].select_option()
        else:
            print("Invalid User Name and Password. Please try Again")

#Creat User Dictionary for login Function
users = {
    "nisharg": Paymentapp("nisharg", "7143", 50000000000),
    "parth": Paymentapp("parth", "9797", 50000000),
    "adarsh": Paymentapp("adarsh", "8780", 100000000)
}

#Creat Object To call functions
Paymentapp.login(users)
