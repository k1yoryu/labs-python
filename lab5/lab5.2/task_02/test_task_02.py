from task_02 import find_unique
import pytest

def test_povtory():
    input_list = [1, 5, 2, 1, 3, 5, 4]
    assert find_unique(input_list) == [2, 3, 4]

def test_net_unikalnyh():
    input_list = ['a', 'b', 'b', 'a', 'c', 'c']
    assert find_unique(input_list) == []

def test_smeshannye_dannye():
    input_list = [7, 'hello', 777, 'hello', 7, 'Python']
    assert find_unique(input_list) == [777, 'Python']

def test_boolean():
    input_list = [True, False, 1, 0, 5]
    assert find_unique(input_list) == [5]

def test_otritsatelnye_chisla():
    input_list = [-1, -2, 0, -1, -5, 0]
    assert find_unique(input_list) == [-2, -5]

def test_pustoy_vvod():
    assert find_unique([]) == []