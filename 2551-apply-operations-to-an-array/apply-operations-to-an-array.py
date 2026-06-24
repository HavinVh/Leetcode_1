class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i,j=0,1
        while j<len(nums):
            if nums[i]==nums[j]:
                nums[i]=2*nums[i]
                nums[j]=0
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        i=j=0
        while j<len(nums):
            if nums[j]==0:
                j+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
        return nums
      

                