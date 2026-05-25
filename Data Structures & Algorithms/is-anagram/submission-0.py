class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        acc1 = {}
        for i in range(len(s)):
            if s[i] in acc1:
                acc1[s[i]] += 1
            else:
                acc1[s[i]] = 1

        acc2 = {}
        for i in range(len(t)):
            if t[i] in acc2:
                acc2[t[i]] += 1
            else:
                acc2[t[i]] = 1

        return acc1 == acc2

        
        