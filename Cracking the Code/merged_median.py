# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).



def merged_median(L1, L2):
    len1 = len(L1)
    len2 = len(L2)

    L_merged = merge(L1, L2)
    mid = int((len1+len2) / 2)
    
    if (len1+len2)//2 == 1:
        return L_merged[mid]
    else:
        return (L_merged[mid] + L_merged[mid-1]) / 2


def merge(Small, Big):
    # O((N+M)*log(N+M)): Merged = sorted(Small + Big)
    # Insert with binary search: O(NM): traverse across M, insert takes O(N)
    Merge = []
    return Merged



if __name__ == "__main__":
    L1 = [1, 3, 4, 6]
    L2 = [5, 7]
    print(merged_median(L1, L2))
