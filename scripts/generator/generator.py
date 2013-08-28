from __future__ import print_function
import dict_np

DEBUG =False 
file_map = open("full_map_np.py", 'w')

def log(a):
    if DEBUG:
        print (a)


print('#!/usr/bin/env python', file=file_map)
print('# -*- coding: utf-8 -*-', file=file_map)
print('default = {', file=file_map)

for consonant_latin in dict_np.default_consonants.keys():
    print('    "%s" : u"%s",' % (consonant_latin, dict_np.default_consonants[consonant_latin].encode("utf-8")), file=file_map) 
    for vowel_latin in dict_np.default_vowels.keys():
        letter_latin = consonant_latin[:-1] + vowel_latin
        consonant_indic = dict_np.default_consonants[consonant_latin]
        vowel_indic = dict_np.default_vowels[vowel_latin]
        letter_indic = dict_np.default_consonants[consonant_latin] + dict_np.default_vowels[vowel_latin]
        print('    "%s" : u"%s",' %(letter_latin, letter_indic.encode("utf-8")), file=file_map) 
        log ("%s -> %s" %(letter_latin, letter_indic))
        log ("%s + %s = %s" %(consonant_latin, vowel_latin, letter_latin))
        log ("%s + %s = %s" %(consonant_indic, vowel_indic, letter_indic))
    log ("")          

for (vowel_latin, vowel_indic) in dict_np.default_vowels_full.items():
    print('    "%s" : u"%s",' %(vowel_latin, vowel_indic.encode("utf-8")), file=file_map) 
print('}', file=file_map)
file_map.close()
