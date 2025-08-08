class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        j=0
        i=0
        k=0
        nums1=nums[:n]
        nums2=nums[n:]
        while k<len(nums):
            if k%2==0:
                nums[k]=nums1[i]
                i+=1
            else:
                nums[k]=nums2[j]
                j+=1
            k+=1
        return nums