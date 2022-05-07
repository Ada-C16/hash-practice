
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(log n)
        Space Complexity: O(n)
    """
    anagram = []
    str_map = {}
    for word in strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in str_map:
            str_map[sorted_word] = [word]
        elif sorted_word in str_map:
            str_map[sorted_word].append(word)
    for key,value in str_map.items():
        anagram.append(value)
    return anagram

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not nums:
        return []
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        elif num in num_dict:
            num_dict[num] += 1
    
    max_nums = []
    for i in range(k):
        max_num = 0
        max_freq = 0
        for num, frequency in num_dict.items():
            if frequency > max_freq:
                max_freq = frequency
                max_num = num
        max_nums.append(max_num)
        del num_dict[max_num]
    return max_nums

def list_helper(list):
    table = {}
    for char in list:
        if char != '.':
            if char in table:
                table[char] += 1
            else:
                table[char] = 1

    for value in table.values():
        if value > 1:
            return False
    return True

def grid_helper(list_one, list_two, list_three):
    grid_one = list_one[:3] + list_two[:3] + list_three[:3]
    if not list_helper(grid_one):
        return False
    grid_two = list_one[3:6] + list_two[3:6] + list_three[3:6]
    if not list_helper(grid_two):
        return False
    grid_three = list_one[6:9] + list_two[6:9] + list_three[6:9]
    if not list_helper(grid_three):
        return False
    return True

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1)
        Space Complexity: O(1)
    """
    for i in range(len(table)):
        print('row', table[i])
        if not list_helper(table[i]):
            return False

        column = []
        for j in range(len(table)):
            column.append(table[j][i])
        
        if not list_helper(column):
            return False
    for i in range(0, len(table), 3):
        if not grid_helper(table[i], table[i+1],table[i+2]):
            return False
    return True

