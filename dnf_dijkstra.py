#!/usr/bin/python

# Dutch national flag sorting algo

random = ['r','b','w','w','b','b','r','w','w','r']

def dnf_sort(arr, order='rwb'):
    lo = mid = 0
    hi = len(arr) - 1

    while mid <= hi:
        if arr[mid] == order[0]:
            swap(arr,lo,mid)
            lo+=1
            mid+=1
        elif arr[mid] == order[1]:
            mid+=1
        elif arr[mid] == order[2]:
            swap(arr,mid,hi)
            hi-=1
    return arr

def swap(lst,a,b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp


if __name__ == '__main__':
    print dnf_sort(random)
