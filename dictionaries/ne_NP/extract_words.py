from __future__ import print_function

file_ne = open("ne_NP.dic", 'r')
file_new = open("np_base.dic", 'w')

for word in file_ne:
    new_word = word.split('/')[0].rstrip()
    print (new_word)
    if new_word:
        print (new_word, file=file_new)

