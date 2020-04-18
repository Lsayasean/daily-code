class Solution:
    def smallerNumbersThanCurrent(self, nums):
        results = []
        sortedArr = sorted(nums)
        
        for num in nums:
            results.append(sortedArr.index(num))
        return results