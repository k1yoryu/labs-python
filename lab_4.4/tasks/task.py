import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
sales_df = pd.read_excel('s7_sales.xlsx')
sales_df['ISSUE_DATE'] = pd.to_datetime(sales_df['ISSUE_DATE'])
sales_df['MONTH'] = sales_df['ISSUE_DATE'].dt.month
sales_df['YEAR'] = sales_df['ISSUE_DATE'].dt.year

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.hist(sales_df['REVENUE_AMOUNT'], bins=50, alpha=0.7, color='skyblue')
plt.title('Распределение выручки', fontsize=12, fontweight='bold')
plt.xlabel('Сумма (руб)\n', fontsize=9)
plt.ylabel('Количество продаж\n', fontsize=9)
plt.grid(True, alpha=0.3)

# Топ аэропортов отправления
plt.subplot(2, 3, 2)
top_departures = sales_df['ORIG_CITY_CODE'].value_counts().head(8)
plt.barh(range(len(top_departures)), top_departures.values, color='lightblue')
plt.yticks(range(len(top_departures)), top_departures.index)
plt.title('Топ-8 аэропортов отправления', fontsize=12, fontweight='bold')
plt.xlabel('\nКоличество вылетов', fontsize=9)
plt.grid(True, alpha=0.3)

# Топ аэропортов назначения
plt.subplot(2, 3, 3)
top_arrivals = sales_df['DEST_CITY_CODE'].value_counts().head(8)
plt.barh(range(len(top_arrivals)), top_arrivals.values, color='lightgreen')
plt.yticks(range(len(top_arrivals)), top_arrivals.index)
plt.title('Топ-8 аэропортов назначения', fontsize=12, fontweight='bold')
plt.xlabel('\nКоличество прилетов', fontsize=9)
plt.grid(True, alpha=0.3)

# Типы пассажиров
plt.subplot(2, 3, 4)
pax_counts = sales_df['PAX_TYPE'].value_counts()
plt.pie(pax_counts.values, labels=pax_counts.index, autopct='%1.1f%%',
        colors=['lightblue', 'lightgreen', 'lightcoral', 'gold'])
plt.title('Типы пассажиров', fontsize=12, fontweight='bold')

# Способы оплаты
plt.subplot(2, 3, 5)
fop_counts = sales_df['FOP_TYPE_CODE'].str.split(',').explode().value_counts().head(6)
plt.bar(fop_counts.index, fop_counts.values, color='orange')
plt.title('Способы оплаты', fontsize=12, fontweight='bold')
plt.xlabel('\nСпособ оплаты', fontsize=9)
plt.ylabel('Количество\n', fontsize=9)
plt.xticks(rotation=45)

# Программа лояльности
plt.subplot(2, 3, 6)
ffp_counts = sales_df['FFP_FLAG'].value_counts()
plt.bar(['Без FFP', 'С FFP'], ffp_counts.values, color=['gray', 'red'])
plt.title('Программа лояльности', fontsize=12, fontweight='bold')
plt.ylabel('Количество\n', fontsize=9)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 5))

# Сезонность продаж
plt.subplot(1, 3, 1)
monthly_sales = sales_df.groupby('MONTH').size()
plt.plot(monthly_sales.index, monthly_sales.values, 'o-', linewidth=2, color='blue')
plt.title('Продажи по месяцам', fontsize=12, fontweight='bold')
plt.xlabel('\nМесяц', fontsize=9)
plt.ylabel('Количество продаж\n', fontsize=9)
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)

# Средняя выручка по типам перелетов
plt.subplot(1, 3, 2)
route_revenue = sales_df.groupby('ROUTE_FLIGHT_TYPE')['REVENUE_AMOUNT'].mean()
plt.bar(route_revenue.index, route_revenue.values, color=['green', 'purple'])
plt.title('Средняя выручка по типам перелетов', fontsize=12, fontweight='bold')
plt.xlabel('\nТип перелета', fontsize=9)
plt.ylabel('Средняя выручка\n', fontsize=9)
plt.grid(True, alpha=0.3)

