def are_anagrams(word1, word2):

    if len(word1) != len(word1):
        return False

    word1 = str(word1).lower()
    word2 = str(word2).lower()

    word1_sort = sorted(word1)
    word2_sort = sorted(word2)

    return word1_sort == word2_sort