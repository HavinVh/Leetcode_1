class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<(-2**31) or x>((2**31)-1):
            return 0
        if x>=0:
            s=1
        else:
            s=-1
        y=abs(x)
        n=str(y)
        n1=n[::-1]
        answer=int(n1)
        if answer<(-2**31) or answer>((2**31)-1):
            return 0
        fanswer=s*answer
        return fanswer
        