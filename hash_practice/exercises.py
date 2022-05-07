
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: n^2logn
        Space Complexity: n
    """
    freq_map = {}
    for word in strings:  # n
        key = list(word) # n
        key.sort()  # logn
        key = "".join(key)  # n
        if key in freq_map:  # n
            freq_map[key].append(word)
        else:
            freq_map[key] = [word]
    return [val for val in freq_map.values()]


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: nlogn
        Space Complexity: n
    """
    freq_dict = {}
    for num in nums: # n
        freq_dict[num]= freq_dict.get(num, 0)+1
    
    freq_target = [freq for freq in freq_dict.values()] # n
    freq_target.sort() # logn
    freq_target = freq_target[-k:] # n
    result = []
    for num in nums: # n
        if (freq_dict[num] in freq_target):
            result.append(num)
            freq_dict[num] = None
    return result



def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: n^3 --> but honestly its prob even more inefficient than that...
        Space Complexity: n
    """
    # check rows
    for subarr in table: # n
        freq_table = create_hash()
        for string in subarr: # n
            string = string.replace(".","")
            if len(string)>0:
                if freq_table[string]:
                    return False
                freq_table[string]=True
    
    # check columns 
    for i in range(len(table)):
        freq_table = create_hash()
        for arr in table:
            key = arr[i].replace(".","")
            if len(key)>0:
                if freq_table[key]:
                    return False
                freq_table[key]=True
    
    # check squares
    checks = [i for i in range(0,7,3)]
    for x in checks:
        for y in checks:
            if not check_sub_square(x,y,table):
                return False
    return True

def create_hash():
    base_hash = {}
    for i in range(1,10):
        base_hash[str(i)]=False
    return base_hash

def check_sub_square(x, y, table):
    freq_table = create_hash()
    for i in range(y, y+3):
        for j in range(x, x+3):
            key = table[i][j].replace(".","")
            if len(key)>0:
                if freq_table[key]:
                    return False
                freq_table[key]=True
    return True

