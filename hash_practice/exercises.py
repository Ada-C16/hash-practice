
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n log (n))
        Space Complexity: O (n)
    """
    anagrams = {}
    for word in strings:
        alphabet = [0] * 26
        for letter in word:
            alphabet[ord(letter.lower())-ord("a")] += 1
        if tuple(alphabet) in anagrams:
            anagrams[tuple(alphabet)].append(word)
        else:
            anagrams[tuple(alphabet)] = [word]
    return_list = []
    for k, v in anagrams.items():
        return_list.append(v)
    return return_list


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    max_keys = sorted(freq_map.keys(), key=freq_map.get, reverse=True)
    return max_keys[0:k]


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
