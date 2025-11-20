from task_05 import combine_dicts
import pytest

def test_bazovoe_sliyanie_bez_peremesheniya():
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    assert combine_dicts(d1, d2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def test_perekrytie_klyuchey():
    d1 = {'имя': 'Алёша', 'возраст': 16}
    d2 = {'возраст': 18, 'город': 'Минск'}
    assert combine_dicts(d1, d2) == {'имя': 'Алёша', 'возраст': 18, 'город': 'Минск'}

def test_pustoy_vtoroy_slovar():
    d1 = {'ключ': 'значение'}
    d2 = {}
    assert combine_dicts(d1, d2) == {'ключ': 'значение'}


def test_pustoy_perviy_slovar():
    d1 = {}
    d2 = {1: 'a', 2: 'b'}
    assert combine_dicts(d1, d2) == {1: 'a', 2: 'b'}


def test_raznye_tipy_klyuchey_i_znacheniy():
    d1 = {1: [1, 2], 'данные': 99}
    d2 = {2: (3, 4), 'данные': 'перезапись'}
    assert combine_dicts(d1, d2) == {1: [1, 2], 'данные': 'перезапись', 2: (3, 4)}