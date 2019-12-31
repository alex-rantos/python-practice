HEXADECIMAL = "0123456789ABCDEF"

def rgb(*args):
    hex_representation = []
    for num in args:
        if (num <= 0): 
            hex_representation.append(HEXADECIMAL[0])
            hex_representation.append(HEXADECIMAL[0])
            continue
        if (num >= 255):
            hex_representation.append(HEXADECIMAL[15])
            hex_representation.append(HEXADECIMAL[15])
            continue

        quotient = num
        remainder_hex = []
        while(quotient > 0):
            remainder = quotient % 16 
            remainder_hex.append(HEXADECIMAL[remainder])
            quotient = quotient // 16
            
        if len(remainder_hex) == 1:
            hex_representation.append(str(0))
            hex_representation.append(remainder_hex[0])
        elif len(remainder_hex) == 2:
            # traverse list in reverse
            for elem in remainder_hex[::-1]:
                hex_representation.append(elem)
        else:
            print(remainder_hex)
            raise Exception("Invalid hex")
    return ''.join(hex_representation)

if __name__ == '__main__':
    assert rgb(0,0,0) == "000000"
    assert rgb(1,2,3) == "010203"
    assert rgb(255,255,255) == "FFFFFF"
    assert rgb(254,253,252) == "FEFDFC"
    assert rgb(-20,275,125) == "00FF7D"
    