class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j=0,1
        s=0
        while j<len(nums)-1:
            if nums[i]>nums[j] and nums[j]<nums[j+1] or nums[i]<nums[j] and nums[j]>nums[j+1]:
                i=j
                j+=1
                s+=1
            else:
                j+=1
        return s
            


        