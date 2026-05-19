# Problem: Missing Number
# https://leetcode.com/problems/missing-number/
# Approach:
# Use the arithmetic series formula. The expected sum of numbers from 0 to n
# is n*(n+1)//2. Subtract the actual sum of nums to find the missing number.
# Time Complexity:  O(n)
# Space Complexity: O(1)

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual