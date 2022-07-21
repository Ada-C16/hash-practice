
def create_anagram_key(string):
    return ''.join(sorted(string))


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n*m)
        Space Complexity: O(n)
    """
    grouped_words = {}
    anagrams = []

    for ele in strings:
        if grouped_words.get(create_anagram_key(ele)) == None:
            grouped_words[create_anagram_key(ele)] = [ele]
        else:
            grouped_words[create_anagram_key(ele)].append(ele)

    for k, v in grouped_words.items():
        anagrams.append(v)

    return anagrams


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    frequency_map = {}
    results = []
    for ele in nums:
        if ele in frequency_map:
            frequency_map[ele] += 1
        else:
            frequency_map[ele] = 1

    values_list = list(frequency_map.values())
    values_list.sort(reverse=True)
    k_values_list = values_list[:k]

    for key, value in frequency_map.items():
        if value in k_values_list:
            results.append(key)

    return results


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

