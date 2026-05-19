# Problem: Swap Case
# Link: https://www.hackerrank.com/challenges/swap-case/problem
# Approach: Swap each character's case and join the result.
# Time Complexity: O(n)
# Space Complexity: O(n)

# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    swaped_list = [i.upper() if i.islower() else i.lower() for i in s]
    return ''.join(swaped_list)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
