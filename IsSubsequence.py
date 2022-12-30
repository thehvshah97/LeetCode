class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if j == len(s):
                return True
        return False


if __name__ == '__main__':
    obj = IsSubsequence()
    print(obj.isSubsequence("b", "abc"))
