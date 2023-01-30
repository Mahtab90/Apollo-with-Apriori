from ast import literal_eval


def cloud_function(json_input):
    itemsets_raw = json_input['itemsets_raw']
    rules = json_input['rules']
    num_trans = json_input['num_trans']
    classes = json_input['class_name']

    # Processing
    output = {}
    for item, rule, num_trans, class_name in zip(itemsets_raw, rules,
                                                 num_trans, classes):
        output[class_name] = {'itemsets': literal_eval(item),
                              'rules': rule,
                              'num_transactions': num_trans}
    # return the result
    res = {
        'analysis_results': str(output)
    }
    return res
