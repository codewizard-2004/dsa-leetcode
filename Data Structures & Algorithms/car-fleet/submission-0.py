class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p, s in zip(position, speed):
            pair.append([p,s])
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p)/ s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # They will collide
                stack.pop()

        return len(stack)