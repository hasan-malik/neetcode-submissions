class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):

            index = ord(s[i].lower()) - ord('a')
            count[index] += 1

            index = ord(t[i].lower()) - ord('a')
            count[index] -= 1

        return not any(count)
