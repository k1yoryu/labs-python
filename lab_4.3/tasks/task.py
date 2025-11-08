import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    phy = random.randint(0, 100)

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

plt.style.use('ggplot')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

yearly_avg = df.groupby('Год поступления')[['ЦТ_Математика', 'ЦТ_Русский язык', 'ЦТ_Физика', 'Средний балл аттестата']].mean().reset_index()

# График 1: Динамика средних баллов ЦТ
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(yearly_avg['Год поступления'], yearly_avg['ЦТ_Математика'], label='Математика (ЦТ)')
ax.plot(yearly_avg['Год поступления'], yearly_avg['ЦТ_Русский язык'], label='Русский язык (ЦТ)')
ax.plot(yearly_avg['Год поступления'], yearly_avg['ЦТ_Физика'], label='Физика (ЦТ)')
ax.set_title('Динамика средних баллов ЦТ по годам')
ax.set_xlabel('Год поступления')
ax.set_ylabel('Средний балл')
ax.set_xticks(years)
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()

# График 2: Динамика среднего балла аттестата
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(yearly_avg['Год поступления'], yearly_avg['Средний балл аттестата'], label='Средний балл аттестата', color='green')
ax.set_title('Динамика среднего балла аттестата')
ax.set_xlabel('Год поступления')
ax.set_ylabel('Средний балл')
ax.set_xticks(years)
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()

# График 3: Динамика проходного балла
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(
    data=df,
    x='Год поступления',
    y='Общий балл',
    hue='Специальность',
    estimator='min',
    ci=None,
    ax=ax
)
ax.set_title('Динамика проходного балла по специальностям')
ax.set_xlabel('Год поступления')
ax.set_ylabel('Минимальный "Общий балл"')
ax.set_xticks(years)
ax.legend(title='Специальность')
ax.grid(True)
plt.tight_layout()
plt.show()

# График 4: Количество поступивших по специальностям
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(
    data=df,
    y='Специальность',
    order=df['Специальность'].value_counts().index,
    ax=ax
)
ax.set_title('Количество студентов по специальностям')
ax.set_xlabel('Количество студентов')
ax.set_ylabel('Специальность')
plt.tight_layout()
plt.show()

# График 5: Статистика по формам обучения
form_counts = df['Форма обучения'].value_counts()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(
    form_counts,
    labels=form_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
ax.set_title('Распределение по формам обучения')
ax.axis('equal')
plt.show()