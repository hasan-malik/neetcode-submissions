class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        acc = []

        for string in strs:

            # check if existing anagram sublist exists
            appended = False
            for j in range(len(acc)):
                if Solution.is_anagram(self, acc[j][0], string):
                    acc[j].append(string)
                    appended = True

            if not appended:
                acc.append([string])


        return acc

    def is_anagram(self, str1: str, str2: str) -> bool:

        if len(str1) != len(str2):
            return False

        letters = [0] * 26

        for i in range(len(str1)):

            letters[ord(str1[i]) - ord('a')] += 1
            letters[ord(str2[i]) - ord('a')] -= 1

        return not any(letters)



            



