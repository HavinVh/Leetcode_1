class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #only the extreme limits are important, 
        l,r=0,len(height)-1
        left,right=height[l],height[r]
        answer=0
        while l<r:
            if left<right:
                l+=1
                left=max(left,height[l])
                answer+=(left-height[l])
            else:
                r-=1
                right=max(right,height[r])
                answer+=(right-height[r])
        return answer


