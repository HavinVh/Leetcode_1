class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(0,len(matrix)):#transpose of the matrix
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            for j in range((len(matrix))//2):
                #two pointer
                matrix[i][j],matrix[i][len(matrix)-j-1]= matrix[i][len(matrix)-j-1],matrix[i][j],
                

                
                
        