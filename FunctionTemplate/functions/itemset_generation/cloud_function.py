from ast import literal_eval
from .itemsets import itemsets_from_transactions

'''
Credits to https://github.com/tommyod/Efficient-Apriori/blob/master/efficient_apriori/apriori.py
'''


def cloud_function(json_input):
    transactions = literal_eval(json_input['transactions'])
    min_support = json_input['min_support']
    max_length = json_input['max_length']
    verbosity = json_input['verbosity']

    class_name = transactions.pop()

    itemsets, num_trans = itemsets_from_transactions(
        transactions,
        min_support,
        max_length,
        verbosity,
        output_transaction_ids=True,
    )

    itemsets_raw = {
        length: {item: counter.itemset_count for
                 (item, counter) in itemsets.items()}
        for (length, itemsets) in itemsets.items()
    }

    res = {
        'itemsets_raw': str(itemsets_raw),
        'num_trans': num_trans,
        'class_name': class_name
    }
    return res
