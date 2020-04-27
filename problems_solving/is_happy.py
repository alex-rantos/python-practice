def is_happy(n):
    """
    A happy number is a number defined by the following process: 
    Starting with any positive integer, replace the number by the sum of the squares of its digits, 
    and repeat the process until the number equals 1 (where it will stay), 
    or it loops endlessly in a cycle which does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers.
    """
    dic = {}
    while True:
        n = is_happy_proc(n)
        if n == 1:
            return True
        elif n in dic:
            return False
        else:
            dic[n] = 1



def is_happy_proc(n):
    digit = 0
    new_number = 0
    while n:
        digit = n%10
        n = n//10
        new_number += digit*digit
    return new_number


if __name__ == "__main__":
    print(is_happy(19))