class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        
        def binarysearch(self,nums,target,l_p):
            l,r=0,len(nums)-1
            i=-1
            while l<=r:
                m=(l+r)//2
                if target>nums[m]:
                    l=m+1
                elif target<nums[m]:
                    r=m-1
                else:
                    i=m
                    if l_p:
                        r=m-1
                    else:
                        l=m+1
            return i
        left=binarysearch(self,nums,target,True)
        right=binarysearch(self,nums,target,False)
        return [left,right]
        
        
