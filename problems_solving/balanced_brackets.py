def balanced_brackets(s):
    """
        Types of brackets are ({[]}).
        Return true if brackets are even and if not returns false.
        ASCII table was used to solve this problem since closing brace is always 1 or 2 position after the opening brace. 
        So the difference between the ASCII code of the closing brace and the opening brace equals 1 or 2.
    """
    # If size of the input string is not even number then return False
    if len(s)%2!=0:
        print("Input's length is not an even number.")
        return False

    left_stack = []
    
    for x in range(len(s)//2):
        left_stack.append(s[x])

    for x in range(len(s)//2, len(s)):
        top = left_stack.pop()
        if ord(s[x]) - ord(top)  not in range(1,3):
            print("brackets not matching. Opening is %s(%d) and closing is %s(%d)." % (top, ord(top), s[x], ord(s[x])))
            return False
    return True


if __name__ == "__main__":
    balanced_bracke_string = "[[[({[[([(([[[[[({})]]]]]))])]]})]]]"
    unbalanced_bracke_string = "[[[({[[([[[[({})]]]]]))])]]})]]]"
    print(balanced_bracke_string + (" is balanced" if balanced_brackets(balanced_bracke_string) else " is NOT balanced"))
    print(unbalanced_bracke_string + (" is balanced" if balanced_brackets(unbalanced_bracke_string) else " is NOT balanced"))