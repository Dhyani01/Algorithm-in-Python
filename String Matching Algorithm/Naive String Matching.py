# Naive String Matching
# How it works it matches the input string in text string character by character. 
# Best case O(n) when input string is not there. 
# Worst case is O(M*N).
# KMP matching algorithm improves the worst case to O(n).


"""AABAACAADAABAAABAA
 AABA

""" 
def stringmatch(pattern,text):
    for i in range((len(text)-len(pattern))+1):
        if pattern==text[i:len(pattern)+i]:
            print(" PatternString Found at index ",end=" ")
            print(i)



text=input("Enter Text: ")
pattern=input("Enter Pattern: ")

stringmatch(pattern,text)