# Каналы продаж
plt.subplot(1, 3, 3)
channel_counts = sales_df['SALE_TYPE'].value_counts()
plt.bar(channel_counts.index, channel_counts.values, color=['navy', 'darkred'])
plt.title('Каналы продаж', fontsize=12, fontweight='bold')
plt.xlabel('\nТип продажи', fontsize=9)
plt.ylabel('Количество\n', fontsize=9)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ПРОГНОЗ
monthly = sales_df.groupby(['YEAR', 'MONTH']).agg({
    'REVENUE_AMOUNT': ['sum', 'count']
}).reset_index()
monthly.columns = ['year', 'month', 'выручка', 'билеты']
monthly = monthly.sort_values(['year', 'month'])
monthly["номер_месяца"] = range(len(monthly))

X = monthly[["номер_месяца"]]
model_tickets = LinearRegression().fit(X, monthly["билеты"])
model_revenue = LinearRegression().fit(X, monthly["выручка"])

future = pd.DataFrame({"номер_месяца": range(len(monthly), len(monthly) + 3)})
pred_tickets = model_tickets.predict(future)
pred_revenue = model_revenue.predict(future)

fig, ax = plt.subplots(1, 2, figsize=(15, 4))

# Прогноз билетов
ax[0].plot(monthly["номер_месяца"], monthly["билеты"], "o-", label="Факт")
ax[0].plot(future["номер_месяца"], pred_tickets, "s--", label="Прогноз")
ax[0].set_title("Количество билетов", fontsize=14)
ax[0].set_ylabel("Билеты, шт\n", fontsize=10)
ax[0].legend()
ax[0].grid(alpha=0.3)

# Прогноз выручки
ax[1].plot(monthly["номер_месяца"], monthly["выручка"], "o-", label="Факт")
ax[1].plot(future["номер_месяца"], pred_revenue, "s--", label="Прогноз")
ax[1].set_title("Выручка", fontsize=14)
ax[1].set_ylabel("Выручка, руб\n", fontsize=10)
ax[1].legend()
ax[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

print("=== ОСНОВНЫЕ ВЫВОДЫ ===")
print(f"• Всего продаж: {len(sales_df):,}")
print(f"• Средний чек: {sales_df['REVENUE_AMOUNT'].mean():.0f} руб")
print(f"• Онлайн продажи: {(sales_df['SALE_TYPE']=='ONLINE').mean()*100:.1f}%")

print("\n=== АЭРОПОРТЫ ===")
print(f"• Главные хабы: MOW ({sales_df['ORIG_CITY_CODE'].value_counts().iloc[0]} вылетов)")
print(f"• OVB - второй по загруженности")

print("\n=== СЕЗОННОСТЬ ===")
monthly_stats = sales_df.groupby('MONTH').size()
print(f"• Пик продаж: месяц {monthly_stats.idxmax()}")
print(f"• Спад: месяц {monthly_stats.idxmin()}")

print("\n=== ПАССАЖИРЫ ===")
print(f"• Взрослые: {sales_df['PAX_TYPE'].value_counts()['AD']/len(sales_df)*100:.1f}%")
print(f"• Участники FFP: {(sales_df['FFP_FLAG']=='FFP').mean()*100:.1f}%")

print("\n=== ОПЛАТА ===")
fop_main = sales_df['FOP_TYPE_CODE'].str.split(',').explode().value_counts().index[0]
print(f"• Основной способ: {fop_main}")
print("• Преобладают простые способы оплаты")

print("\n=== ПРОГНОЗ НА 3 МЕСЯЦА ===")
print(f"• Рост продаж: +{(pred_tickets[-1]/monthly['билеты'].iloc[-1]-1)*100:.1f}%")
print(f"• Рост выручки: +{(pred_revenue[-1]/monthly['выручка'].iloc[-1]-1)*100:.1f}%")