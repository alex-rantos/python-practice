"""Write a program that outputs sequentially the integers from 1 to 99 but on some conditions prints a string instead:
when the integer is a multiple of 3 print “Open” instead of the number,
when it is a multiple of 7 print “Source” instead of the number,
when it is a multiple of both 3 and 7 print “OpenSource” instead of the number."""

def is_multiple3(x:int)->bool:
    return True if x%3 == 0 else False
def is_multiple7(x:int)->bool:
    return True if x%7 == 0 else False

def print_integers(arr:[int]) -> None:
    if not arr: return
    for x in arr:
        mul3 = is_multiple3(x)
        mul7 = is_multiple7(x)
        if mul3 and mul7:
            print('OpenSource')
        elif mul3:
            print("Open")
        elif mul7:
            print("Source")
        else:
            print(x)

if __name__ == "__main__":
    array = [x for x in range(1,100)]
    print_integers(array) 
    