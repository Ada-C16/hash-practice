
from ntpath import join
from sqlalchemy import true


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    word_dict = {}
    for word in strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
            print(f"{word} found in dict")
        else:
            word_dict[sorted_word] = [word]
    result = []
    for k, v in word_dict.items():
        result.append(v)
    return result

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

grouped_anagrams(words)

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n) (This is the result of using the list sort method)
        Space Complexity: O(n)
    """
    if not nums or k < 1:
        return []
    freq_map = {}
    for num in nums:
        freq_map[num] = 1 + freq_map.get(num, 0)
    freq_list = [(num, freq) for num, freq in freq_map.items()]
    freq_list.sort(key = lambda x: x[1], reverse=True)
    top_el = [freq_list[i][0] for i in range(k)]
    return top_el

numbers = [1, 1, 1, 2, 2, 3]
k = 2
# top_k_frequent_elements(numbers, k)


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

