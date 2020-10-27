'''
Tips for Strings:
1. Write values from the back
2. string library in Python:
    s.lower(), s.upper()
    s.strip()
    s.isalpha(), s.isdigit(), s.isspace()
    s.startswith('other'), s.endswith('other') 
    s.find('other')
    s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
    s.split('delim') 
    delim.join(list_of_strings) 
'''

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

    
    