
def create_freq_map(word):
    freq_map = {}
    for char in word:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    # convert to frozenset because it's hashable whereas dicts and sets are not
    return freq_map

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?

    Ideas
    Have freq maps as keys and words as values in a list
    dict = {
        {"a":1, "t":1, "e":1}: ["ate", "eat", "tea"]
    }
    -> would need 3 hash tables: 1 for hash of hash tables of frequences, 2 dict has keys?
    -> or create this dict example without creating another hash

    PSEUDO
    - Create empty dict
    - Loop through each word in words and create freq map (maybe use a helper)
    - if freq map not in dict, append to dict with freq map as key and word as value
    - if freq map in dict, append word to value
    - return dict values as list
    """
    word_dict = {}
    for word in strings:
        current_freq_map = frozenset(create_freq_map(word))
        if current_freq_map in word_dict:
            word_dict[current_freq_map] += [word]
        else:
            word_dict[current_freq_map] = [word]

    return list(word_dict.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?

    Ideas
    Create freq map where keys are nums and value is the frequency
    How to return the number with 1st, 2nd highest freq if k =2
    what if k=3

    PSEUDO
    -Create freq map 
    freq_map = {
        1:1,
        2:3,
        3:2
    }
    - have a max_count for max value ->
        - could also maybe use slicing 
    -create empty list
    - for i in range(k), append key that has max count
    - decrement max_count

    with duplicate max values:
    - create max_list instead of a variable

    """
    # max_count = 0
    # freq_map = {}
    # for num in nums:
    #     if num in freq_map:
    #         freq_map[num] += 1
    #     else:
    #         freq_map[num] = 1

    #     if max_count < freq_map[num]:
    #         max_count = freq_map[num]

    # answer = []
    # for key, value in freq_map.items():
    #     if k > 0:
    #         if value == max_count:
    #             answer.append(key)
    #             k -= 1
    #             max_count -= 1

    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    freq_values = list(freq_map.values())
    # sorts values of freq map in descending order
    freq_values.sort(reverse=True)
    # k number of max frequencies 
    max_values = freq_values[:k]

    answer = set()
    for key, value in freq_map.items():
        for max in max_values:
            if value == max:
                answer.add(key)
    
    
    return list(answer)

    


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

