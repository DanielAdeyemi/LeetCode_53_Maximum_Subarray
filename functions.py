class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = globalSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            if(currentSum > globalSum):
                globalSum = currentSum
        return globalSum
