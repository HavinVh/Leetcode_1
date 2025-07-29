class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j,l=m-1,n-1,m+n-1
        while l>-1:
            while i>-1 and j>-1:
                if nums1[i]>nums2[j]:
                    nums1[l]=nums1[i]
                    i-=1
                    l-=1
                else:
                     nums1[l]=nums2[j]
                     j-=1
                     l-=1
            if i>-1 and j<0:
                nums1[l]=nums1[i]
                i-=1
                l-=1
            if j>-1 and i<0:
                nums1[l]=nums2[j]
                j-=1
                l-=1
        return nums1         


        