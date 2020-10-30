class Solution:
    # The idea to is have a start pointer to track where our substring begins
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            # If the new char is already in the substring
            # The 2nd condition is because we also keep indexes of characters that are already passed (i < start)
            # It means characters whose index < start are essentially not in the unique set.
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # start a new substring at that index
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
    
if __name__ == '__main__':
    solver = Solution()
    s = 'abbcadioaaannndfghutyoqyl'
    print(solver.lengthOfLongestSubstring(s)) # ndfghutyoq = 10