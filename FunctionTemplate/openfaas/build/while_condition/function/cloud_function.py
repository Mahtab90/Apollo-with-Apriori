from ast import literal_eval

def cloud_function(json_input):
    max_length = json_input['max_length']
    large_itemsets = literal_eval(json_input['large_itemsets'])
    while_break_part_1 = json_input['while_break_part_1']
    while_break_part_2 = json_input['while_break_part_2']
    k = json_input['k']

    # Processing
    if while_break_part_1 == 1:
        condition = 0
    elif while_break_part_2 == 1:
        condition = 0
    elif max_length == 1:
        condition = 0
    elif not large_itemsets[k-1]:
        condition = 0
    else:
        condition = 1

    # return the result
    res = {
        'condition': condition
    }
    return res
