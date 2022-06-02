import heapq
from tempfile import SpooledTemporaryFile


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    # No matter what, the output is a 2D array
    # Each array within the array are grouped by strings
    # that are anagrams of each other
    # Use a hashmap to organize the letter with the quantity,
    # but also to group which strings go with each other
    # Step 1 - sort the word/string
    # Step 2 - check if sorted word is in dict key, if not add as key
    # and put the string as a value in a list.
    # Step 3 - Return all values in dict in an array

    # strings = ["eat","tea","tan","ate","nat","bat"]
    if len(strings) == 0:
        return strings

    anagram_dict = {}
    for word in strings:
        sorted_string = "".join(sorted(word))
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = [word]
        else:
            anagram_dict[sorted_string].append(word)
    return list(anagram_dict.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    if len(nums) == 0:
        return nums

    heap = []
    frequent_num_dict = {}
    for num in nums:
        if num not in frequent_num_dict:
            frequent_num_dict[num] = 1
        else:
            frequent_num_dict[num] += 1

    top_k_result = []
    for num, count in frequent_num_dict.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    while len(heap):
        top_k_result.append(heapq.heappop(heap)[1])
    return top_k_result


def valid_sudoku(table):
    """ This method will return true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """

    row_digits = {}
    column_digits = {}
    # this takes care of row and column duplication
    for i in range(len(table)):
        for j in range(len(table[i])):
            value = table[i][j]
            if value == ".":
                continue
            if value not in row_digits:
                row_digits[value] = [i]
            else:
                if i in row_digits[value]:
                    return False
                else:
                    row_digits[value].append(i)
            if value not in column_digits:
                column_digits[value] = [j]
            else:
                if j in column_digits[value]:
                    return False
                else:
                    column_digits[value].append(j)

    # this takes care of each 3 X 3 sub-grids
    grid_digits = {}
    for i in range(len(table)):
        for j in range(len(table[i])):
            value = table[i][j]
            if value != ".":
                if (i // 3, j // 3) in grid_digits:
                    return False
                else:
                    grid_digits[(i // 3, j // 3)] = value
            return True
