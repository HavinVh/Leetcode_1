class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        diff=0
        if len(nums)>1:
            i=0
            j=1
            while j<len(nums):
                diff=max(diff,nums[j]-nums[i])
                i+=1
                j+=1
            return diff
        else:
            return 0
