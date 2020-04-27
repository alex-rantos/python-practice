CAPITAL_MIN_VALUE = 65
CAPITAL_MAX_VALUE = 90
LOWER_CASE_MIN_VAL = 97
LOWER_CASE_MAX_VAL = 122
def alphabet_position(text):
    res_string = ""
    for c in text:
        if ord(c) in range(CAPITAL_MIN_VALUE,CAPITAL_MAX_VALUE + 1):
            res_string += (str(ord(c) - CAPITAL_MIN_VALUE + 1) + " ")
        
        if ord(c) in range(LOWER_CASE_MIN_VAL,LOWER_CASE_MAX_VAL + 1):
            res_string += (str(ord(c) - LOWER_CASE_MIN_VAL + 1) + " ")

    return res_string[:(len(res_string) - 1)]

if __name__ == "__main__":
    print(alphabet_position("zZThe sunset sets at twelve o' clock."))

"""
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""