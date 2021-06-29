# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #5
# Date: 6/29/20

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area(rect):

    x1 = int(rect[0])
    x2 = int(rect[2])
    y1 = int(rect[1])
    y2 = int(rect[3])

    length = y2 - y1
    width = x2 - x1
    area = length * width

    return area

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectanlge. return (0, 0, 0, 0) if there is no overlap


def overlap(rect1, rect2):

    r1x1 = rect1[0]
    r1y1 = rect1[1]
    r1x2 = rect1[2]
    r1y2 = rect1[3]

    r2x1 = rect2[0]
    r2y1 = rect2[1]
    r2x2 = rect2[2]
    r2y2 = rect2[3]

    leftX = r1x1
    if r2x1 > leftX:
        leftX = r2x1

    rightX = r1x2
    if r2x2 < rightX:
        rightX = r2x2

    if rightX <= leftX:
        return(0, 0, 0, 0)

    topY = r1y2
    if r2y2 < topY:
        topY = r2y2

    bottomY = r1y1
    if r2y1 > bottomY:
        bottomY = r2y1

    if topY <= bottomY:
        return(0, 0, 0, 0)

    return (leftX, bottomY, rightX, topY)

# Input: bldg is a rectangle in the form of a tuple of 4 integers representing the whole office space cubicles is a list of tuples of 4 integers representing
# all the requested cubicles
# Output: a single integer denoting the area of the unallocated space in the office


def unallocated_space(bldg, cubicles):

    bx1 = bldg[0]
    bx2 = bldg[2]
    by1 = bldg[1]
    by2 = bldg[3]

    length = by2 - by1
    width = bx2 - bx1

    n = len(cubicles)

    matrix = [[0 for i in range(length)] for j in range(width)]

    for k in range(n):
        cubicle = cubicles[k]
        cx1 = cubicle[0]
        cx2 = cubicle[2]
        cy1 = cubicle[1]
        cy2 = cubicle[3]

        for j in range(cy1, cy2):
            for i in range(cx1, cx2):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 1:
                    matrix[i][j] = -1

    count = 0
    for j in range(length):
        for i in range(width):
            if matrix[i][j] == 0:
                count += 1
    return count


# Input: bldg is a rectangle in the form of a tuple of 4 integers representing the whole office space cubicles is a list of tuples of 4 integers representing
# all the requested cubicles
# Output: a single integer denoting the area of the contested space in the office
def contested_space(bldg, cubicles):

    bx1 = bldg[0]
    bx2 = bldg[2]
    by1 = bldg[1]
    by2 = bldg[3]

    length = by2 - by1
    width = bx2 - bx1

    n = len(cubicles)

    matrix = [[0 for i in range(length)] for j in range(width)]

    for k in range(n):
        cubicle = cubicles[k]
        cx1 = cubicle[0]
        cx2 = cubicle[2]
        cy1 = cubicle[1]
        cy2 = cubicle[3]

        for j in range(cy1, cy2):
            for i in range(cx1, cx2):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 1:
                    matrix[i][j] = -1

    count = 0
    for j in range(length):
        for i in range(width):
            if matrix[i][j] == -1:
                count += 1
    return count

# Input: rect is a rectangle in the form of a tuple of 4 integers representing the cubicle requested by an employee cubicles is a list of tuples of 4 integers
# representing all the requested cubicles
# Output: a single integer denoting the area of the uncontested space in the office that the employee gets


def uncontested_space(rect, cubicles):

    bx1 = rect[0]
    bx2 = rect[2]
    by1 = rect[1]
    by2 = rect[3]

    length = by2 - by1
    width = bx2 - bx1

    n = len(cubicles)

    matrix = [[0 for i in range(length)] for j in range(width)]

    for k in range(n):
        cubicle = cubicles[k]
        cx1 = cubicle[0]
        cx2 = cubicle[2]
        cy1 = cubicle[1]
        cy2 = cubicle[3]

        for j in range(cy1, cy2):
            for i in range(cx1, cx2):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 1:
                    matrix[i][j] = -1

    count = 0
    for j in range(length):
        for i in range(width):
            if matrix[i][j] == 1:
                count += 1
    return count


def guaranteed_space(rect, cubicles):

    bx1 = rect[0]
    bx2 = rect[2]
    by1 = rect[1]
    by2 = rect[3]

    length = by2 - by1
    width = bx2 - bx1

    n = len(cubicles)

    matrix = [[0 for i in range(length)] for j in range(width)]

    for k in range(n):
        cubicle = cubicles[k]
        cx1 = cubicle[0]
        cx2 = cubicle[2]
        cy1 = cubicle[1]
        cy2 = cubicle[3]

        for j in range(cy1, cy2):
            for i in range(cx1, cx2):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 1:
                    matrix[i][j] = -1

    spaces = []
    for k in range(n):
        cubicle = cubicles[k]
        cx1 = cubicle[0]
        cx2 = cubicle[2]
        cy1 = cubicle[1]
        cy2 = cubicle[3]

        count = 0
        for j in range(cy1, cy2):
            for i in range(cx1, cx2):
                if matrix[i][j] == 1:
                    count += 1
        spaces.append(count)

    return spaces


def main():

    inpt = "33 26 3 Alice 2 3 10 11 Ted 7 2 18 8 GreedyBob 17 11 30 24"
    nums = inpt.split()
    width = int(nums[0])
    length = int(nums[1])
    numEmployees = int(nums[2])

    index = 3
    cubicles = []
    for i in range(numEmployees):
        rect = (int(nums[index+1]), int(nums[index+2]),
                int(nums[index+3]), int(nums[index+4]))
        index += 5
        cubicles.append(rect)

    building = (0, 0, width, length)

    unallocate = unallocated_space(building, cubicles)
    print(unallocate)

    g = guaranteed_space(building, cubicles)
    n = len(g)
    index = 3
    for i in range(n):
        count = g[i]
        name = nums[index]
        index += 5
        tmpStr = name + ": " + str(count) + "\n"
        print(tmpStr)


if __name__ == "__main__":
    main()
