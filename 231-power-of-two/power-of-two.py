class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%2!=0:
            if n==1:
                return True
            else:
                return False
        else:
            return n>0 and (n & (n-1) )==0
