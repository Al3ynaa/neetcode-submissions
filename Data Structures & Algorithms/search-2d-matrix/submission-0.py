class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=rows*cols -1
        while left<=right:
            mid=(left+right)//2
            row=mid//cols
            column=mid%cols
            value=matrix[row][column]

            if target==value:
                return True
            elif target<value:
                right=mid-1
            else:
                left=mid+1
        return False