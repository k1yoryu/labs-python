import pytest
from task import proverka_treygolnika

def test_pramoygolnie():
    assert proverka_treygolnika(3, 4, 5) == True
    assert proverka_treygolnika(5, 12, 13) == True

def test_ne_pramoygolnie_no_sycheswyit():
    assert proverka_treygolnika(3, 3, 3) == False
    assert proverka_treygolnika(2, 3, 4) == False

def test_ne_sychewyit():
    assert proverka_treygolnika(1, 1, 3) == False
    assert proverka_treygolnika(1, 2, 5) == False
    assert proverka_treygolnika(10, 2, 3) == False

def test_symma3_ravna_dvum():
    assert proverka_treygolnika(1, 2, 3) == False
    assert proverka_treygolnika(5, 5, 10) == False

def test_0_minus_chisla():
    assert proverka_treygolnika(0, 4, 5) == False
    assert proverka_treygolnika(-1, 4, 5) == False
    assert proverka_treygolnika(3, -4, 5) == False

def test_float_chisla():
    assert proverka_treygolnika(6.0, 8.0, 10.0) == True

def test_random_poryadok():
    assert proverka_treygolnika(5, 3, 4) == True
    assert proverka_treygolnika(4, 5, 3) == True

def test_string():
    with pytest.raises(TypeError):
        proverka_treygolnika("3", "4", "5")

    with pytest.raises(TypeError):
        proverka_treygolnika(3, "4", 5)

def test_invalid_types():
    with pytest.raises(TypeError):
        proverka_treygolnika(None, 1, 1)
