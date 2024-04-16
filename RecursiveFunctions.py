def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )
    
def addToN(n):
    """ Return the sum of the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n == 0:
        return 0
    else:
        return n + addToN(n-1)

def findSumOfDigits(n):
    """ Return the sum of the digits in a non-negative integer. """
    if n < 10:
        return n
    else:
        return n % 10 + findSumOfDigits(n // 10)

# File: RecursiveFunctions.py
# Student: Akwawo Ekpu
# UT EID: ace2453
# Course Name: CS303E
# 
# Date:04/07/2023
# Description of Program: This is a progam made to run some recursive fuunctions. 


def integerToBinary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return integerToBinary(n // 2) + str(n % 2)

def integerToList(n):
    if n < 10:
        return [str(n)]
    else:
        return integerToList(n // 10) + [str(n % 10)]

def isPalindrome(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])

def findFirstUppercase(s):
    if not s:
        return None
    elif s[0].isupper():
        return s[0]
    else:
        return findFirstUppercase(s[1:])

def findLastUppercase(s):
    if not s:
        return None
    elif s[-1].isupper():
        return s[-1]
    else:
        return findLastUppercase(s[:-1])

def findFirstUppercaseIndexHelper(s, index):
    if index < 0 or index >= len(s):
        return -1
    elif s[index].isupper():
        return index
    else:
        return findFirstUppercaseIndexHelper(s, index+1)

def findFirstUppercaseIndex(s):
    return findFirstUppercaseIndexHelper(s, 0)


