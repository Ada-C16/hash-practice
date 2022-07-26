
from http.client import CONTINUE


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    strings_dict = {}
    anagrams_list = []

    for string in strings:
        string_list = list(string)
        string_list.sort()
        alphabetized_string = "".join(string_list)

        if alphabetized_string not in strings_dict.keys():
            strings_dict[alphabetized_string] = []
            strings_dict[alphabetized_string].append(string)
        else: 
            strings_dict[alphabetized_string].append(string)
    
    for value in strings_dict.values():
        anagrams_list.append(value)

    return anagrams_list




def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    # Iterate through nums array 
    # Create a dictionary to track the most common elements
        # key = num, value = tally of num 
    # Create a list --> this will be returned later. Append elements that have the highest tallies.
        # Compare values to each other. If there is a tie, then consider their index in nums array.
        # Compare the length of this list against k.  

    nums_tally = {}
    most_common_nums = []

    for num in nums:
        if num not in nums_tally.keys():
            nums_tally[num] = 1
        else: 
            nums_tally[num] += 1

    for key, value in nums_tally.items():
        if len(most_common_nums) < k:
            if value == nums_tally[key]:
                most_common_nums.append(key)
            elif value > nums_tally[key]:
                most_common_nums.append(key)
            else:
                continue
        else:
            break

    return most_common_nums


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

