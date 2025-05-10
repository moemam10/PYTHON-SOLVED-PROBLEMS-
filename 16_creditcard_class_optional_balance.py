
class CreditCard:
    def __init__(self, customer, bank, account, limit, balance=0):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = balance

    def __str__(self):
        return f"CreditCard(Customer: {self.customer}, Bank: {self.bank}, Account: {self.account}, Limit: {self.limit}, Balance: {self.balance})"

card1 = CreditCard("John Doe", "Bank A", "1234-5678", 5000)
card2 = CreditCard("Jane Doe", "Bank B", "9876-5432", 3000, 1000)
print(card1)
print(card2)
