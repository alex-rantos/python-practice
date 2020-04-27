def find_missing_letter(chars):
    prev = 0
    for elem in chars:
        if (prev != 0 and prev + 1 != ord(elem)):
            break
        prev = ord(elem)
    return chr(prev + 1)

if __name__ == '__main__':
    assert find_missing_letter(['a','b','c','d','f']) == 'e'
    