import pytest
from main import filtred_data_in_stock

def test_1():
    parsed_data_array = eqwid_test.filtred_data_in_stock();
    for i in parsed_data_array:
        assert i.is_available == 1, 'Товар недоступен'
        print(i.name);



