import numpy as np

money_month = np.array([45.70, 56.90, 43.20, 42.90, 37, 29,
                     27, 15.90, 56.90, 40, 42, 44])

winter_money = np.sum(money_month[[0, 1, 11]])
summer_money = np.sum(money_month[[5, 6, 7]])

if winter_money > summer_money:
    print(f"Больше тратится зимой. {winter_money} > {summer_money}")
elif summer_money > winter_money:
    print(f"Больше тратится летом. {summer_money} > {winter_money}")
else:
    print("Одинаково тратится")

max_value = np.max(money_month)
max_months = np.where(money_month == max_value)[0] + 1
print("Номера месяцев с наибольшими расходами:", *max_months)