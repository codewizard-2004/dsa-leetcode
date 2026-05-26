from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            
            # remove left element if it goes out of bound
            if l > q[0]:
                q.popleft()
            
            #check if we have reached end of window
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res
            

        