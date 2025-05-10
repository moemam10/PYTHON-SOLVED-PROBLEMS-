
class CreditCard:
    def __init__(self, customer, bank, account, limit, balance=0):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = balance

    def setcustomer(self, customer):
        self.customer = customer

    def setbank(self, bank):
        self.bank = bank

    def setaccount(self, account):
        self.account = account

    def setlimit(self, limit):
        self.limit = limit

    def setbalance(self, balance):
        self.balance = balance

    def charge(self, amount):
        if amount + self.balance > self.limit:
            return False
        else:
            self.balance = amount
            return True

    def makePayment(self, amount):
        if amount < 0:
            print("Payment amount cannot be negative.")
        else:
            self.balance -= amount

    def __str__(self):
        return f"CreditCard(Customer: {self.customer}, Bank: {self.bank}, Account: {self.account}, Limit: {self.limit}, Balance: {self.balance})"

card1 = CreditCard("John Doe", "Bank A", "1234-5678", 5000)
card2 = CreditCard("Jane Doe", "Bank B", "9876-5432", 3000, 1000)
print(card1)
print(card2)
