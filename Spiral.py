#  File: Spiral.py
#  Student Name: Akwawo Ekpu
#  Student UT EID: ace2453


import sys


# Input: n
# Output:
def get_dimension(in_data):
    pass
    '''##### ADD CODE HERE #####'''
    dimension = input("")
    try:
        num = int(dimension)
        return num
    except ValueError:
        return "Invalid data"


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    pass
    '''##### ADD CODE HERE #####'''
    if n % 2 == 0:
        n += 1
    start = 0
    spiral = 0
    point = 0
    point = (n // 2, n // 2)
    x,y = point
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    arr = [ [0] * n  for _ in range(n)]
    count = 1
    arr[x][y] = count
    for i in range(n+1):
        for j in range(n+1):
            count += 1
            if x <= y and x + y <= n:
                x += 1
                arr[x][y] = count

            elif x < y and x + y >= n:
                y+= 1
                arr[x][y] = count
            
            elif x > y and x + y < n:
                y -= 1
                arr[x][y] = count

            elif x > y and x + y < n:
                x -= 1
                arr[x][y] = count
                
             
            

    return arr
            

            
            
             
    

    
    


# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    pass
    '''##### ADD CODE HERE #####'''


# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    pass
    '''##### ADD CODE HERE #####'''


# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
