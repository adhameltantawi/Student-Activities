# Problem: List Comprehensions
# Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Approach: Generate all (i,j,k) triples with i+j+k != n using list comprehension.
# Time Complexity: O((x+1)(y+1)(z+1))
# Space Complexity: O((x+1)(y+1)(z+1))

# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coords = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    
    print(coords)
