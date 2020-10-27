# Given a list of possibly overlapping intervals, return a new list of intervals 
# where all overlapping intervals have been merged.
# The input list is not necessarily ordered in any way.
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
# you should return [(1, 3), (4, 10), (20, 25)].

def merge_intervals(intervals):
    results = []
    for start, end in sorted(intervals, key=lambda x: x[0]):
        if results and start <= results[-1][1]:
            # if (5, 8) and (4, 10) -> (4, 10)
            new_start = min(start, results[-1][0])
            new_end = max(end, results[-1][1])
            results[-1] = (new_start, new_end)
        else:
            results.append((start, end))
    
    return results

if __name__ == "__main__":
    intervals = [(1,3), (5,8), (4,10), (20,25)]
    L = merge_intervals(intervals)
    print(L)

