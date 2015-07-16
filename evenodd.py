#!/usr/bin/python
# Count numbers with even number of odd digits in them

lim=int(raw_input("Enter a number limit: "))
count=0

for i in range(1,lim+1):
    l = map(int, str(i))
    odd_digits = 0
    msg = ''
    for x in 1,3,5,7,9:
        odd_digits += l.count(x)
    if odd_digits > 0 and (odd_digits % 2) == 0:
        count += 1
        msg = '\t===> FOUND!\t%s' % count
    print "%s: %s%s" % (i,odd_digits,msg)

print "Number with even odd digits from 1 to %s: %s" % (lim,count)
