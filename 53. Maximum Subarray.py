class Solution:
    def maxSubArray(self, nums):
        rangeSum=nums[0]
        maxSum=nums[0]
        for n in nums[1:]:
            if rangeSum + n < n:
                rangeSum=n
            else:
                rangeSum+=n
            if rangeSum > maxSum:
                maxSum = rangeSum
        return  maxSum

sln = Solution()
assert 6==(sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
assert -2==sln.maxSubArray([-2])
assert 1==(sln.maxSubArray([-2,1,-3]))
assert 0==(sln.maxSubArray([0,0]))
assert 4==(sln.maxSubArray([-1,1,2,1]))
assert -1==(sln.maxSubArray([-1,-2]))
assert 1==(sln.maxSubArray([1,-2,0]))