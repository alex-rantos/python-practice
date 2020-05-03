"""You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b."""
def max_diff(num: int) -> int:
    a,b = 0,0
    x = str(num)[0]
    for i in range(9,0,-8):
        if i == 1: 
            c = 1
            while int(x) == 1 or int(x) == 0:
                try:
                    x = str(num)[c]
                    c+=1
                    i = 0
                except:
                    x = str(num)[c - 1]
                    break
            a = int(str(num).replace(str(x), str(i)))
        elif i == 9: 
            c = 1
            while i==int(x): 
                try:
                    x = str(num)[c]
                    c+=1
                except:
                    x = str(num)[0]
                    break
            b = int(str(num).replace(str(x), str(i)))
        x = str(num)[0]

        
    return (b-a)

if __name__ == "__main__":
    assert max_diff(555) == 888
    assert max_diff(9) == 8
    assert max_diff(123456) == 820000
    assert max_diff(10000) == 80000
    assert max_diff(9288) == 8700
    assert max_diff(1019) == 8089