""" Create a new list allowing up to max_e duplicates of each member """
def delete_nth(order,max_e):
    hs = {}
    ret_list = []
    for elem in order:
        if elem in hs:
            if hs[elem] >= max_e:
                continue
            else:
                ret_list.append(elem)
                hs[elem] += 1
        else:
            hs[elem] = 1
            ret_list.append(elem)
    return ret_list
    
if __name__ == '__main__':
    assert (delete_nth([20,37,20,21], 1) == [20,37,21])
    assert (delete_nth([1,1,3,3,7,2,2,2,2], 3) == [1, 1, 3, 3, 7, 2, 2, 2])    

"""
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
"""
