from collections import defaultdict 
from heapq import nlargest 

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n * m), where n = length of strings array,  
        and m = length of each string in the array
        Note -- I'm not sure. Could you comment on this, please? Thank you!
        Space Complexity: O(n)
    """
    anagrams = defaultdict(list)

    for string in strings: 
      sorted_string = ''.join(sorted(list(string))) 
      anagrams[sorted_string].append(string)

    return list(anagrams.values())

# helper method for top_k_frequent_elements
def frequency_dict(nums):
  freq_dict = defaultdict(int)
  for num in nums:
      freq_dict[num] += 1
  return freq_dict
  
def top_k_frequent_elements_with_hash(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n) due to sorting 
        Space Complexity: O(n)
    """
    if k > len(nums):
      return []

    # make a frequency dictionary 
    freq_dict = frequency_dict(nums)

    # sort by value w/ highest values occurring first 
    sorted_by_most_common = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True) 

    # return the k number of values that are the most common 
    return [sorted_by_most_common[i][0] for i in range(k)]


def top_k_frequent_elements(nums, k): 
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(k log n) -- made slightly better w/ heap 
        Space Complexity: O(n)
    """
    if k > len(nums):
      return []

    # make a frequency dictionary 
    freq_dict = frequency_dict(nums)

    # use a heap to return the k largest keys 
    return nlargest(k, freq_dict.keys(), key=freq_dict.get)


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)
    quadrant_dict = defaultdict(set)

    for i in range(9):
        for j in range(9):
            num = table[i][j]
            if num == '.':
                continue
            if num in row_dict[i] or \
                num in col_dict[j] or \
                num in quadrant_dict[i//3*3 + j//3]:
                    return False
            row_dict[i].add(num)
            col_dict[j].add(num)
            quadrant_dict[i//3*3 + j//3].add(num)
        
    return True