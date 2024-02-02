class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m = list(zip(*matrix))
        for i in range(len(matrix)):
            matrix[i] = m[i][::-1]
