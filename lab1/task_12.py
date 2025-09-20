tarif_minutes = 60
tarif_sms = 30
tarif_internet = 1024  # 1 ГБ
tarif_price = 24.99

# перерасход за единицу
minute_price = 0.89
sms_price = 0.59
mb_price = 0.79
nalog = 0.02

used_minutes = int(input("Введите количество израсходованных за месяц минут: "))
used_sms = int(input("Введите количество отправленных за месяц SMS: "))
used_internet = int(input("Введите объем использованного интернет-трафика (в МБ): "))

dopoln_minuti = used_minutes - tarif_minutes
dopoln_smski = used_sms - tarif_sms
dopoln_trafik = used_internet - tarif_internet

if dopoln_minuti < 0:
    dopoln_minuti = 0
if dopoln_smski < 0:
    dopoln_smski = 0
if dopoln_trafik < 0:
    dopoln_trafik = 0

stoimost_minuti = dopoln_minuti * minute_price
stoimost_smski = dopoln_smski * sms_price
stoimost_trafik = dopoln_trafik * mb_price

itogo_bez_naloga = tarif_price + stoimost_minuti + stoimost_smski + stoimost_trafik
summa_naloga = itogo_bez_naloga * nalog
itogo = itogo_bez_naloga + summa_naloga

print("Тариф: " + str(round(tarif_price, 2)) + " руб.")

if dopoln_minuti > 0:
    print("Минут сверх тарифа: " + str(dopoln_minuti) + " шт, доплата " + str(round(stoimost_minuti, 2)) + " руб.")

if dopoln_smski > 0:
    print("SMS сверх тарифа: " + str(dopoln_smski) + " шт, доплата " + str(round(stoimost_smski, 2)) + " руб.")

if dopoln_trafik > 0:
    print("Интернет сверх тарифа: " + str(dopoln_trafik) + " МБ, доплата " + str(round(stoimost_trafik, 2)) + " руб.")

print("Налог: " + str(round(summa_naloga, 2)) + " руб.")
print("Всего к оплате: " + str(round(itogo, 2)) + " руб.")