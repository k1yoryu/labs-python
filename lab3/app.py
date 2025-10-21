from bank import Bank, Client
import os

from exceptions import InitError

DATA_FILE = "data/bank.json"
STATEMENTS_PATH = "data/statements"


def load_or_create_bank():
    if os.path.exists(DATA_FILE):
        try:
            bank = Bank.load(DATA_FILE)
            print(
                f"\nИнициализация. Загружен банк: {bank.name} ({bank.country}). Количество клиентов {len(bank.clients)}")
            return bank
        except Exception as e:
            print(f"Ошибка загрузки приложения: {e}")
            raise InitError("Ошибка загрузки приложения")
    else:
        print(f"Ошибка загрузки приложения. Файл {DATA_FILE} не найден")
        raise InitError("Ошибка загрузки приложения")


def main_menu(bank: Bank):
    while True:
        print("\n=== Главное меню ===")
        print("1. Показать клиентов")
        print("2. Создать клиента")
        print("3. Войти под клиентом")
        print("4. Сохранить и выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            if not bank.clients:
                print("Нет клиентов в банке.")
            else:
                for c in bank.clients.values():
                    print(f" - {c.client_id}: {c.name} (счетов: {len(c.accounts)} шт.)")

        elif choice == "2":
            client_id = input("Введите ID клиента: ").strip()
            if client_id in bank.clients:
                print("Клиент с таким ID уже существует.")
                continue

            name = input("Полное имя клиента: ").strip()
            email = input("Email: ").strip()
            phone = input("Телефон (необязательно): ").strip() or None

            client = Client(client_id, name, email, phone)
            bank.add_client(client)
            bank.save(DATA_FILE)

            print(f"Клиент {name} создан.")

        elif choice == "3":
            client_id = input("Введите ID клиента: ").strip()
            if client_id not in bank.clients:
                print("Клиент не нйден.")
                continue
            client_menu(bank, client_id)

        elif choice == "4":
            bank.save(DATA_FILE)
            print("Данные сохранены. Выход")
            break
        else:
            print("Неверный выбор, повторите")


def client_menu(bank: Bank, client_id: str):
    client = bank.get_client(client_id)
    while True:
        print(f"\n=== Меню клиента: {client.name} ===")
        print("1. Показать счета")
        print("2. Открыть новый счет")
        print("3. Закрыть счет")
        print("4. Пополнить счет")
        print("5. Снять со счета")
        print("6. Перевести между своими счетами")
        print("7. Сохранить выписку по счетам")
        print("8. Вернуться в главное меню")

        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                if not client.accounts:
                    print("Нет открытых счетов.")
                else:
                    for acc in client.accounts.values():
                        print(f" - {acc}")

            elif choice == "2":
                currency = input(
                    "Какой счет открываем? Введите валюту (доступны BYN, USD, EUR): ").upper()
                bank.open_account(client_id, currency)

            elif choice == "3":
                currency = input("Какой счет закрываем? Введите валюту счета: ").upper()
                bank.close_account(client_id, currency)

            elif choice == "4":
                currency = input("Введите валюту счета: ").upper()
                amount = float(input("Введите сумму пополнения: "))
                bank.deposit(client_id, currency, amount)

            elif choice == "5":
                currency = input("Введите валюту счета: ").upper()
                amount = float(input("Введите сумму для снятия: "))
                bank.withdraw(client_id, currency, amount)

            elif choice == "6":
                from_currency = input("С какой валюты перевести: ").upper()
                to_currency = input("На какую валюту перевести: ").upper()
                amount = float(input("Введите сумму перевода: "))
                bank.transfer(client_id, from_currency, to_currency, amount)

            elif choice == "7":
                save_statement(bank, client_id)

            elif choice == "8":
                bank.save(DATA_FILE)
                break

            else:
                print("Неверный выбор")

            bank.save(DATA_FILE)

        except Exception as e:
            print(f"Ошибка: {e}")

def save_statement(bank: Bank, client_id: str):
    client = bank.get_client(client_id)
    total = sum(acc.balance for acc in client.accounts.values())
    data = {
        "client": client.name,
        "accounts": [acc.to_dict() for acc in client.accounts.values()],
        "total_balance": total
    }

    os.makedirs(STATEMENTS_PATH, exist_ok=True)
    filename = f"{STATEMENTS_PATH}/statement_{client_id}.json"
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Выписка сохранена в {filename}")


if __name__ == "__main__":
    bank = load_or_create_bank()
    main_menu(bank)