
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    if len(strings) == 0:
        return []
    if len(strings) == 1:
        return [[strings[0]]]
    list1 = [strings[0]]
    listOfLists = [list1]
    for word in strings[1:]:
        flag = False
        for lists in listOfLists:
            # check in the existing inner lists
            if anagram_helper(word) == anagram_helper(lists[0]):
                lists.append(word)
                flag = True
                break
        # if not in the existing, create a new group
        if not flag:
            listOfLists.append([word])
    return listOfLists

def anagram_helper(word2):
    freq_dict = {}
    for letter in word2:
        if letter not in freq_dict:
            freq_dict[letter] = 1
        else:
            freq_dict[letter] += 1
    return freq_dict


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)for sorted, O(n) to build freq dic, adding the two, the worst case will be O(n log n)
        Space Complexity: O(n)
    """
    if len(nums) == 0:
        return []
    freq_dict = {}
    for elem in nums:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1
    # sorted returns list of tuples (key, value)
    sorted_dict = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    return_list = []
    for index in range(k):
         return_list.append(sorted_dict[index][0])
    return return_list
    
def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    
    #for horizontal
    seen_dict = {}
    for row in table:
        for elem in row:
            if elem == ".":
                continue
            if elem in seen_dict:
                return False
            else:
                seen_dict[elem] = 1
        seen_dict = {}

    # for vertical
    seen_dict = {}
    for col in range(len(table[0])):
        for row in range(len(table)):
            if table[row][col] == ".":
                        continue
            if table[row][col] in seen_dict:
                    return False
            else:
                    seen_dict[table[row][col]] = 1
        seen_dict = {}
    
    # # for 3x3 grid
    seen_dict = {}
    for i in range(3):
        for j in range(3):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1

    seen_dict = {}
    for i in range(3):
        for j in range(3, 6):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1

    seen_dict = {}
    for i in range(3):
        for j in range(6,9):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1

    seen_dict = {}
    for i in range(3,6):
        for j in range(3):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1

    seen_dict = {}
    for i in range(3,6):
        for j in range(3, 6):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1
    
    seen_dict = {}
    for i in range(3,6):
        for j in range(6, 9):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1
    
    seen_dict = {}
    for i in range(6,9):
        for j in range(3):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1
    
    seen_dict = {}
    for i in range(6,9):
        for j in range(3, 6):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1
    
    seen_dict = {}
    for i in range(6,9):
        for j in range(6, 9):
            if table[i][j] == ".":
                continue
            if table[i][j] in seen_dict:
                return False
            else:
                seen_dict[table[i][j]] = 1
    return True