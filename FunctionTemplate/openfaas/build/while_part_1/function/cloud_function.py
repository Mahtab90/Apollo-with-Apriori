from ast import literal_eval
from .itemsets import apriori_gen

'''
Credits to https://github.com/tommyod/Efficient-Apriori/
    blob/master/efficient_apriori/itemsets.py
'''


def cloud_function(json_input):
    large_itemsets = literal_eval(json_input['large_itemsets'])
    k = json_input['k']
    transaction_count = json_input['trans_num']
    parallel_num = json_input['parallel_num']

    # Processing
    itemsets_list = sorted(item for item in large_itemsets[k - 1].keys())
    C_k = list(apriori_gen(itemsets_list))

    # If no candidate items were found, break the loop
    if not C_k:
        res = {
            'large_itemsets': str(large_itemsets),
            'trans_num': transaction_count,
            'k': 2,
            'while_break_part_1': 1,
            'C_k_array': []
        }
        return res

    list_length = len(C_k)//parallel_num
    C_k_array = [str([C_k[i+j] for j in range(list_length)])
                 for i in range(parallel_num)]
    C_k_array.append(str(C_k[list_length*parallel_num:]))
    # return the result

    res = {
        'large_itemsets': str(large_itemsets),
        'trans_num': transaction_count,
        'k': 2,
        'while_break_part_1': 0,
        'C_k_array': C_k_array
    }
    return res
