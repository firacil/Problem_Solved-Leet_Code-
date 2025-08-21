from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        height = [0] * n
        
        for i in range(m):
            # build histogram of consecutive 1s
            for j in range(n):
                if mat[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            
            # count submatrices ending at row i
            stack = []
            sum_in_row = [0] * n
            for j in range(n):
                # monotonic stack to keep heights increasing
                while stack and height[stack[-1]] >= height[j]:
                    stack.pop()
                
                if stack:
                    prev = stack[-1]
                    sum_in_row[j] = sum_in_row[prev] + height[j] * (j - prev)
                else:
                    sum_in_row[j] = height[j] * (j + 1)
                
                res += sum_in_row[j]
                stack.append(j)
        
        return res
