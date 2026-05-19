# Problem: Count Letters (frequency)
# Link: https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J?fbclid=IwAR3kBgECKX2RrvDydVJcJls5Fb7avGJIIfYkPAOXMxSr74TBc9ulf2_cAfE
# Approach: Count occurrences using a dictionary, then print characters in alphabetical order.
# Time Complexity: O(n + k log k) where k is number of distinct characters
# Space Complexity: O(k)s = input()

s = input()
count = {}
for ch in s:
    if ch in count:
        count[ch] +=1
    else:
        count[ch] = 1
for ch in sorted(count):
    print(f"{ch} : {count[ch]}")
        
