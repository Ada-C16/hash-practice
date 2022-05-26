from collections import defaultdict

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """

    anagrams_hash = {}
    for word in strings:
        sorted_word = "".join(sorted(word))

        if sorted_word in anagrams_hash:
            anagrams_hash[sorted_word].append(word)
        else:
            anagrams_hash[sorted_word] = [word]

    anagrams_list = list(anagrams_hash.values())

    return anagrams_list

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    k_most_frequent = []
    nums_frequency = {}

    for num in nums:
        if num not in nums_frequency.keys():
            nums_frequency[num] = 1
        else:
            nums_frequency[num] += 1
            
    sorted_vals =  list(sorted(nums_frequency.values())[::-1])
    for i in range(k):
        for key, val in nums_frequency.items():
            if val == sorted_vals[i]:
                k_most_frequent.append(key)
                nums_frequency[key]=0

    return k_most_frequent



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

