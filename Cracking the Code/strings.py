def isPalindromic(s):
    i = 0
    j = len(s)-1
    while i<j:
        if i < j and s[i] != s[j]:
            return False
        i = i+1
        j = j-1
    
    return True



if __name__ == "__main__":
    assert isPalindromic('abcecba'), "Palindrome failed!" 
    assert isPalindromic('abcefcba') == False, "Palindrome failed!" 
    
    