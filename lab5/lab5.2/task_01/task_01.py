def count_words(stroka):
    if stroka is None:
        return 0
    words = stroka.split()
    return len(words)
