class Switch(object):

    def get_case(self, i):
        case_name = 'case_'+str(i)
        method = getattr(self, case_name, lambda: 'Invalid')
        return method()

    def case_0(self):
        return 'Case 0 fired'

    def case_1(self):
        return 'Case 1 fired'

    def case_4(self):
        return 4


if __name__ == "__main__":
    s = Switch()
    print(s.get_case(0))
    print(s.get_case(1))
    print(s.get_case(3))
    print(s.get_case(4))
