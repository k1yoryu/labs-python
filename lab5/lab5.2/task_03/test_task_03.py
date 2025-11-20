from task_03 import is_palindrome
import pytest

def test_slovo_ne_palindrome():
    assert is_palindrome("nonstop") == False

def test_slovo_palindrome():
    assert is_palindrome("заказ") == True

def test_registr():
    assert is_palindrome("Заказ") == False

def test_chislo_palindrome():
    assert is_palindrome(12321) == True

def test_chislo_ne_palindrome():
    assert is_palindrome(37529329) == False

def test_odin_simvol_chislo_pusto():
    assert is_palindrome("a") == True
    assert is_palindrome(5) == True
    assert is_palindrome("") == True

def test_otricatelnoe_chislo_unikalnaya_proverka():
    assert is_palindrome(-121) == False