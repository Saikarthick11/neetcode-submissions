class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
        pairs=list(dic.items())
        pairs.sort(key=lambda x: x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(pairs[i][0])
        return result
            

        