import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('lab_4_part_5.xlsx', sheet_name='Данные', skiprows=1)
df = df.dropna(axis=1, how='all')
df.columns = ['Дата', 'Год', 'Год_мес', 'точка', 'бренд', 'товар', 'Количество', 'Продажи', 'Себестоимость']

df['Средняя_цена'] = df['Продажи'] / df['Количество']
df['Прибыль'] = df['Продажи'] - df['Себестоимость']

point_analysis = df.groupby('точка').agg({
    'Количество': 'sum',
    'Продажи': ['sum', 'mean'],
    'Себестоимость': 'sum',
    'Прибыль': 'sum'
}).round(0)
point_analysis.columns = ['Количество', 'Продажи_всего', 'Продажи_средние', 'Себестоимость', 'Прибыль']

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
point_analysis['Продажи_всего'].sort_values().plot(kind='barh', color='skyblue')
plt.title('Продажи по точкам')
plt.xlabel('Продажи, руб.')

plt.subplot(2, 2, 2)
point_analysis['Продажи_средние'].sort_values().plot(kind='barh', color='lightgreen')
plt.title('Средние продажи на точку')
plt.xlabel('Средние продажи, руб.')

plt.subplot(2, 2, 3)
point_analysis['Количество'].sort_values().plot(kind='barh', color='orange')
plt.title('Количество продаж по точкам')
plt.xlabel('Количество, шт.')

plt.subplot(2, 2, 4)
point_analysis['Прибыль'].sort_values().plot(kind='barh', color='purple')
plt.title('Прибыль по точкам')
plt.xlabel('Прибыль, руб.')

plt.suptitle('АНАЛИЗ ПО ТОЧКАМ РЕАЛИЗАЦИИ', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

product_analysis = df.groupby('товар').agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum',
    'Средняя_цена': 'mean',
    'Прибыль': 'sum'
}).round(0)

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
product_analysis.nlargest(8, 'Продажи')['Продажи'].plot(kind='bar', color='blue')
plt.title('Топ-8 товаров по продажам')
plt.ylabel('Продажи, руб.')
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
product_analysis.nlargest(8, 'Прибыль')['Прибыль'].plot(kind='bar', color='orange')
plt.title('Топ-8 товаров по прибыли')
plt.ylabel('Прибыль, руб.')
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
product_analysis.nlargest(8, 'Количество')['Количество'].plot(kind='bar', color='green')
plt.title('Топ-8 товаров по количеству')
plt.ylabel('Количество, шт.')
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
product_analysis.nlargest(8, 'Средняя_цена')['Средняя_цена'].plot(kind='bar', color='red')
plt.title('Топ-8 товаров по средней цене')
plt.ylabel('Средняя цена, руб.')
plt.xticks(rotation=45)

plt.suptitle('АНАЛИЗ ПО ТОВАРАМ', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

monthly_dynamics = df.groupby('Год_мес').agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Прибыль': 'sum'
}).reset_index()
monthly_dynamics['Рост_%'] = monthly_dynamics['Продажи'].pct_change() * 100

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.plot(monthly_dynamics['Год_мес'].astype(str), monthly_dynamics['Продажи'], marker='o', linewidth=2)
plt.title('Динамика товарооборота')
plt.ylabel('Продажи, руб.')
plt.xticks(rotation=45)
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(monthly_dynamics['Год_мес'].astype(str), monthly_dynamics['Количество'], marker='s', linewidth=2, color='red')
plt.title('Динамика количества продаж')
plt.ylabel('Количество, шт.')
plt.xticks(rotation=45)
plt.grid(True)

plt.subplot(2, 2, 3)
colors = ['red' if x < 0 else 'green' for x in monthly_dynamics['Рост_%'].fillna(0)]
plt.bar(monthly_dynamics['Год_мес'].astype(str), monthly_dynamics['Рост_%'].fillna(0), color=colors)
plt.title('Рост/спад продаж по месяцам (%)')
plt.ylabel('Изменение, %')
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
plt.plot(monthly_dynamics['Год_мес'].astype(str), monthly_dynamics['Прибыль'], marker='^', linewidth=2, color='orange')
plt.title('Динамика прибыли')
plt.ylabel('Прибыль, руб.')
plt.xticks(rotation=45)
plt.grid(True)

plt.suptitle('ДИНАМИКА ТОВАРООБОРОТА', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

top_products = product_analysis.nlargest(5, 'Продажи').index
forecast_data = []

for product in top_products:
    product_sales = df[df['товар'] == product].groupby('Год_мес')['Количество'].sum()
    if len(product_sales) > 1:
        last_3_avg = product_sales.tail(3).mean()
        trend = product_sales.pct_change().mean()
        forecast = last_3_avg * (1 + (trend if not pd.isna(trend) and trend > -0.5 else 0.05))
        forecast_data.append({
            'Товар': product,
            'Средние_продажи': int(last_3_avg),
            'Прогноз': int(forecast)
        })

forecast_df = pd.DataFrame(forecast_data)

if not forecast_df.empty:
    plt.figure(figsize=(12, 6))

    x_pos = np.arange(len(forecast_df))
    width = 0.35

    plt.bar(x_pos - width / 2, forecast_df['Средние_продажи'], width, label='Факт', alpha=0.7, color='blue')
    plt.bar(x_pos + width / 2, forecast_df['Прогноз'], width, label='Прогноз', alpha=0.7, color='red')

    plt.title('ПРОГНОЗ ПРОДАЖ ПО ТОВАРАМ', fontsize=14, fontweight='bold')
    plt.ylabel('Количество, шт.')
    plt.xticks(x_pos, forecast_df['Товар'], rotation=45)
    plt.legend()
    plt.grid(True, axis='y', alpha=0.3)

    for i, (fact, forecast_val) in enumerate(zip(forecast_df['Средние_продажи'], forecast_df['Прогноз'])):
        plt.text(i - width / 2, fact + max(fact, forecast_val) * 0.01, f'{fact}', ha='center', va='bottom')
        plt.text(i + width / 2, forecast_val + max(fact, forecast_val) * 0.01, f'{forecast_val}', ha='center',
                 va='bottom')

    plt.tight_layout()
    plt.show()

total_sales = df['Продажи'].sum()
total_quantity = df['Количество'].sum()
total_profit = df['Прибыль'].sum()
avg_price = df['Средняя_цена'].mean()

print("ИТОГОВЫЕ ПОКАЗАТЕЛИ:")
print(f"Товарооборот: {total_sales:,.0f} руб.")
print(f"Количество продаж: {total_quantity:,.0f} шт.")
print(f"Прибыль: {total_profit:,.0f} руб.")
print(f"Средняя цена: {avg_price:.0f} руб.")
print(f"Товаров: {df['товар'].nunique()} шт.")
print(f"Точек: {df['точка'].nunique()} шт.")
print(f"Период: {df['Год_мес'].min()} - {df['Год_мес'].max()}")

best_product = product_analysis.nlargest(1, 'Продажи').index[0]
best_point = point_analysis.nlargest(1, 'Продажи_всего').index[0]

print(f"\nЛУЧШИЕ ПОКАЗАТЕЛИ:")
print(f"Топ товар: {best_product}")
print(f"Топ точка: {best_point}")
