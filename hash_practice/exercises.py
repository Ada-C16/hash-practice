
from collections import defaultdict
import bisect


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: say that s is the length of an input string
        Time Complexity: O(n * slog(s)) because I sort each string
        Space Complexity: O(n)
    """
    fd = {}
    for s in strings:
        # time complexity O(n*len(s)log(len(s)))
        # because it takes time to sort them
        # maybe I could use a set somehow, but I still need a unique key
        # set cant be a key
        # nope bc then "aca" and "acc" would have the same set
        sorted_s = "".join(sorted(s))
        if fd.get(sorted_s):
            fd[sorted_s].append(s)
        else:
            fd[sorted_s] = [s]

    result = []
    # O(n) worst case
    for l in fd.values():
        result.append(l)
    
    return result

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    fd = defaultdict(int)
    for num in nums:
        # time: O(n)
        # space: O(n)
        fd[num] += 1

    result = sorted(fd, key=lambda x : fd[x], reverse=True)
    # probably O(n log(n)) in worst case for time, if frequency is 1 for everything
    # O(n) for space, another list
    # Can I make this better? maybe by storing/updating the k highest
    # frequencies as I build the fd? Notes say I can make it better...
    # not sure how to do that bc the frequencies change

    return result[:k]
    
def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1) constant bc its O(9*9) or O(81) no matter what
        Space Complexity: O(1) constant bc its O(9*3) or O(27)
    """

    # check rows and columns
    for i in range(9):
        row = table[i]
        column = []
        for k in range(9):
            column.append(table[k][i])
            # check each subgrid
            if i%3 == 0 and k%3 == 0:
                subgrid = make_l_from_square(table, i, k)
                subgrid_fd = make_fd(subgrid)
                if not is_valid_fd(subgrid_fd):
                    return False

        row_fd = make_fd(row)
        column_fd = make_fd(column)
        if (not is_valid_fd(row_fd)) or (not is_valid_fd(column_fd)):
            return False

    # no invalid things
    return True

def make_l_from_square(table, row_start, column_start):
    result = []
    for row in range(row_start, row_start+3):
        for column in range(column_start, column_start+3):
            result.append(table[row][column])
    return result


def make_fd(l):
    result = {}
    for num in l:
        result[num] = 1 if not result.get(num) else result[num] + 1
    return result

def is_valid_fd(fd):
    for key, value in fd.items():
        if key == ".":
            continue
        if value > 1:
            return False
    return True

