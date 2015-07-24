#!/usr/bin/python

def binarySearch(sorted_array,val):
    mid = len(sorted_array)/2
    if (mid == 0):
        print sorted_array[0]
        return sorted_array[0]
    if (val < sorted_array[mid]):
        sorted_array = sorted_array[:mid]
    else:
        sorted_array = sorted_array[mid:]
    return binarySearch(sorted_array,val)
