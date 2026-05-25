class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hash:
                return [hash[target - nums[i]], i]
                
            hash[nums[i]] = i  # value: index
            

        return []



        # slow:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]