# Problem: The Last 2 Digits
# Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Y
# Approach: Multiply all numbers and print the last two digits of the product.
# Time Complexity: O(n)
# Space Complexity: O(n)

#problem 3
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Y

the_numbers = list(map(int,(input().split())))
x = 1
for i in the_numbers:
    x *= i
print(str(x)[-2:])
