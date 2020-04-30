# odoo challenge
def r(pwd, fr, to, by):
    return ''.join([pwd[i] for i in range(fr, to, by)])

class Solution():
    def __init__(self):
        self.pwd = [0]*40
    
    def r(self,res,fr,to,by):
        start = fr
        for x in res:
            self.pwd[start] = x
            start += by


if __name__ == "__main__":

    # print(r(pwd, 0, 4, 1)) == "9677"
    # print(r(pwd, 4, 20, 2)) == "122b1820"
    # print(r(pwd, 5, 30, 3))  == "c238a4c50" 
    # print(r(pwd, 5, 40, 4))  == "c63ad9043"
    # print(r(pwd, 6, 40, 6)) =="210184"
    # print(r(pwd, 7, 8, 1)) =="4"
    # print(r(pwd, 10, 40, 3)) == "b32fb9c343"
    # print(r(pwd, 10, 40, 5)) == "b14989"
    # print(r(pwd, 15, 40, 6)) == "1d14f"
    # print(r(pwd, 20, 40, 3)) == "4c5069a"
    s = Solution()
    s.r("9677", 0, 4, 1)
    s.r("122b1820", 4, 20, 2)
    s.r("c238a4c50", 5, 30, 3)
    s.r("c63ad9043", 5, 40, 4)
    s.r("210184", 6, 40, 6)
    s.r("4", 7, 8, 1)
    s.r("b32fb9c343", 10, 40, 3)
    s.r("b14989", 10, 40, 5)
    s.r("1d14f", 15, 40, 6)
    s.r("4c5069a", 20, 40, 3)
    print(''.join([str(elem) for elem in s.pwd]) )

