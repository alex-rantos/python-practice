"""Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
BEST SOLUTION :
lo, hi = 0, 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)
        return lo == 0
"""
def check_valid_string(s: str) -> bool:
    if not s:
        return True
    balance = 0
    joker_both = 0
    joker_left = 0
    import pdb
    for i,c in enumerate(s):
        print("s:%s || pos:%s & char:%s :: balance: %s, joker_both: %s , joker_left %s" %(s[:i],i,c,balance,joker_both,joker_left))
        if c == "*":
            if balance > 0:
                joker_both += 1
            else: joker_left += 1
        elif c == "(":
            balance += 1
        elif c == ")" and i > 0:
            if balance > 0:
                balance -= 1
            elif balance == 0 and joker_left + joker_both > 0:
                if joker_left:
                    joker_left -= 1
                elif joker_both:
                    joker_both -= 1
                # balance++ and balance--
            elif balance < 0 and joker_both + joker_left > 0:
                if abs(balance) <= joker_left:
                    joker_left = joker_left - 1
                    balance -= 1
                else:
                    return False
            else:
                return False
        else:
            return False
            #raise Exception("Unknown character in input string")
        while joker_both > balance:
            joker_both -= 1
            joker_left += 1
    if balance == 0 or (joker_both >= balance or joker_left + balance >= 0 and balance < 0):
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = "()"
    s2 = "())"
    s3 = "(*))"
    s4 = "(((()"
    s5 = "(((***"
    s6 = "(*))"
    s7 = ")("
    r1 = check_valid_string(s1)
    r2 = check_valid_string(s2)
    r3 = check_valid_string(s3)
    r4 = check_valid_string(s4)
    r5 = check_valid_string(s5)
    r6 = check_valid_string(s6)
    r7 = check_valid_string(s7)
    assert r1 == True
    assert r2 == False
    assert r3 == True
    assert r4 == False
    assert r5 == True
    assert r6 == True
    assert r7 == False
    s8 = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    r8 = check_valid_string(s8)
    assert r8 == False