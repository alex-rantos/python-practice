""" Split any sequence by a certain @param delimiter """

def split_seq_by_delimiter(seq, delimiter):
    sublist = []
    for elem in seq:
        if (elem != delimiter):
            sublist.append(elem)
        else:
            yield sublist
            sublist = []
    # When delimiter was not found in the end, the last seq was not returned.
    if sublist:
        yield sublist      


import itertools
if __name__ == '__main__':
    l = ['g', 'd', 'e', '*', 'g', 'f', 'e']
    lists = list(split_seq_by_delimiter(l, "*"))
    print(lists)
    
    spl = [list(y) for x, y in itertools.groupby(l, lambda z: z == "*") if not x]
    print(spl)