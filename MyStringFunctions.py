# File: MyStringFunctions.py
# Student: Akwawo Ekpu
# UT EID: ace2453
# Course Name: CS303E
# 
# Date: 05/05/2023
# Description of Program:

def myAppend( s, ch ):
    # Return a new string that is like s but with character ch added at the end
    return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    count = 0
    for c in s:
        if c== ch:
            count+=1
    return count 

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of s1 followed by the elements of s2, in the sameorder they appear in s2.
    result = s1
    for c in s2:
        result += c
    return result
    

def myMin( s ):
    # Return the character in s with the lowest ASCII code. If s is empty, print "Empty string: no min value" and return None.
    if len(s) == 0:
        print("Empty string: no min value")
        return None
    else:
        mini = s[0]
        for c in s:
            if ord(c) < ord(mini):
                mini = c
        return mini

    
    
def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been inserted at the ith position. I.e., the string is now one character longer than before. Print "Invalid index" if i is greater than the length of s and return None.
    if i > len(s):
        print("Invalid index")
        return None
    else:
        return s[:i] + ch + s[i:]
    
    
def myPop( s, i ):
    # Return two results:  1. a new string that is like s but with the ith  element removed; 2. the value that was removed.Print "Invalid index" if i is greater than or equal to len(s), and return s unchanged and None
    if i >= len(s):
        print("Invalid index")
        return s, None
    else:
        cut = s[i]
        return s[:i] + s[i+1:], cut
    
    
def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1
    
def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of ch in s, if any. Return -1 if ch does not occur in s.
    last = -1
    for i in range(len(s)):
        if s[i] == ch:
             last = i
    return last

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch removed. If there is none, return s.
    g = myFind(s,ch)
    for i in range(len(s)):
        if i == g:
            return s[:i] + s[i+1:]
    return s
    
            
            
    
def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.removed. If there are none, return s.
    empty = ""
    for char in s:
        if char != ch:
            empty += char
    print(empty) 


def myReverse( s ):
    # Return a new string like s but with the characters in the reverse order.
    reverse = s[::-1]
    return reverse

    
