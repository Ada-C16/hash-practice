
def to_dict(word):
    anagram = {}

    for letter in word:
        if letter not in anagram:
            anagram[letter] = 1
        else:
            anagram[letter] += 1

    return anagram


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2) might be O(n^3) because of .sort()
        Space Complexity: O(n)
    """

    # dictionary where the key is a tuple with the letters and key is a list of the element
    print("OG LIST: ", strings)
    result_list = []
    anagram_dict = {}

    if len(strings) == 0:
        return []

    for word in strings:
        letter_list = []
        for letter in word:
            letter_list.append(letter)
            letter_list.sort()
            ordered_word = "".join(letter_list)
        hashed = hash(ordered_word)
        if hashed in anagram_dict:
            anagram_dict[hashed].append(word)
        else:
            anagram_dict[hashed] = [word]

    for value in anagram_dict.values():
        result_list.append(value)

    return result_list
<<<<<<< HEAD
=======
    # print("WORD: ", word)
    # if len(anagram_dict) < 1:
    #     anagram_dict[word] = [word]
    #     print(anagram_dict)
    # else:
    #     # dict_copy = anagram_dict.copy()
    #     for key in anagram_dict.keys():
    #         print("key: ", key)
    #         print("value: ", anagram_dict[key])
    #         if not is_anagram(word, key):
    #             print("False")
    #             anagram_dict[word] = [word]
    #             print(anagram_dict)
    #         else:
    #             print("True")
    #             anagram_dict[key].append(word)
    #             print(anagram_dict)
    #             print("----------------")

    print("FINAL DICT: ", anagram_dict)
>>>>>>> e3050e5f771fa3d08f54414dd959a733f0e9f41f


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    print(k)
    frequency_map = {}

    for element in nums:
        if element in frequency_map:
            frequency_map[element] += 1
        else:
            frequency_map[element] = 1

    print(frequency_map)

    max_value = sorted(frequency_map.keys(),
                       key=frequency_map.get, reverse=True)
    print(max_value)
    return max_value[0:k]


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
