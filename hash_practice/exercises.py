
from audioop import reverse
from copy import copy
from curses import keyname
from tabnanny import check


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    if not strings:
        return strings

    lists_of_anagrams = []
    list_of_dicts = []

    for string in strings:
        word_dict = {}
        for letter in string:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
        if word_dict not in list_of_dicts:
            list_of_dicts.append(word_dict)
            lists_of_anagrams.append([string])
        else:
            index = list_of_dicts.index(word_dict)
            lists_of_anagrams[index] += [string]

    return lists_of_anagrams


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    if not nums:
        return nums
    
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    if len(freq_map) == k:
        return nums

    holding = []

    for key, value in freq_map.items():
        holding.append((key, value))
    
    holding.sort(key = lambda x: x[1], reverse=True)
    
    result = []

    for tuple in holding:
        result.append(tuple[0]) 

    return result[:k]
    



def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Not the cleanest solution, since I am checking every value in the table
        three times, but I got it working!
    """

    for row in table:
        row_validity = check_section(row)
        if not row_validity:
            return False

    columns = []
    column = 9

    while column > 0:
        current_column = []
        for row in table:
            if row[column-1] != '.':
                current_column.append(row[column-1])
        columns.append(current_column)
        column -= 1
    
    for column in columns:
        column_validity = check_section(column)
        if not column_validity:
            return False

    sub_grids = {}
    row_count = 9
    column_count = 9

    for row in range(row_count):
        for col in range(column_count):
            placement = row // 3 + col // 3
            if row > 2:
                placement += 3
            if row > 5:
                placement += 3

            if table[row][col] != '.':
                
                if placement in sub_grids:
                    sub_grids[placement] += [table[row][col]]
                else:
                    sub_grids[placement] = [table[row][col]]

    for value in sub_grids.values():
        holding_set = set()
        for num in value:
            if num not in holding_set:
                holding_set.add(num)
            else:
                return False
    
    return True

def check_section(section):
    holding_set = set()
    for i in section:
        if i != ".":
            if i in holding_set:
                return False
            else:
                holding_set.add(i)
    return True