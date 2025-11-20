import pytest

def count_words(stroka):
    if stroka is None:
        return 0
    words = stroka.split()
    return len(words)

def test_simple_sentence():
    # Проверка обычного предложения
    assert count_words("Привет мир") == 2

def test_sentence_with_multiple_spaces():
    # Проверка предложения с лишними пробелами между словами
    assert count_words("Python    это   круто") == 3

def test_sentence_with_leading_trailing_spaces():
    # Проверка пробелов в начале и конце строки
    assert count_words("   Начало и конец   ") == 3

def test_empty_string():
    # Проверка пустой строки
    assert count_words("") == 0

def test_string_with_only_spaces():
    # Проверка строки, состоящей только из пробелов
    assert count_words("     ") == 0

def test_none_input():
    # Проверка случая, если передали None (защита от ошибок)
    assert count_words(None) == 0