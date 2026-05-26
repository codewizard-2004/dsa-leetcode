class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in range(len(nums)):
            f = target - nums[i]
            if f in d:
                return [d[f], i]
            else:
                d[nums[i]] = i
        