"""
@Problem: All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.

---
@Solution:
Let's try thinkinkg about this problem recursively. First consider the base cases:

If there are 0 disks, then do nothing, since we are done.
If there is 1 disk, then we can move the single disk from the source peg to the target peg directly.
Now, let's assume we have an existing tower_of_hanoi function that can move n disks from a source peg to a target peg using a spare stack. 
The recurrence would then look like this:
    - If there is more than 1 disk, then we can do the following:
    - Recursively move n - 1 disks from the source stack to the spare stack
    - Move the last (biggest) disk from the source stack to the target stack
    - Recursively move all n - 1 disks from the spare stack to the target stack

---
@Analysis:
This will run in O(2^n) time, since for each call we're recursively calling ourselves twice. 
This should also take O(n) space since the function call stack goes n calls deep.
"""

def tower_of_hn(n, a='1', b='2', c='3'):
    if n == 0:
        return
    if n == 1:
        print("Move {} to {}".format(a,c))
        return
    else:
        tower_of_hn(n-1, a, c, b)
        print("Move {} to {}".format(a, c))
        tower_of_hn(n-1, b, a, c)

if __name__ == "__main__":
    n = int(input("Number of sticks: "))
    tower_of_hn(n)