class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = [] this will make it O(n2)
        seen = set()  # set lookup is O(1)
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False