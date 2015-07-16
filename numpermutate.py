#!/usr/bin/python

INPUT='1226'
hash = {str(x+1):a for x,a in enumerate(map(chr,range(97,123)))}
#print hash

a = []

def numpermutate(input):
    count = 0
    print "Entering: %s" % input
    if input == '':
        return 1
    for i in range(len(input)):
        print "loop: %s" % input[i]
        if i+1 > 2 or input[:i+1] not in hash:
            break
        else:
            a.append(input[:i+1])
            print "calling...: %s" % (input[i+1:])
            count += numpermutate(input[i+1:])
            print "After: count: %s" % count
        print "Array: %s => %s" % (a, count)
    return count

def main(input):
    print numpermutate(input)
    print a

if __name__ == '__main__':
    main(INPUT)
