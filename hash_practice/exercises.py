
import numbers


def grouped_anagrams(strings):
    """ 
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    anagram_dict = {}

    for word in strings: 
        list_of_letters = list(word)
        list_of_letters.sort()
        key = "".join(list_of_letters) 

        if word not in anagram_dict:
            anagram_dict[key] = anagram_dict.get(key,[])
            anagram_dict[key].append(word)
        else:
            anagram_dict[key].append(word)
    
    list_words_same_letters = []

    for value in anagram_dict.values():
        list_words_same_letters.append(value)
    return list_words_same_letters


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """

    frequency_map = {}
    if not nums:
        return []
    if len(nums) == len(set(nums)):
        return nums

    for number in nums:
        if frequency_map.get(number):
            frequency_map[number] +=1
        else:
            frequency_map[number] =1

    sorted_map = sorted(frequency_map.keys(), key=frequency_map.get, reverse=True)
    return sorted_map[0:k]

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

