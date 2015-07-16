#!/usr/bin/python

data = [
         [ "John", "john@gmail.com", "john@fb.com"],
         [ "Dan", "dan@gmail.com", "+1234567"],
         [ "john123", "+5412312", "john123@skype.com"],
         [ "john1985", "+5412312", "john@fb.com"]
       ]

# Build a hashmap
#datamap = {i:k for i,k in enumerate(data)}
#print datamap
#for i in datamap:
# if set(datamap[i]).intersection(set(datamap[i+1]))]
#    print datamap[i]


# Build reverse hash of lists using content as key and array of index as value
# hashmap with int won't work cause dup key get overwritten immediately.
datamap = {}
for i,j in enumerate(data):
    for k in j:
        if k in datamap:
            datamap[k] = datamap[k] + [i]
        else:
            datamap[k] = [i]

print datamap
print

# Now merge/union the intersecting sets
sets = [set(i) for i in datamap.values() if i]
merged = True
while sets and merged:
    print "sets: %s"%sets
    first, rest = sets[0], sets[1:]
    sets = []
    merged = False
    for x in rest:
        if first.intersection(x):
            first = first.union(x)
            merged = True
        else:
            sets.append(x)
    sets.append(first)

res = [list(a) for a in sets]
print res
