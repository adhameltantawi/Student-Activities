# Problem: Missing Number
# Link: https://leetcode.com/problems/missing-number/description/?envType=daily-question&envId=2024-02-20
# Approach: Use sum formula n(n+1)/2 and subtract actual sum of the array.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
