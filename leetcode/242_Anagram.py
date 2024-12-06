from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        count = defaultdict(int)
        for i in range(n):
            count[s[i]] += 1
            count[t[i]] -= 1

        for k in count:
            if count[k] != 0:
                return False
        return True