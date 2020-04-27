"""
Prints all combinations of nested lists.
"""

def get_all_nested_list(l,returned_list):
    nested_list = l
    while isinstance(nested_list, list):
        for elem in nested_list:
            get_all_nested_list(elem,returned_list)
        if isinstance(nested_list[0], str):
            returned_list.append(nested_list)
        nested_list = nested_list[0]


if __name__ == '__main__':
    l = [['a', 'b', 'c', 'd'],[[["d","d"]],['z', 'x', 'g', 'd'], ['z', 'C', 'G', 'd']]]
    l2 = list()
    get_all_nested_list(l,l2)
    print(l2)
    