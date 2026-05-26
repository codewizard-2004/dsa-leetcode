class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        streak = 1
        
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                streak += 1
            elif nums[i] != nums[i + 1]:
                res = max(res, streak)
                streak = 1

        res = max(res, streak)
        return res

        