
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n * mlogm)
        Space Complexity: O(n^2)
    """
    hash_table = {}
    if not strings:
        return []
    
    for word in strings:
        # sort each word in ascending order
        sorted_words = "".join(sorted(word))
        if sorted_words not in hash_table:
            # add word as a list as the value of the sorted_words key
            hash_table[sorted_words] = [word]
        else:
            hash_table[sorted_words].append(word)
    
    # turn values into a list
    result = list(hash_table.values())

    return result


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    freq_dict = {}
    result = []
    if not nums:
        return []

    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    sorted_list = list(sorted(freq_dict, key=freq_dict.get, reverse=True))
    print(sorted_list)

    for i in range(k):
        result.append(sorted_list[i])

    return result



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

print(top_k_frequent_elements([1, 2, 2, 2, 3, 3, 3], 2))