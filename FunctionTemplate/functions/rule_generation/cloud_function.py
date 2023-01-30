from ast import literal_eval
from .rules import generate_rules_apriori

'''
Credits to https://github.com/tommyod/Efficient-Apriori/blob/master/efficient_apriori/apriori.py
'''


def cloud_function(json_input):
    itemsets_raw = literal_eval(json_input['itemsets_raw'])
    min_confidence = json_input['min_confidence']
    num_trans = json_input['num_trans']
    verbosity = json_input['verbosity']

    rules = generate_rules_apriori(
        itemsets_raw,
        min_confidence,
        num_trans,
        verbosity,
    )

    res = {
        'itemsets': str(itemsets_raw),
        'rules': str(list(rules))
    }

    return res
