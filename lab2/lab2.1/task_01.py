text = input("Введите текст: ")
words = text.split()

words_counts = {}
for word in words:
    words_counts[word] = words_counts.get(word, 0) + 1

print("Словарь слов и их количества: ")
for word, count in words_counts.items():
    print(word + ":" + str(count))