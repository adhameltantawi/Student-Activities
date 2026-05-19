# Problem: Day of the Year
# Link: https://leetcode.com/problems/day-of-the-year/description/
# Approach: 
# - Parse the date into year, month, and day.
# - Use a list of days in each month, adjusting February for leap years.
# - Sum days of previous months and add the current day.
# Time Complexity: O(1) — fixed number of operations.
# Space Complexity: O(1) — constant extra space.

class Solution(object):
    def dayOfYear(self, date):
        y, m, d = map(int, date.split('-'))

        days_in_month = [31, 28 + self.is_leap(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return sum(days_in_month[:m-1]) + d

    def is_leap(self, year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)