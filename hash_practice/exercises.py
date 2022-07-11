
def grouped_anagrams(words):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """

    array = []
    dic = {}
    for word in words:
        char_in_words_sum = 0
        for char in word:
            char_in_words_sum += ord(char)
        if char_in_words_sum in dic:
            dic[char_in_words_sum].append(word)
        else:
            dic[char_in_words_sum] = [word]
            # print(dic)
    for key in dic:
        array.append(dic[key])

    return array

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    dic = {}
    results_list = []
    for element in nums:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    dic_values_list = (list(dic.values()))
    dic_values_list.sort(reverse=True)
    k_dic_values_list = dic_values_list[:k]

    for key, value in dic.items():
        if value in k_dic_values_list:
            results_list.append(key)

    return results_list


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

