# python refresher
# a simple banking script

#create a customer class
#This is the parent class.

print('Create customer:')
print('Deposit using the deposit():')
print('View balance using the view_balance():')
print('withdraw using the withdraw():')
print('..................................')

class Customer():

    def __init__ (self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("Customer Details")
        print("")
        print("Name:  ",self.name)
        print("Age:   ",self.age)
        print("Gender:",self.gender)

#Child Class

class Bank(Customer):
    def __init__(self,name,age,gender):
        super().__init__ (name,age,gender) # The super refers to the method in the parent class.
        self.balance = 0

    # Deposit method. Takes amount as an argument.
    def deposit(self,amount):
        self.amount = amount
        self.balance += self.amount
        print("Account Balance Updated: Ksh",self.balance)

    # Withdraw method.
    #Takes amount as an argument.
    #Checks first if there is enouch balance.
    def withdraw(self,amount):

        self.amount=amount
        
        if self.amount > self.balance:
            print("Insufficient Balance.")
            print("Available Balance: KSh.",self.balance)
        else:
             self.balance = self.balance - self.amount
             print("Withdrawal Successful.")
             print("Amount withdrawn: Ksh.",self.amount)
             print("Account Balance: KSh.",self.balance)

    #Method to view Balance
    #Only takes the self argument
    def view_balance(self):

        #Utilize the show details method of the parent class.
        self.show_details()

        #Obtain the current account balance.
        print("Account Balance. KSh.",self.balance)
