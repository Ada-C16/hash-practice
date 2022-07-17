
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    anagrams = {}
    for string in strings:
        sorted_string = sorted(string)
        joined_string = ''.join(sorted_string)
        if joined_string in anagrams:
            anagrams[joined_string].append(string)
        else:
            anagrams[joined_string] = [string]
    anagram_list = []
    for key in anagrams.keys():
        anagram_list.append(anagrams[key])
    return anagram_list

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] in nums_dict:
            nums_dict[nums[i]] += 1
        else:
            nums_dict[nums[i]] = 1
 
    frequency_dict={}    
    max_value = 0
    for key, value in nums_dict.items():
        if frequency_dict.get(value):
            frequency_dict[value].append(key)
        else:
            frequency_dict[value] = [key]
        
        if value > max_value:
            max_value = value
    final_list = []
    for i in range(k):
        frequency_nums = frequency_dict.get(max_value - i)
        if frequency_nums:
            check_next = 0
            for num in frequency_nums:
                if check_next + i < k:
                    final_list.append(num)
                else:
                    break
                check_next += 1
    return final_list


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

