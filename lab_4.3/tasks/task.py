import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt

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

    math = random.randint(70, 100)
    lang = random.randint(85, 100)
    phy = random.randint(65, 100)

    ct_total = math + lang + phy
    school = round(random.uniform(8.5, 10.0), 1)
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

plt.style.use("ggplot")

numeric_cols = [
    "ЦТ_Математика",
    "ЦТ_Русский язык",
    "ЦТ_Физика",
    "Средний балл аттестата",
    "Общий балл",
    "Балл ЦТ/ЦЭ"
]

yearly_avg = df.groupby("Год поступления")[numeric_cols].mean().reset_index()


#Средние баллы ЦТ
plt.figure(figsize=(9, 5))
plt.plot(yearly_avg["Год поступления"], yearly_avg["ЦТ_Математика"], label="Математика")
plt.plot(yearly_avg["Год поступления"], yearly_avg["ЦТ_Русский язык"], label="Русский язык")
plt.plot(yearly_avg["Год поступления"], yearly_avg["ЦТ_Физика"], label="Физика")
plt.title("Средние баллы ЦТ по годам")
plt.xlabel("Год поступления")
plt.ylabel("Средний балл")
plt.legend()
plt.show()

#Средний балл аттестата
plt.figure(figsize=(9, 5))
plt.plot(yearly_avg["Год поступления"], yearly_avg["Средний балл аттестата"], color="green")
plt.title("Средний балл аттестата по годам")
plt.xlabel("Год поступления")
plt.ylabel("Средний балл")
plt.show()

#Минимальный проходной балл по специальностям
plt.figure(figsize=(10, 5))
for spec in specialties:
    subset = df[df["Специальность"] == spec]
    mins = subset.groupby("Год поступления")["Общий балл"].min()
    plt.plot(mins.index, mins.values, label=spec)

plt.title("Минимальный проходной балл по специальностям")
plt.xlabel("Год поступления")
plt.ylabel("Минимальный общий балл")
plt.legend()
plt.show()

#Количество студентов по специальностям
plt.figure(figsize=(8, 4))
spec_counts = df["Специальность"].value_counts()
plt.barh(spec_counts.index, spec_counts.values)
plt.title("Количество студентов по специальностям")
plt.xlabel("Количество")
plt.ylabel("Специальность")
plt.show()

#Формы обучения
plt.figure(figsize=(6, 6))
form_counts = df["Форма обучения"].value_counts()
plt.pie(form_counts.values, labels=form_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Распределение по формам обучения")
plt.show()