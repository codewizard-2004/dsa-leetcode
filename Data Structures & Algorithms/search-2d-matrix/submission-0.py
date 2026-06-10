class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False
            
        top = 0
        bottom = len(matrix) - 1
        n = len(matrix[0]) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][n]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                return binSearch(matrix[mid])
        
        return False
        