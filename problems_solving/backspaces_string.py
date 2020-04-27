# Assume "#" is like a backspace in string.
def clean_string(string):
    mylist = []
    for elem in string:
        if elem == '#':
            if len(mylist) > 0: 
                mylist.pop()
        else:
            mylist.append(elem)
    return ''.join(mylist)

"""   
import regex
def reg_clean_string(string):
    return regex.sub(r'[^#]((?R)*)#+|\A#+', '', s)
"""

if __name__ == '__main__':
    assert clean_string('abc####d##c#') == ''
    print("Test passed")
    