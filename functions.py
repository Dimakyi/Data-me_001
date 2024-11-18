#TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    # Implement this

    return lst[::-1]

print(reverse_list([1,2,3,4,5,6,7,8,9,10]))   

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    # Implement this
    element = []
    for i in list:
        element += 1

    return element

print(count_occurrences())
def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    # Implement this
    return dict.intersect(value)

print(count_occurrences())
def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    return sorted(lst1, lst2)
    # Implement this
print(merge_sorted_lists([5,2,3,1,7,9,6,4][1,4,7,9,5,4,7,]))

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    # Implement this
    for i in numbers:
        if (numbers > 8) and (numbers <10):
            return numbers

print([1,2,3,4,5,6,7,8,9,10])
def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    # Implement this

    string = str1 == str2[::-1]
    string == string
    return string
    
print(is_anagram("madam", "madam"))

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    # Implement this
    for i in nested_list:
        
        return 

print(flatten_list[1,2,3,4,5,6,[47,8,9,10]])

def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    # Implement this

    return set(lst)
print(remove_duplicates(["banana","orange","grapes","banana"]))

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    # Implement this
    for i in lst1:
        for j in lst2:
            if i and j in lit2:
                return j
print(find_common_elements([1,2,3,4,5,6,7,8,9,10],[1,1,2,3,4,4,5,6,7,7,]))