
from collections import defaultdict

def create_string_freq_map(strings):
    """
    Returns a dictionary of dictionaries. 
    Keys are of each string in strings and values of a dictionary 
    that has keys of each letter in the string and values of how many 
    times that letter appears in the string.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    grouped_string_dicts = {}

    for string in strings: 
        string_dict = defaultdict(int)

        for char in string:
            string_dict[char] += 1

        grouped_string_dicts[string] = string_dict

    return grouped_string_dicts

def grouped_anagrams(strings):
    """ 
    Return an array of arrays.
    Each subarray will have strings, which are anagrams of each other.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    grouped_anagrams = []

    if not strings:
        return grouped_anagrams

    grouped_string_dicts = create_string_freq_map(strings)

    for string in strings:
        anagram_array = []
        anagram_array.append(string)

        for word, char_freq_dict in grouped_string_dicts.items():
            if grouped_string_dicts[string] == char_freq_dict and word != string:
                anagram_array.append(word)
                strings.remove(word)

        grouped_anagrams.append(anagram_array)

    return grouped_anagrams

def top_k_frequent_elements(nums, k):
    """ 
    Returns the k most common elements
    In the case of a tie, it will select the first occuring element.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    most_common_nums = []

    if not nums:
        return most_common_nums

    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    while len(most_common_nums) < k:
        most_freq_num = max(freq_map, key = lambda x: freq_map[x])
        most_common_nums.append(most_freq_num)
        del freq_map[most_freq_num]

    return most_common_nums

def valid_sudoku_rows(table):
    """
    Returns true if all rows in a sudoku table are valid.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    for row in table:
        row_set = set()

        for char in row:
            if char not in row_set and char != ".":
                row_set.add(char)
            elif char in row_set:
                return False
            
    return True

def valid_sudoku_columns(table):
    """
    Returns true if all columns in a sudoku table are valid.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    index = 0

    while index < 9: 
        column_set = set()
        
        for row in table:
            if row[index] not in column_set and row[index] != ".":
                column_set.add(row[index])
            
            elif row[index] in column_set:
                return False

        index += 1

    return True

def valid_sudoku_box(table, left_index, right_index, top_index, bottom_index):
    """
    Returns true if 3x3 box, defined by indices in sudoku table, are valid.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    box_set = set()

    for column in range(left_index, right_index + 1):
        for row in range (top_index, bottom_index + 1):
            if table[column][row] not in box_set and table[column][row] != ".":
                box_set.add(table[column][row])
            elif table[column][row] in box_set:
                return False

    return True

def valid_sudoku_boxes(table):
    """
    Returns true if all 3x3 boxes in a sudoku table are valid.
    Time Complexity: O()
    Space Complexity: O()
    """

    # I'm positive I could do this recursively, but my bran is too tired
    top_left_valid = valid_sudoku_box(table, 0, 2, 0, 2)
    top_middle_valid = valid_sudoku_box(table, 3, 5, 0, 2)
    top_right_valid = valid_sudoku_box(table, 6, 8, 0, 2)
    middle_left_valid = valid_sudoku_box(table, 0, 2, 3, 5)
    middle_middle_valid = valid_sudoku_box(table, 3, 5, 3, 5)
    middle_right_valid = valid_sudoku_box(table, 6, 8, 3, 5)
    bottom_left_valid = valid_sudoku_box(table, 0, 2, 6, 8)
    bottom_middle_valid = valid_sudoku_box(table, 3, 5, 6, 8)
    bottom_right_valid = valid_sudoku_box(table, 6, 8, 6, 8)

    return top_left_valid and top_middle_valid and top_right_valid and middle_left_valid and middle_middle_valid and middle_right_valid and bottom_left_valid and bottom_middle_valid and bottom_right_valid
    

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    return valid_sudoku_rows(table) \
        and valid_sudoku_columns(table) \
        and valid_sudoku_boxes(table)
