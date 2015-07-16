#!/usr/bin/python
# permutate chars from strings given a list of strings

def solve(words):
	if not words: 
		return ['']
	return (char + r for char in words[0] for r in solve(words[1:]))

print list(solve(['red', 'fox', 'super']))
