def filter_list(l):
    integer_list = []
    for elem in l:
        if type(elem) == type(1):
            integer_list.append(elem)
    
    return integer_list

if __name__ == '__main__':
    print(filter_list([1,2,'a','b']))
    