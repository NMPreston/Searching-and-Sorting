# Noah Preston, CSC 231, 001

def linear_search(search_lst, target): # Linear search for an unsorted list
    for i, item in enumerate(search_lst): # Loop through elements 
        if item == target: # Check if item is equal to intended target
            return True, i # Return True and the index if it is found
    return False, None # Otherwise return False or None

def smart_sequential_search(search_lst, target): # Smart sequential search for sorted list
    for i, item in enumerate(search_lst): # Loop through elements
        if item == target: # Check if item is equal to intended target 
            return True, i # Return True and the index if it is found
        elif item > target: # Check if item is greater than target 
            break 
    return False, None # Return False and None 

def binary_search(search_lst, target): # Binary search for sorted list 
    left, right = 0, len(search_lst) - 1 # Left and right pointers for list 
    while left <= right:
        middle = (left + right) // 2 # Calculate middle index 
        if search_lst[middle] == target:
            return True, middle # Return True and the index if it is found
        elif search_lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False, None # Return False and None 

# Test functions 
def main():
    print("Linear Search:", linear_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31))  # True
    print("Smart Sequential Search:", smart_sequential_search([1, 4, 5, 23, 31, 56, 57, 71, 105], 31))  # True, 4
    print("Binary Search (6 not in list):", binary_search([1, 2, 3, 5, 8], 6))  # False
    print("Binary Search (5 in list):", binary_search([1, 2, 3, 5, 8], 5))  # True

if __name__ == "__main__":
    main()

