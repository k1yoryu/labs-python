import random
from faker import Faker
import pandas as pd


# === Генерация данных ===
fake = Faker('ru_RU')
years = [2021, 2022, 2023, 2024, 2025]
forms = ['очная', 'заочная']
specialties = [
    "Программная инженерия",
    "Прикладная информатика",
    "Кибербезопасность",
]

students = []
for _ in range(500):
    year = random.choice(years)
    form = random.choice(forms)
    specialty = random.choice(specialties)

    math = random.randint(0, 100)
    lang = random.randint(0, 100)
    phy = random.randint(0, 100)  # Физика

    ct_total = math + lang + phy
    school = round(random.uniform(5.0, 10.0), 1)
    total = ct_total + school * 10

    students.append({
        "ФИО": fake.name(),
        "Год поступления": year,
        "Форма обучения": form,
        "Балл ЦТ/ЦЭ": ct_total,
        "ЦТ_Математика": math,
        "ЦТ_Русский язык": lang,
        "ЦТ_Физика": phy,
        "Средний балл аттестата": school,
        "Общий балл": total,
        "Специальность": specialty,
        "Адрес регистрации": fake.address().replace("\n", ", "),
        "Номер мобильного телефона": fake.phone_number()
    })

df = pd.DataFrame(students)
