class Solution(object):
    def decompressRLElist(self, nums):
        i = 0
        res = []
        while i < len(nums):
            freq = i 
            val = i + 1
            # extends adds on to a current array, something I learned 
            # also another thing i leanred, in python you can do something like arrray * x and it will pring it that many times
            res.extend([nums[val]] * nums[freq])
            i += 2
        return res
            