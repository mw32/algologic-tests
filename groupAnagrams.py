#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:11:52 2020

@author: martin.widjaja
"""
strs = ["eat", "tea", "tan", "ate", "nat", "bat", "boo", "bop", "bob"]

def groupAnagramsSLOW(self, strs):
    
    from collections import Counter    
    result = dict()
    
    for i in strs:
        
        # Convert words to sorted set of letters
        a = sorted(i)
        #print(a)
        # Take a counter of the letters and convert to dict
        b = dict(Counter(a))
        #print(b)
        
        # Build the key for the result dict
        key = ""
        for k,v in b.items():
            key = "%s%s%s"%(key,k,v)
        #print(key)
        
        if key in result:
            result[key].append(i)
        else:
            result[key] = [i]
        #print(result.values())
        
            
    return list(result.values())


 

result = dict()

for i in strs:
    
    # Convert words to sorted list of letters
    a = sorted(i)
    print(a)
    # Create a new string in alphabetical order
    key = ''.join(a)
    print(key)
    
    if key in result:
        result[key].append(i)
    else:
        result[key] = [i]
    print(result.values())
        
print(list(result.values()))

       