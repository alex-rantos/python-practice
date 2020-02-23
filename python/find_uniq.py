""" 
    Find the trully unique string from an array
    @return the string that consists of characters that match no other string in the array
"""
def find_trully_uniq(arr):
    found = False
    for i in range(len(arr) - 1):
        if (type(arr[i]) != str) or (type(arr[i+1]) != str):
            raise Exception("Invalid element. Should be string")

        res = set(arr[i]).intersection(arr[i+1])


        if (res == set()):
            # case for whitespace
            if (arr[i].strip() == arr[i+1].strip() == ""):
                continue
            if (found == False):
                # element in [i] or [i + 1] is unique
                found = True
            else:
                # If previous iteration elem was found it means the unique
                # elem was the [i + 1] in the previous iteration and [i] on this one
                return arr[i]
        else:
            # case that first elem is the unique
            if (found == True):
                return arr[i-1]
    if (found == True):
        # return last one         
        return arr[-1]
    else:
        return None

""" 
    Find the unique string from an array
    @return the string that consists the least similar characters with any other string in the array
"""
def find_uniq(arr):
    found = False
    ht = {}
    for i in range(len(arr) - 1):
        if (type(arr[i]) != str) or (type(arr[i+1]) != str):
            raise Exception("Invalid element. Should be string")

        res = set(arr[i]).intersection(arr[i+1])

        if len(res) not in ht.keys():
            ht[len(res)] = (arr[i],arr[i+1])

        if (res == set()):
            # case for whitespace
            if (arr[i].strip() == arr[i+1].strip() == ""):
                continue
            if (found == False):
                # element in [i] or [i + 1] is unique
                found = True
            else:
                # If previous iteration elem was found it means the unique
                # elem was the [i + 1] in the previous iteration and [i] on this one
                return arr[i]
        else:
            # case that first elem is the unique
            if (found == True):
                return arr[i-1]
    if (found == True):
        # return last one         
        return arr[-1]
    else:
        # return the least similar
        min_key = min(ht.keys())
        return ht[min_key][1]


if __name__ == '__main__':
    
    assert (find_trully_uniq([ 'Aa', 'aaa', 'aaaaa', 'Aaaa', 'AaAaAa', 'a' , 'BbBb']) == 'BbBb')
    assert (find_trully_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) == 'foo')
    assert (find_trully_uniq([ 'Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem',
    'Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem',
    'Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Logas','Gollem' ]) == None)
    assert (find_trully_uniq([ '0x1171 ','0x1171 ','0x2240','0x1171' ]) == None)

    assert (find_uniq([ 'Gollem','Gollem','Gollem','Gollem','Gollem'
    ,'Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem',
    'Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Gollem','Logas','Gollem' ]) == "Logas")
    assert (find_uniq([ '0x1171 ','0x1171 ','0x2240','0x1171' ]) == "0x2240")
