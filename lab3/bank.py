from exceptions import InsufficientFundsError

class BankAccount:
    def __init__(self, account_id, client_id, currency, balance=0.0):
        self.account_id = account_id
        self.client_id = client_id
        self.currency = currency
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств на счете")
        self.balance -= amount

    def to_dict(self):
        return {
            "id": self.account_id,
            "currency": self.currency,
            "balance": self.balance
        }

    def __str__(self):
        return f"Счет {self.account_id}: {self.currency} {self.balance:.2f}"