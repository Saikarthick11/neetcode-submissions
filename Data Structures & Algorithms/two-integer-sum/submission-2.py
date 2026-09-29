class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #solution 1
        # s=list()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+nums[j])==target:
        #             return [i,j]
                
        # return []

        #solution 2
        group={}
        for i in range(len(nums)):
            needed_value=target-nums[i]
            if needed_value in group:
                return [group[needed_value],i]
            else:
                group[nums[i]]=i
        return []