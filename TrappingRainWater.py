class Solution(object):
    def trap(self,ele):
        water=0
        n=len(ele)
        left_max=[0]*n
        right_max=[0]*n
        left_max[0]=ele[0]
        right_max[n-1]=ele[n-1]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1],ele[i])
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i+1],ele[i])
        for i in range(n):
            water+=min(left_max[i],right_max[i])-ele[i]
        return water
