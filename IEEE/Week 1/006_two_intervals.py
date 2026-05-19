# Problem: Two Intervals
# Link: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/X
# Approach: Compute intersection using max of starts and min of ends.
# Time Complexity: O(1)
# Space Complexity: O(1)

# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/X
def solve():
    l1, r1, l2, r2 = map(int, input().split())
    
    intersect_start = max(l1, l2)
    intersect_end = min(r1, r2)
    
    if intersect_start <= intersect_end:
        print(f"{intersect_start} {intersect_end}")
    else:
        print("-1")

if __name__ == "__main__":
    solve()
