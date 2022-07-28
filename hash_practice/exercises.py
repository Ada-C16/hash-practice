
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(nlogn)? Not sure on this
        Space Complexity: 0(n)
    """
    anagrams_dict = {}

    for word in strings:
        sorted_string = ''.join(sorted(word))

        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string].append(word)
        else:
            anagrams_dict[sorted_string] = [word]

    return list(anagrams_dict.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: 0(n)
        Space Complexity: 0(n)
    """
    nums_dict = {}

    if not nums:
        return []

    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    most_common_list = sorted(nums_dict, key=nums_dict.get, reverse=True)
    return most_common_list[:k]


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

