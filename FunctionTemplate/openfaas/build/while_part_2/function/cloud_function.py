from ast import literal_eval
from operator import concat
from functools import reduce

'''
Credits to https://github.com/tommyod/Efficient-Apriori/
    blob/master/efficient_apriori/itemsets.py
'''


def cloud_function(json_input):
    found_itemsets_partial = json_input['found_itemsets_partial']
    large_itemsets = literal_eval(json_input['large_itemsets'])
    k = json_input['k']
    max_length = json_input['max_length']

    # Processing
    found_itemsets_ = [literal_eval(itemsets) for itemsets in
                       found_itemsets_partial]
    found_itemsets = reduce(concat, found_itemsets_)

    # If no itemsets were found, break out of the loop
    if not found_itemsets:
        res = {
            'large_itemsets': str(large_itemsets),
            'while_break_part_2': 1,
            'k': k
        }
        return res

    large_itemsets[k] = {i: counts for (i, counts) in found_itemsets.items()}

    k += 1

    if k > max_length:
        res = {
            'large_itemsets': str(large_itemsets),
            'while_break_part_2': 1,
            'k': k
        }
        return res

    # return the result
    res = {
        'large_itemsets': str(large_itemsets),
        'while_break_part_2': 0,
        'k': k
    }
    return res
