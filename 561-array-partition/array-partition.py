class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        j=1
        s=0
        while j<len(nums):
            
            s=s+min(nums[i],nums[j])
            i+=2
            j+=2
        return s

