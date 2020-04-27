"""
Moving Zeros To The End
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.
"""

def swap_elems(array,fromIndex,toIndex):
    if (toIndex < 0):
        raise Exception("Invalid state. toIndex(=%d) should not be negative",toIndex)
    array[toIndex] = array[fromIndex]
    array[fromIndex] = 0 

def move_zeros(array):
    index , zero_occurences = 0 , 0
    print(array)
    while (index < len(array)):
        if array[index] == 0 and type(array[index]) != type(False):
            zero_occurences += 1
        else:
            if zero_occurences > 0:
                swap_elems(array,index,index - zero_occurences)
                #zero_occurences = 0
                print(array)
        index += 1
    return array

if __name__ == '__main__':
    assert move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]