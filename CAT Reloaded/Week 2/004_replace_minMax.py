# Problem: Replace MinMax (swap min and max elements)
# Link: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M?fbclid=IwAR0FJIKP70xau9iibN2mvxYsLbwYVlkgSnagRBmaJiH7_qU-7yunb0Qj5iE
# Approach: Read the list, find indices of min and max, swap them, then print the list.
# Time Complexity: O(n)
# Space Complexity: O(1) 

n = int(input())
my_list = list(map(int,(input().split())))
listMin = my_list.index(min(my_list))
listMax = my_list.index(max(my_list))
my_list[listMin], my_list[listMax] = my_list[listMax], my_list[listMin]
print (*my_list)