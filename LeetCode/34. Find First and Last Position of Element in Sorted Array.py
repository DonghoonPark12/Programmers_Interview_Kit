class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        if target not in nums:
            return [-1,-1]
        count=0
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
                i+=1
                count+=1
        if count<2:
            res.append(res[-1])
        
        return [res[0],res[-1]]
