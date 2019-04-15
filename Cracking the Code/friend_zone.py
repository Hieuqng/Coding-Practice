import queue
def count_zones(M):
    '''
    @This function counts number of "islands" in matrix M
    '''
    Q = queue.Queue()
    count = 0
    visited = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
    
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 1 and visited[i][j] == 0:
                count += 1
                Q.put((i,j))

            while not Q.empty():
                r, c = Q.get()
                visited[r][c] = 1
                pos = [ (-1,0), (1,0), (0,-1), (0,1) ]

                for dr, dc in pos:
                    if r+dr < 0 or r+dr >= len(M) or c+dc < 0 or c+dc >= len(M[0]):
                        continue
                    if M[r+dr][c+dc] == 1 and visited[r+dr][c+dc] == 0:
                        Q.put((r+dr, c+dc))

    return count


def count_circle(M):
    '''
    @This function counts number of friend circles (those who have direct or indirect frienship with others)
    '''
    Q = queue.Queue()
    count = 0
    visited = [0 for _ in range(len(M))]
    
    for i in range(len(M)):
        if visited[i] == 0:
            count += 1
            Q.put(i)

        while not Q.empty():
            r = Q.get()
            visited[r] = 1

            for j in range(len(M[0])):
                if M[i][j] == 1 and visited[j] == 0:
                    Q.put(j)   

    return count


if __name__ == "__main__":
    M = [
        [1,1,0,1],
        [1,1,0,0],
        [0,0,1,1],
        [1,0,1,1]
    ]

    print(count_zones(M))
    print(count_circle(M))
