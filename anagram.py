#!/usr/bin/python

#from collections import Counter
#from collections import OrderedDict
import re
import sys

dict_file = '/usr/share/dict/words'
dict_file = '/usr/share/dict/linux.words'
main_hash = {}

def build_hash():
    with open(dict_file, 'r') as d:
        lines = d.readlines()
        for l in lines:
            l = l.lower().strip()
            # if contains non alpha: - or ', just skip it
            if re.search('\W+', l):
                continue
    
            #print "%s:"% l
   
            # Build the main hash table for anagram
            hash_key = create_key(l)
            if hash_key in main_hash:
                main_hash[hash_key].append(l)
            else:
                main_hash[hash_key] = [l]
            #print "%s: %s\n" % (hash_key,main_hash[hash_key])


def create_key(word):
    lst = sorted(list(word))

    # build the key for the hashtable
    word_dict = {}
    word_dict = {x:lst.count(x) for x in lst}
    # only for 2.7++
    #word_dict = dict(Counter(lst))

    k = ''
    for i in sorted(word_dict.keys()):
        k = k + "%s%s" % (i, word_dict[i])
    return k


# Search anagram
if __name__ == '__main__':
  print "Building dictionary..."
  build_hash()
  while True:
      input = raw_input('Enter word> ')
      search_key = create_key(input)
      if search_key not in main_hash:
          print "No anagram found for word '%s'" % input
          continue
      print "Anagrams: %s" % " ".join(main_hash[search_key])
