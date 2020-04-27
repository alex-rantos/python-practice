""" 
Extracts all inner multi-level nested lists and returns them in a list.
If an element is not a list return the element by itseft
"""

from itertools import chain 

# stackoverflow answer
def remove_unnecessary_lists(nested_list):
    for item in nested_list:
        if not isinstance(item,list):
            yield item
        elif list(chain(*item)) == item:
            yield item
        else:
            yield from remove_unnecessary_lists(item)

if __name__ == '__main__':
    my_nested_list = [['a', 'b', 'c', 'd'],['e', [["d","d"]],['z', 'x', 'g', 'd'], ['z', 'C', 'G', 'd']]]
    l = [['a', 'b', 'c', 'd'],[["d","d","g"],[[["a"]]],[["d","d"]],['z', 'x', 'g', 'd'], ['z', 'C', 'G', 'd']]]
    #my_nested_list = [['a', 'b', 'c', 'd'],['e', ['r'], [["d","d"]],['z', 'x', 'g', 'd'], ['z', 'C', 'G', 'd']]]

    flat_list = list(remove_unnecessary_lists(my_nested_list))
    print(flat_list)
    