class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev_day=stack.pop()
                ans[prev_day]=i-prev_day
            stack.append(i)
        return ans
        