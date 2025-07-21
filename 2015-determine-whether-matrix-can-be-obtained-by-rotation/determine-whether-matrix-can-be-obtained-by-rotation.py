class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        mat1=mat
        for k in range(4):
            for i in range(0,len(mat)):#transpose of the matrix
                for j in range(i,len(mat)):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(len(mat)):
                for j in range((len(mat))//2):
                    #two pointer
                    mat[i][j],mat[i][len(mat)-j-1]= mat[i][len(mat)-j-1],mat[i][j]
            if mat==target:
                return True
        else:
            return False      
