from ast import literal_eval
from .itemsets import TransactionManager

'''
Credits to https://github.com/tommyod/Efficient-Apriori/
    blob/master/efficient_apriori/itemsets.py
'''


def cloud_function(json_input):
    transactions = literal_eval(json_input['transactions'])
    min_support = json_input['min_support']

    # Processing
    class_name = transactions.pop()

    manager = TransactionManager(transactions)

    transaction_count = len(manager)
    if transaction_count == 0:
        res = {
            'large_itemsets': str({}),
            'trans_num': 0,
            'k': 0,
            'class_name': class_name,
            'condition': 0
        }
        return res

    # Generating the itemsets of size 1
    candidates = {(item,): len(indices) for item, indices in
                  manager._indices_by_item.items()}
    large_itemsets = {1: {item: count for (item, count) in candidates.items()
                          if (count / len(manager)) >= min_support}}

    # if large itemsets were found, convert to dictionary
    if not large_itemsets.get(1, dict()):
        res = {
            'large_itemsets': str({}),
            'trans_num': transaction_count,
            'k': 0,
            'class_name': class_name,
            'condition': 0
        }
        return res

    # return the result

    res = {
        'large_itemsets': str(large_itemsets),
        'trans_num': transaction_count,
        'k': 2,
        'class_name': class_name,
        'condition': 1
    }
    return res
