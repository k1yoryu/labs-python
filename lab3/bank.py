import json
import os
import uuid
from datetime import date
from exceptions import UnauthorizedOperationError, InsufficientFundsError, AccountExistsError, AccountNotFoundError

class Bank:
    def __init__(self, name, country, created_at=None, currency_rates=None):
        self.name = name
        self.country = country
        self.created_at = created_at or str(date.today())
        self.clients = {}
        self.currency_rates = currency_rates

    def add_client(self, client):
        self.clients[client.client_id] = client

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise UnauthorizedOperationError("Клиент не найден")
        return self.clients[client_id]

    def open_account(self, client_id, currency):
        currency = currency.upper()
        if currency not in self.currency_rates:
            raise ValueError(
                f"Неверная валюта. Доступные: {', '.join(self.currency_rates.keys())}"
            )

        client = self.get_client(client_id)

        if currency in client.accounts:
            raise ValueError(f"У клиента уже есть счет в валюте {currency}")

        account = BankAccount(str(uuid.uuid4()), client_id, currency)
        client.add_account(account)
        print(f"Открыт счет {account.account_id} для клиента {client.name} ({currency})")

    def close_account(self, client_id, currency):
        client = self.get_client(client_id)
        client.remove_account(currency)
        print(f"Счет в валюте {currency} закрыт")

    def deposit(self, client_id, currency, amount):
        acc = self.get_client(client_id).get_account(currency)
        acc.deposit(amount)
        print(f"Баланс после пополнения: {acc.balance:.2f} {currency}")

    def withdraw(self, client_id, currency, amount):
        acc = self.get_client(client_id).get_account(currency)
        acc.withdraw(amount)
        print(f"Баланс после снятия: {acc.balance:.2f} {currency}")

    def transfer(self, client_id, from_currency, to_currency, amount):
        client = self.get_client(client_id)
        from_acc = client.get_account(from_currency)
        to_acc = client.get_account(to_currency)
        from_acc.withdraw(amount)

        converted = self.convert_currency(amount, from_currency, to_currency)
        to_acc.deposit(converted)

        print(
            f"Перевод {amount:.2f} {from_currency} → {converted:.2f} {to_currency} "
            f"(курс {from_currency}/{to_currency}: {self.currency_rates[to_currency] / self.currency_rates[from_currency]:.3f})"
        )

    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency not in self.currency_rates or to_currency not in self.currency_rates:
            raise ValueError("Неизвестная валюта")
        base_usd = amount / self.currency_rates[from_currency]
        converted = base_usd * self.currency_rates[to_currency]
        return round(converted, 2)

    @staticmethod
    def load(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError("Файл данных не найден")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)["bank"]

        bank = Bank(
            data["name"],
            data["country"],
            data.get("created_at"),
            data.get("currency_rates")
        )

        for c in data.get("clients", []):
            client = Client.from_dict(c)
            bank.add_client(client)

        return bank

    def save(self, filepath):
        data = {
            "bank": {
                "name": self.name,
                "country": self.country,
                "created_at": self.created_at,
                "currency_rates": self.currency_rates,
                "clients": [c.to_dict() for c in self.clients.values()]
            }
        }

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def __str__(self):
        return f"{self.name} ({self.country})"


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