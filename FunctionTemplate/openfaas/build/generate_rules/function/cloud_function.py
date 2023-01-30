from ast import literal_eval
from .itemsets import ItemsetCount, TransactionManager
from .rules import generate_rules_apriori

'''
Credits to https://github.com/tommyod/Efficient-Apriori/
    blob/master/efficient_apriori/itemsets.py
'''


def cloud_function(json_input):
    transactions = literal_eval(json_input['transactions'])
    large_itemsets = literal_eval(json_input['large_itemsets'])
    num_trans = json_input['num_trans']
    min_confidence = json_input['min_confidence']

    # Processing

    manager = TransactionManager(transactions)

    itemsets_out = {
        length: {
            item: ItemsetCount(itemset_count=count,
                               members=manager.transaction_indices(set(item)))
            for (item, count) in itemsets.items()
        }
        for (length, itemsets) in large_itemsets.items()
    }

    itemsets_raw = {
        length: {item: counter.itemset_count for
                 (item, counter) in itemsets.items()}
        for (length, itemsets) in itemsets_out.items()
    }

    rules = generate_rules_apriori(itemsets_raw,
                                   min_confidence,
                                   num_trans,
                                   verbosity=0)

    # return the result
    res = {
        "itemsets_raw": str(itemsets_raw),
        'rules': str(list(rules)),
        'num_trans': num_trans
    }
    return res
