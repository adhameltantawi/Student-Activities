# Problem: Python String Split and Join
# Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# Approach: Split the input on whitespace and join with '-'.
# Time Complexity: O(n)
# Space Complexity: O(n)

#problem 1
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    return "-".join(line.split())
    
if __name__ == '__main__':    
  line = input()    
  result = split_and_join(line)    
  print(result)
