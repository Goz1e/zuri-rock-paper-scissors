# # Check if two words are anagrams 
# # Example:
# # find_anagrams("hello", "check") --> False
# # find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    m = list(word)
    n = list(anagram)
    if len(n) == len(m):
        for i in n:
            if i in m:
                return True
            else:
                return False
    else:
        return False

    print(m,n)
    return m
    
find_anagram('belo','elbow')