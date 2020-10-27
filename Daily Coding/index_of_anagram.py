"""
@Problem:
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4

---
@Solution:
1. Create frequency list, which can:
    - Counter of each character
    - Increase or decrease the freq of a character
2. Basic idea of the find_anagram is:
    - We run a window, W, through S.
    - The first window is S[:len(W)]. We check if this window is an anagram seperately
    - Slide the window by 1. Do increment for new(end) char, decrement for old(start) char
"""

class FrequencyList:
    def __init__(self, word):
        self.d = {}
        for c in word:
            self.increment(c)
    
    def _create_if_not_exist(self, key):
        if key not in self.d:
            self.d[key] = 0
        return
    
    def _del_if_zero(self, key):
        if self.d[key] == 0:
            del self.d[key]
    
    def increment(self, key):
        self._create_if_not_exist(key)
        self.d[key] += 1
        self._del_if_zero(key)

    def decrement(self, key):
        self._create_if_not_exist(key)
        self.d[key] -= 1
        self._del_if_zero(key)

    def is_empty(self):
        return not self.d
    

def find_anagram(W, S):
    ret = []

    F = FrequencyList(W)

    # check if the first window is an anagram
    for i in range(len(W)):
        F.decrement(S[i])
    if F.is_empty():
        ret.append(0)

    # slide the window by 1 to the end of S
    for i in range(len(W), len(S)):
        # start is old, end is new
        start, end = S[i-len(W)], S[i]
        
        # decrement old, increment new
        F.decrement(start)
        F.increment(end)

        # check if it is anagram
        if F.is_empty():
            # append the beginning index 
            ret.append(i - len(W) + 1)

    return ret


if __name__ == "__main__":
    W = 'ab'
    S = 'abxaba'
    print(find_anagram(W, S))