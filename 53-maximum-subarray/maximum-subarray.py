class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runningSum=nums[0]
        MaxNow=nums[0]
      
        for i in range(1,len(nums)):
            runningSum=max(nums[i],runningSum+nums[i])
            MaxNow=max(MaxNow,runningSum)
        return MaxNow

