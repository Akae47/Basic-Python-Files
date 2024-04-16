# File: MyListFunctions.py
# Student: Akwawo EKpu
# UT EID: ace2453
# Course Name: CS303E
#
# Date:03/24/23
# Description of Program: This is a program that uses a list of functions to manipulate strings.

def myAppend(lst, x):
    return lst + [x]

def myExtend(lst1,lst2): 
    return lst1 + lst2

def myMax(lst):
    if not lst:
        print("Empty list: no max value")
        return None
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum


def mySum(lst):
    total = 0
    for i in lst:
        total += i
    return total


def myCount(lst, x):
    count = 0
    for things in lst:
        if things == x:
            count += 1
    return count


def myInsert(lst, i, x):
    if (i < 0) or (i > len(lst)):
        print("Invalid index")
        return None
    lists = lst[:i]
    lists.append(x)
    lists.extend(lst[i:])
    return lists


def myPop(lst, i):
    if i < 0 or i >= len(lst):
        print("Invalid index")
        return lst, None
    removed = lst[i]
    new = lst[:i] + lst[i+1:]
    return new, removed


def myFind(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1   # x was not found in the list



def myRFind(lst, x):
    for i in range(len(lst)-1, -1, -1):  
        if lst[i] == x:
            return i
    return -1



def myFindAll(lst, x):
    ind = []
    for i in range(len(lst)):
        if lst[i] == x:
            ind.append(i)
    return ind

def myReverse(lst):
    return lst[::-1]

def myRemove(lst, x):
    try:
        lst.remove(x)
        return lst
    except ValueError:
        return lst

def myRemoveAll(lst, x):
    while x in lst:
        lst.remove(x)
    return lst


def mySlice(lst, i, j):
    if i < 0 or j > len(lst):
        print("Illegal index value")
    else:
        splicelst = []
        for k in range(i, j):
            splicelst.append(lst[k])
        return splicelst
    

