#!/usr/bin/python

def isPalindrome(s):
    l = list(s.lower())
    a = 0
    z = len(l) - 1

    while a <= z:
        if not l[a].isalnum():
            a+=1
        elif not l[z].isalnum():
            z-=1
        elif l[a] == l[z]:
            a+=1
            z-=1
        elif l[a] != l[z]:
            #print "a:%s, z:%s - %s" % (a,z,l[a]+l[z])
            return False
    return True


if __name__ == '__main__':
    while True:
        i = raw_input('Enter string > ')
        i = i.strip()
        if isPalindrome(i):
            print "'%s' is a palindrome!!" % i
        else:
            print "'%s' is NOT a palindrome!!" % i
        print
