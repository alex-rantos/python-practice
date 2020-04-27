""" Return a string representation of a diamond with correct indentation."""

def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    ret_str = []
    counter = 1
    while(counter <= n):
        indent = (n-counter)//2
        ret_str.extend(indent*" " + counter*"*" + "\n")
        counter += 2
    
    counter = n - 2
    while(counter >= 1):
        indent = (n-counter)//2
        print(indent)
        ret_str.extend(indent*" " + counter*"*" + "\n")
        counter -= 2

    return "".join(ret_str) 
    
if __name__ == '__main__':
    expected =  " *\n"
    expected += "***\n"
    expected += " *\n"
    assert (diamond(1) == "*\n")
    assert (diamond(2) == None)
    assert (diamond(3) == expected)
    assert (diamond(5) == "  *\n ***\n*****\n ***\n  *\n")
    assert (diamond(0) == None)
    assert (diamond(-3) == None)
