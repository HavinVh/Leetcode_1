class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        a,b=0,k-1
        s=float(10**6)
        while b<len(nums):
            s=min(s,nums[b]-nums[a])
            a,b=a+1,b+1
        return s



