from main import get_total

def test_get_total():
    costs_mock = {'socks':5, 'shoes':60, 'sweater':30}
    assert get_total(costs_mock, ['socks', 'shoes'], 0.09) == 70.85


def test_items_not_in_costs():
    costs = {'item1': 10, 'item2': 20, 'item3': 30}
    items = ['item4', 'item5']
    tax = 0.1

    assert get_total(costs, items, tax) == 0.00

def test_tax_is_none():
    costs = {'item1': 10, 'item2': 20, 'item3': 30}
    items = ['item1', 'item2']
    tax = None

    assert get_total(costs, items, tax) == 30.00