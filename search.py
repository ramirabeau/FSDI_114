#!/usr/bun/env python3

# Unordered list search
def ul_seq_search(array, element):
    position = 0
    found = False
    while position < len(array) and not found:
        if array[position] == element:
            found = True
        else:
            position += 1

    return found

# Ordered list search
def ol_seq_search(array, element):
    position = 0
    found = False
    stopped = False
    while position < len(array) and not found and not stopped:
        if array[position] == element:
            found = True
        else:
            if array[position] > element:
                stopped = True
            position += 1

    return found

# Binary Search
def binary_search(arr, ele):
    # First and last index values
    first = 0
    last = len(arr)-1
    found = False
    while first <= last and not found:
        mid = int((first+last)/2)
        # Match found
        if arr[mid] == ele:
            found = True
        # set new midpoints up or down depending on the comparison
        else:
            # Set down
            if ele< arr[mid]:
                last = mid-1
            # Set up                
            else: first = mid + 1
    return found

    #Recursive version of Binary Search
    def rec_bin_search(arr, ele):
        # Base Case
        if len(arr) == 0:
            return False
        # Recursive Case
        else:
            mid = int(len(arr)/2)
            # If match is found
            if arr[mid] == ele:
                return True
            else:
                # Call again on the second half
                if ele < arr[mid]:
                    return rec_bin_search(arr[:mid], ele)
                # Or call on the first half
                else:
                    return rec_bin_search(arr[mid+1:], ele)
           