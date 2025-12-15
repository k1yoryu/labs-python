# сгенерировать базу данных, в которой в первой колонке (напитки к новому году)
# количество этих напитков на складе (в бутылках)
# Количество проданных со склада напитков
# цена за бутылку
# страна производства, год производства
# расчетый столбце: посчитать объем выручки (от реализованной продукции)
# и остаток на складе


from faker import Faker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fake = Faker()

napitki = ["Вода", "Rich", "Fanta", "Sprite", "Квас", "Чай", "Морс"]
strana = ["Франция", "Италия", "Россия", "Германия", "Испания", "Армения", "США"]


n = 100
data = {
    "Напиток": [fake.random_element(napitki) for _ in range(n)],
    "Страна производства": [fake.random_element(strana) for _ in range(n)],
    "Год производства": [fake.random_int(min=2000, max=2024) for _ in range(n)],
    "Количество на складе": [fake.random_int(min=10, max=500) for _ in range(n)],
    "Продано": [],
    "Цена за бутылку": [round(fake.random_int(min = 500, max  = 5000), 2) for _ in range(n)]
}

for i in range(n):
    max_sold = data["Количество на складе"][i]
    sold = fake.random_int(min=0, max=max_sold)
    data["Продано"].append(sold)

df = pd.DataFrame(data)
print(df.head(5))

df["Выручка"] = df["Продано"] * df["Цена за бутылку"]
df["Остаток на складе"] = df["Количество на складе"] - df["Продано"]
print(df.head(5))

total = df.groupby("Напиток")["Выручка"].sum()
total.plot(kind='bar', figsize=(10, 5), title="Выручка по напиткам", color='red')
plt.ylabel("Выручка")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

ostatok = df.groupby("Напиток")["Остаток на складе"].sum()
ostatok.plot(kind='bar', figsize=(10, 5), title="Остаток на складе", color='black')
plt.ylabel("Количество (бутылки)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

money_strana = df.groupby("Страна производства")["Выручка"].sum()
money_strana.plot(kind='pie', autopct='%1.1f%%', title="Доля выручки по странам")
plt.ylabel('')
plt.tight_layout()
plt.show()