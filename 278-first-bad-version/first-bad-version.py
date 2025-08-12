# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        v=1
        f=n
        bad=n
        while v<=f:
            m=(v+f)//2
            if isBadVersion(m):
                bad=m
                f=m-1
            else:
                v=m+1
        return bad
    
        