class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        s=[]
        for i in nums2:
            while s and s[-1]<i:
                popped=s.pop()
                d[popped]=i
            s.append(i)
        ans=[]
        for i in nums1:
            if i in d:
                ans.append(d[i])
            else:
                ans.append(-1)
        return ans

        