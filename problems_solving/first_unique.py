"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[None,2,None,2,None,3,None,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
"""


class FirstUnique:
    def __init__(self, nums: [int]):
        self.dic = {}
        self.counter = 0
        self.index = 0
        self.nums = []
        for x in nums:
            self.add(x)

    def showFirstUnique(self) -> int:
        if len(self.nums) == self.counter:
            return -1
        return self.nums[self.index]

    def add(self, value: int) -> None:
        self.nums.append(value)
        n = len(self.nums)
        if value in self.dic:
            self.dic[value].append(n - 1)
            self.counter += 2 if len(self.dic[value]) == 2 else 1
            self.check_first_unique(n)
        else:
            self.dic[value] = [n - 1]
            self.check_first_unique(n)

    def check_first_unique(self, n) -> None:
        if self.counter < n:
            while len(self.dic[self.nums[self.index]]) > 1:
                self.index += 1
        else:
            self.index = n - 1


def parse_input(input1: [str], input2: [str]) -> [str]:
    obj = None
    if len(input1) != len(input2):
        print(input1)
        print(input2)
        raise Exception("One of the above inputs are invalid")
    output = []
    for i in range(len(input1)):
        if input1[i] == "FirstUnique":
            obj = FirstUnique(input2[i][0])
            output.append(None)
        elif input1[i] == "showFirstUnique":
            output.append(obj.showFirstUnique())
        elif input1[i] == "add":
            obj.add(input2[i][0])
            output.append(None)
        else:
            raise Exception("Invalid Input: " + input1[i])
    return output


if __name__ == "__main__":
    assert parse_input(["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add",
                        "showFirstUnique", "add", "showFirstUnique"], [[[2, 3, 5]], [], [5], [], [2], [], [3], []]) == [None, 2, None, 2, None, 3, None, -1]
    assert parse_input(["FirstUnique", "showFirstUnique",
                        "add", "showFirstUnique"], [[[809]], [], [809], []]) == [None, 809, None, -1]

    assert parse_input(["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add",
                        "showFirstUnique"], [[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []]) == [None, -1, None, None, None, None, None, 17]
