from task_01 import count_words

def test_2_slova():
    assert count_words("Глаза что?") == 2

def test_7_slov():
    assert count_words("Тёмная ночь, только пули свистят по степи") == 7

def test_pustaya_stroka():
    assert count_words("") == 0

def test_nevidimye_razdeliteli():
    text = "Слово\tвторое\nтретье"
    assert count_words(text) == 3

def test_slova_cherez_defis():
    text = "Рок-н-ролл"
    assert count_words(text) == 1

def test_mnogo_punktuatsii_bez_probela():
    text = "Остановитесь!!!"
    assert count_words(text) == 1

def test_lishnie_probely_v_seredine():
    assert count_words("раз   два    три") == 3

def test_probely_po_krayam_i_lishnie_vnutri():
    assert count_words("   Начало середина конец  ") == 3

def test_tolko_probely():
    assert count_words("    ") == 0

def test_znachenie_none():
    assert count_words(None) == 0