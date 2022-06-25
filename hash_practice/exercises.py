
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """

    def create_freq_table(string):
        new_table = {}
        new_table["word"] = string
        for char in string:
            if char in new_table:
                new_table[char] += 1
            else:
                new_table[char] = 1
        return new_table
    def is_anagram(string, table):
        table_copy = table.copy()
        for char in string:
            if char in table_copy:
                if table_copy[char] > 0:
                    table_copy[char] = table_copy[char] - 1
                    continue
                else:
                    return False
            else:
                return False
        return True
    if len(strings) == 0:
        return []
    array_of_hashmaps = []
    output_array = []
    for string in strings:
        array_of_hashmaps.append(create_freq_table(string))
    for string in strings:
        temp_array = []
        for hashmap in array_of_hashmaps:
            if is_anagram(string, hashmap) == True:
                temp_array.append(hashmap["word"])
        output_array.append(temp_array)
    
    output_array_copy = [output_array[0]]
    for list in output_array:
        if list in output_array_copy:
            continue
        else:
            output_array_copy.append(list)

    return output_array_copy

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    def make_freq_map(nums):
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] +=1
            else:
                freq_map[num] = 1
        return freq_map
    
    def sort_freq_map(freq_map, k):
        k_list = []
        for key,value in freq_map.items():
            if len(k_list) < k:
                k_list.append((key,value))
            else:
                for pair in k_list:
                    if value > pair[1]:
                        k_list.remove(pair)
                        k_list.append((key,value))
                        break
        return k_list
    
    freq_map = make_freq_map(nums)
    return sort_freq_map(freq_map,k)


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass

