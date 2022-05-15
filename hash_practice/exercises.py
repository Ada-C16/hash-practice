from collections import defaultdict

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
    """
    anagrams = []
    word_dict = anagrams_helper(strings)
    for word in word_dict.values():
        anagrams.append(word)
    return anagrams


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements"""
    
    num_frequency = {}
    for num in nums:
        if not num in num_frequency.keys():
            num_frequency[num] = 1
        num_frequency[num] += 1	
    k_most_frequent_keys = sorted(num_frequency, key=num_frequency.get, reverse=True)[:k]
    return k_most_frequent_keys


# anagram_helper
def anagrams_helper(source_list):
    word_dict = defaultdict(list)
    for word in source_list:
        key = "".join(sorted(word))
        word_dict[key].append(word)
    return word_dict