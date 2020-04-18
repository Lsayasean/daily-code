class Solution:
    def smallerNumbersThanCurrent(self, nums):
        results = []
        # sorts the array to compare with current array
        sortedArr = sorted(nums)
        
        for num in nums:
            # gives index of array which also lets us know how many numbers are currently smaller than current number
            results.append(sortedArr.index(num))
        return results

        # solution 2, slower 

        res = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            res.extend([count])
        return res