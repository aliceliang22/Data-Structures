# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #3
# Date: 6/19/20

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):

    tuples_list.sort(key=lambda x: x[0])

    newTupList = []
    for i in range(len(tuples_list)):
        tup = tuples_list[i]
        overlap = True

        if len(newTupList) == 0:
            newTupList.append(tup)
        else:
            for j in range(len(newTupList)):
                newTup = newTupList[j]

                if tup[1] < newTup[0]:
                    newTupList.insert(j, tup)
                    overlap = False
                    break

                # check if tup and newTup overlap
                overlap = check_overlap(tup, newTup)
                if overlap == True:
                    newInterval = collapse_interval(tup, newTup)
                    newTupList.remove(newTup)
                    newTupList.insert(j, newInterval)
                    break

                if j == len(newTupList) - 1:
                    newTupList.append(tup)

    return newTupList


def check_overlap(tup1, tup2):

    if tup1[0] > tup2[1] or tup1[1] < tup2[0]:
        return False
    else:
        return True


def collapse_interval(tup1, tup2):

    min = tup1[0]
    max = tup1[1]
    if tup2[0] < min:
        min = tup2[0]
    if tup2[1] > max:
        max = tup2[1]

    return (min, max)

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval


def sort_by_interval_size(tuples_list):

    tuples_list.sort(key=lambda x: x[0])

    newTupList = []
    for i in range(len(tuples_list)):
        tup = tuples_list[i]

        if len(newTupList) == 0:
            newTupList.append(tup)
        else:
            for j in range(len(newTupList)):
                newTup = newTupList[j]

                if tup[1] - tup[0] < newTup[1] - newTup[0]:
                    newTupList.insert(j, tup)
                    break

                if j == len(newTupList) - 1:
                    newTupList.append(tup)

    return newTupList

# Input: no input
# Output: a string denoting all test cases have passed


def test_cases():

    # write your own test cases
    assert merge_tuples([(1, 2)]) == [(1, 2)]
    assert merge_tuples([(14, 17), (-8, -5), (26, 29), (-20, -15), (12, 15), (2, 3), (-10, -7), (25, 30), (2, 4), (-21, -16),
                        (13, 18), (22, 27), (-6, -3), (3, 6), (-25, -14)]) == [(-25, -14), (-10, -3), (2, 6), (12, 18), (22, 30)]
    assert merge_tuples([(12, 15), (-10, -3), (6, 7), (25, 40), (4, 6),
                        (9, 12), (13, 14)]) == [(-10, -3), (4, 7), (9, 15), (25, 40)]
    assert merge_tuples([(-9, -3), (-10, -5), (1, 2), (1, 3),
                        (4, 6)]) == [(-10, -3), (1, 3), (4, 6)]

    # write your own test cases
    assert sort_by_interval_size([(1, 3), (4, 5)]) == [(4, 5), (1, 3)]
    assert sort_by_interval_size([(-25, -14), (-10, -3), (2, 6), (12, 18), (22, 30)]) == [
        (2, 6), (12, 18), (-10, -3), (22, 30), (-25, -14)]
    assert sort_by_interval_size(
        [(-10, -3), (4, 7), (9, 15), (25, 40)]) == [(4, 7), (9, 15), (-10, -3), (25, 40)]
    assert sort_by_interval_size(
        [(-10, -3), (1, 3), (4, 6)]) == [(1, 3), (4, 6), (-10, -3)]

    return "all test cases passed"


def main():

    # open file intervals.in and read the data and create a list of tuples
    infile = open("intervals.in", "r")
    n = int(infile.readline().strip())

    if n < 1 or n > 100:
        return "invalid N: 1 <= N <= 100"

    tupList = []
    for i in range(n):
        num = infile.readline().strip()
        tmp = num.split()
        try:
            tupList.append((int(tmp[0]), int(tmp[1])))
        except:
            pass

    # merge the list of tuples
    mergeList = merge_tuples(tupList)

    # sort the list of tuples according to the size of the interval
    sort_by_interval_size(mergeList)

    # run your test cases
    print(test_cases())

    # open file intervals.out and write the output list of tuples from the two functions


if __name__ == "__main__":
    main()
