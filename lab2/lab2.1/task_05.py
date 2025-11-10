word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()

word1_sort = sorted(word1)
word2_sort = sorted(word2)

if word1_sort == word2_sort:
    print("Это анаграмма")
else:
    print("Это не анаграмма")