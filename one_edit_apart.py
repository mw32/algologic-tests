#!/usr/bin/python

import sys

# Given 2 strings, check if there's only 1 edit: 1 insert, deletion, char diff
def one_edit_apart(str1, str2):
    # s1 is set to the shorter string
    s1,s2 = (str2,str1) if (len(str1) > len(str2)) else (str1,str2)
    print s1, s2

    delta = len(s2) - len(s1)

    # If there's more than 2 chars, false
    if delta > 1:
        return False
    diff_length = True if delta == 1 else False

    diff = False
    i = j = 0
    while i < len(s1):
        print "Comparing %d:%s and %d:%s:" % (i,s1[i],j,s2[j]),
        if s1[i] != s2[j]:
            print "False"
            if diff:
                print "Already had a diff, found another diff at index %d" % i
                return False
            diff = True
            if diff_length:
                print "Skipping a letter in longer string %s" % s2
                i -= 1
        else:
            print "True"
        i += 1
        j += 1
    return True

if __name__ == '__main__':
    print "The 2 strings are one edit apart: %s" % one_edit_apart(sys.argv[1], sys.argv[2])

