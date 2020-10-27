# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

def count_islands(M):
    n_rows = len(M)
    n_cols = len(M[0])
    count = 0

    # Traverse through the array and look for 1. Call it x
    # After a trace, all surrounding 1's of x is filled by 0. Add 1 to count
    # Move to the next non-zero element
    for i in range(n_rows):
        for j in range(n_cols):
            if M[i][j] == 1:
                trace(M, i, j, n_rows, n_cols)
                count += 1
    return count


def trace(M, i, j, n_rows, n_cols):
    '''
    Detect 1 and its surround 1's. Filled them all with zero.
    '''

    if i<0 or j<0 or i>=n_rows or j>=n_cols:
        return 

    M[i][j] = 0 # Fill with 0 the "current 1"
    moves = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)] # Possible directions

    for i, j in moves:
        # If next cell is 1, continue tracing
        if 0<= i < n_rows and 0<= j< n_cols and M[i][j] == 1:
            trace(M, i, j, n_rows, n_cols)
    return 


if __name__ == "__main__":
    M = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1]
    ]

    print(count_islands(M))