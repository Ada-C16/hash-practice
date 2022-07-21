def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    if not strings:
        return []
    res_list = [[strings[0]]]
    dict_list = [create_dict(strings[0])]

    for i in range(1, len(strings)):
        cur_str = strings[i]
        cur_str_dict = create_dict(cur_str)
        if cur_str_dict in dict_list:
            match_index = dict_list.index(cur_str_dict)
            res_list[match_index].append(cur_str)
        else:
            res_list.append([cur_str])
            dict_list.append(cur_str_dict)
    return res_list
                
        
    
def create_dict(word): 
    word_dict = {}
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    return word_dict


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
    """
    
    nums_dict = create_dict(nums) 
    num_freq_tuple_list = []
    for num, freq in nums_dict.items():
        num_freq_tuple_list.append((num, freq))
    num_freq_tuple_list.sort(key=sort_by_tuple_freq, reverse=True)
    res_list = []
    i = 0
    while k > 0 and i < len(num_freq_tuple_list):
        res_list.append(num_freq_tuple_list[i][0])
        i += 1
        k -= 1
    return res_list


def sort_by_tuple_freq(x) :
    return x[1]   
        

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1)
        Space Complexity: O(1)
"""
    for row in range(len(table)):
        if valid_row(row, table) == False:   
            return False
        
        
    for col in range(len(table[0])):
        if valid_col(col, table) == False:
            return False
        
    row = 0
    while row < 9:
        col = 0
        while col < 9:
            if valid_grid(row, col, table) == False:
                return False
            col += 3
        row += 3   
    return True


def valid_grid(start_row, start_col, table):
    num_set = set()
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            digit = table[i][j]
            if check_valid(digit, num_set) is False:
                return False
    return True



def valid_row(cur_row, table):
    num_set = set()
    for digit in table[cur_row]:
        if check_valid(digit, num_set) is False:
            return False
    return True

def valid_col(cur_col, table):
    num_set = set()
    for row in range(len(table)):
        digit = table[row][cur_col]
        if check_valid(digit, num_set) is False:
            return False
    return True
            
                
def check_valid(digit, num_set):     
    if digit != ".":
        if digit in num_set:
            return False
        else:
            num_set.add(digit)
    return True

