"""
How much will you spend?
Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.

If item doesn't exist in the given cost values, the item is ignored.

Output should be rounded to two decimal places.
"""

costs = {'socks':5, 'shoes':60, 'sweater':30}


def get_total(costs, items, tax=0):
    if tax is None:
        tax = 0
    total_sum = sum(costs.get(item, 0) for item in items) * (1 + tax)
    return round(total_sum, 2)

total_sum = get_total(costs, ['socks', 'shoes'], 0.09)
print(total_sum)
