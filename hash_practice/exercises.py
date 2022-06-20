
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(nk log k)
        Space Complexity: O(n)

    """
    """ not sure why split() doesn't work:
    # for word in strings:
    #     split_word ="".join(word.split("").sort()) #aet
    """
    new_group_words = []
    word_dict = {}

    for word in strings:
        split_word = []
        for char in word:
            split_word.append(char)
            split_word.sort()
        sorted_word = "".join(split_word)
        if sorted_word not in word_dict:
            word_list = [word]
            word_dict[sorted_word] = word_list  # aet: [eat, tea]
            new_group_words.append(word_list)
        else:
            word_dict[sorted_word].append(word)  # [eat, tea].append()

    return new_group_words


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nk)
        Space Complexity: O(n)
    """
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    sorted_values = list(num_dict.values())
    sorted_values.sort(reverse=True)
    new_array = sorted_values[:k]
    new_list = []
    for key, value in num_dict.items():
        if value in new_array:
            new_list.append(key)

    return new_list


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
