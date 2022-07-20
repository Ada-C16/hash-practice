
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagram_hash = {}
    anagram_list = []

    for string in strings:
        sorted_string = "".join(sorted(string))

        if anagram_hash.get(sorted_string):
            anagram_hash[sorted_string].append(string)

        else:
            anagram_hash[sorted_string] = [string]

    for string in anagram_hash.values():
        anagram_list.append(string)
    return anagram_list 

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    frequency = {}
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    sorted_hash = sorted(frequency.items(), key=lambda x:(x[1]), reverse=True)
    most_common = []

    for i in sorted_hash:
        most_common.append(i[0])
    return most_common[:k]


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

