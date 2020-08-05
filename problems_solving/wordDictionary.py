"""Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string 
containing only letters a-z or dot(s) (..). A dot (.) means it can represent any one letter."""


class TrieNode:
    def __init__(self):
        self.data = [None] * (ord('z') - ord('a') + 1)
        self.end = False

    def add(self, char):
        temp = self.data[ord(char) - ord('a')]
        if temp:
            return temp
        else:
            ret = self.data[ord(char) - ord('a')] = TrieNode()
            return ret

    def search(self, char):
        return self.data[ord(char) - ord('a')]

    def searchDFS(self, word):
        for i, c in enumerate(word):
            if c == ".":
                for node in self.data:
                    if node and node.searchDFS(word[i + 1:]):
                        return True
                return False
            else:
                next = self.data[ord(c) - ord('a')]
                return next.searchDFS(word[i + 1:]) if next else False
        return self.end


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.head
        for c in word:
            cur = cur.add(c)
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cur = self.head
        for i, c in enumerate(word):
            if c == ".":
                return cur.searchDFS(word[i:])
            else:
                cur = cur.search(c)
                if not cur:
                    return False
        return cur.end

    def test(self):
        word = "badz"
        l = [["at"], ["and"], ["an"], ["add"]]
        for l in l:
            for w in l:
                self.addWord(w)
        assert obj.search("a") == False
        assert obj.search(".at") == False
        self.addWord("bat")
        assert obj.search(".at") == True
        self.addWord(word)
        assert obj.search(word) == True
        assert obj.search("bad") == False
        assert obj.search(".a..") == True
        assert obj.search("b...") == True
        self.addWord(word + "g")
        assert obj.search("bad") == False
        assert obj.search("b..") == True
        assert obj.search("b...") == True
        assert obj.search("b....") == True
        assert obj.search("badzg") == True
        assert obj.search("badz") == True
        assert obj.search("b.dz.") == True
        self.addWord("a")
        self.addWord("aa")
        self.addWord("a")
        assert obj.search(".") == True
        assert obj.search("..") == True
        assert obj.search(".a") == True
        assert obj.search("a.") == True
        assert obj.search("a") == True


if __name__ == "__main__":
    obj = WordDictionary()
    obj.test()
