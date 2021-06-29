# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #1
# Date: 6/12/20

#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged in a spiral
def create_spiral(dim):

    rows, cols = (dim, dim)
    matrix = [[0 for i in range(cols)] for j in range(rows)]

    centeri = dim // 2
    centerj = centeri
    numOfLoops = dim - centeri
    val = 1
    matrix[centeri][centerj] = val
    for k in range(1, numOfLoops):
        i1 = centeri - k + 1
        i2 = centeri + k - 1
        j1 = centerj - k
        j2 = centerj + k

        for i in range(i1, i2 + 1):
            val += 1
            matrix[i][j2] = val

        for j in range(j2, j1 - 1, -1):
            val += 1
            matrix[i2 + 1][j] = val

        for i in range(i2, i1-1, -1):
            val += 1
            matrix[i][j1] = val

        for j in range(j1, j2+1):
            val += 1
            matrix[i1-1][j] = val

    return matrix

#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number within the range of numbers in
#         the grid
#  Output: sum_sub_grid returns the sum of the numbers (including val)
#          surrounding the parameter val in the grid
#          if val is out of bounds, returns -1


def sum_sub_grid(grid, val):

    row = len(grid)
    for i in range(row):
        col = len(grid[i])
        for j in range(col):
            if grid[i][j] == val:
                i1 = i - 1
                i2 = i + 2
                j1 = j - 1
                j2 = j + 2

                if i1 < 0:
                    i1 = 0
                if i2 > col:
                    i2 = col
                if j1 < 0:
                    j1 = 0
                if j2 > row:
                    j2 = row

                sum = 0
                for ii in range(i1, i2):
                    for jj in range(j1, j2):
                        sum = sum + grid[ii][jj]
                return sum

    return -1


def main():

    # Open file for output
    infile = open("spiral.in", "r")
    outfile = open("spiral.out", "w")
    line = infile.readline()

    number = line.split()
    num = int(number[0])
    value = int(number[1])

    # first number is odd
    if num % 2 != 1:
        num += 1

    # second number in the range 1 and the square of the dimension
    if value < 1 or value > num ** 2:
        outfile.write("-1")
        exit()

    grid = create_spiral(num)

    sum = sum_sub_grid(grid, value)
    sum_str = str(sum)
    outfile.write(sum_str)

    infile.close()
    outfile.close()

    # test correctness of functions
    # print(test_cases())
    # read the dimension of the grid and value from input file
    # test that dimension is odd
    # create a 2-D list representing the spiral
    # find sum of adjacent terms
    # write the sum in the output file


if __name__ == "__main__":
    main()
