# Problem: Plus One
# Link: https://leetcode.com/problems/plus-one/
# Approach:
# - Traverse the digits from right to left.
# - Convert trailing 9s into 0s because adding 1 to 9 produces a carry.
# - When a non-9 digit is found, increment it and stop.
# - If all digits are 9, insert 1 at the beginning (e.g., 999 → 1000).
# - This approach modifies the list in-place without creating extra copies.
#
# Time Complexity: O(n)    # We may traverse all digits once in the worst case
# Space Complexity: O(1)   # No extra space is used aside from a few variables

class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1

        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i >= 0:
            digits[i] += 1
        else:
            digits.insert(0, 1)

        return digits