money = input("Введите сумму в рублях(целое число): ")
if not money.isdigit():
    print("Введите целое число")
else:
   money = int(money)
   po_100 = money // 100
   money %= 100

   po_50 = money // 50
   money %= 50

   po_10 = money // 10
   money %= 10

   po_5 = money // 5
   money %= 5

   po_2 = money // 2
   money %= 2

   po_1 = money // 1

   print ("Купюры по 100 рублей: ", po_100)
   print ("Купюры по 50 рублей: ", po_50)
   print("Купюры по 10 рублей: ", po_10)
   print("Купюры по 5 рублей: ", po_5)
   print("Купюры по 2 рубля: ", po_2)
   print("Купюры по 1 рублю: ", po_1)

