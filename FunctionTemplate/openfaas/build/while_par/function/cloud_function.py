from ast import literal_eval
from .itemsets import TransactionManager

'''
Credits to https://github.com/tommyod/Efficient-Apriori/
    blob/master/efficient_apriori/itemsets.py
'''


def cloud_function(json_input):
    transactions = literal_eval(json_input['transactions'])
    candidates = literal_eval(json_input['C_k_array'])
    min_support = json_input['min_support']
    # Processing

    manager = TransactionManager(transactions)

    found_itemsets_partial = {}
    for candidate in candidates:
        over_min_support, indices = manager.transaction_indices_sc(
             candidate, min_support=min_support)
        if over_min_support:
            found_itemsets_partial[candidate] = len(indices)
    # return the result

    res = {
        'found_itemsets_partial': str(found_itemsets_partial)
    }
    return res
