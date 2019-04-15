"""
@Problem:
You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, 
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

---
@Solution:
We want to construct a dictionary, in which:
    - keys are location (i,j) of the matrix
    - values are the maximum value we can get at that location
"""

def find_path(M, i, j , cache={}):
    if (i,j) not in cache:
        if i == len(M)-1 and j == len(M[0])-1:
            cache[i,j] = M[i][j]
        elif i == len(M)-1:
            cache[i,j] = M[i][j] + find_path(M, i, j+1, cache)
        elif j == len(M[0])-1:
            cache[i,j] = M[i][j] + find_path(M, i+1, j, cache)
        else:
            cache[i,j] = M[i][j] + max(find_path(M, i+1, j, cache), find_path(M, i, j+1, cache))
            
    # print to see how the dictionary is implemented: 
    # print(cache)
    return cache[i,j]
    
    

if __name__ == "__main__":
    M = [
        [0,3,1,1],
        [2,0,0,4],
        [1,5,3,1]
    ]

    print("Num rows: {} \nNum cols: {}".format(len(M), len(M[0])))
    total = find_path(M, 0, 0)
    print(total)