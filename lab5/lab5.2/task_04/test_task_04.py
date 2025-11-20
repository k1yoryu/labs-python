from task_04 import are_anagrams
import pytest

def test_anagramma():
    assert are_anagrams("маяк", "ямка") == True

def test_ne_anagramma():
    assert are_anagrams("маяк", "ёлка") == False

def test_raznaya_dlina():
    assert are_anagrams("сержант", "подполковник") == False

def test_razniy_registr():
    assert are_anagrams("Маяк", "ямка") == True

def test_pustie_stroki():
    assert are_anagrams("", "") == True

def test_frazi_s_probelami():
    assert are_anagrams("Меча сИла", "села Мича") == True

