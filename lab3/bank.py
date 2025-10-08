from exceptions import InsufficientFundsError
from exceptions import AccountExistsError, AccountNotFoundError


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


class Client:
        def __init__(self, client_id, name, email=None, phone=None):
            self.client_id = client_id
            self.name = name
            self.email = email
            self.phone = phone
            self.accounts = {}

        def add_account(self, account):
            if account.currency in self.accounts:
                raise AccountExistsError("Счет в этой валюте уже существует")
            self.accounts[account.currency] = account

        def remove_account(self, currency):
            if currency not in self.accounts:
                raise AccountNotFoundError("Счет не найден")
            del self.accounts[currency]

        def get_account(self, currency):
            if currency not in self.accounts:
                raise AccountNotFoundError("Счет не найден")
            return self.accounts[currency]

        def to_dict(self):
            return {
                "id": self.client_id,
                "name": self.name,
                "email": self.email,
                "phone": self.phone,
                "accounts": [a.to_dict() for a in self.accounts.values()]
            }

        @staticmethod
        def from_dict(data):
            client = Client(data["id"], data["name"], data.get("email"), data.get("phone"))
            for acc_data in data.get("accounts", []):
                acc = BankAccount(
                    acc_data["id"],
                    client.client_id,
                    acc_data["currency"],
                    acc_data["balance"]
                )
                client.add_account(acc)
            return client

        def __str__(self):
            return f"{self.name} (ID: {self.client_id})"