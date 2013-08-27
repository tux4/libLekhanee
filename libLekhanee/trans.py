#!/usr/bin/env python
# -*- coding: utf-8 -*-

import full_map_np 
from dict_np import ambguity

class transliterator:
    def __init__(self, keymap):
        self.__keymap = keymap 

    def transliterate(self, text):
        return self.__trans(text)

    def anm(self, text):
    """Resolves the consonant ambiguity like T, t, n, N, d, D etc"""
        results = []
        for i in range(0, len(text)):
            pivot = text[i]
            pre_pivot = text[:i]
            post_pivot = text[i+1:]
            for amb in ambguity:
                if pivot in amb:
                    print "Text:%s, i:%s, len:%s, Pre:%s, Post:%s" %(text, i, len(text), pre_pivot, post_pivot)
                
                    results += map(lambda p: pre_pivot + p + post_pivot, amb)

        return results                

    def __trans(self, part1, part2 = "", result = ""):
        if not part1 and not part2:
            return unicode(result)
        else:
            if self.__keymap.has_key(part1):
                result += self.__keymap[part1]
                part1 = part2
                return self.__trans(part1, "", result)
            else:
                if len(part1) == 1:
                    result += part1
                    part1 = part2
                    return self.__trans(part1, "", result)
                else:
                    return self.__trans(part1[:-1], part1[-1:] + part2, result) 

if __name__ == "__main__":

    np_en_keymap = full_map_np.default
    np_en = transliterator(np_en_keymap)
    #print np_en.transliterate("kaaThmaaNDu?") 
    a= np_en.transliterate("takamateeta")
    for result in np_en.anm(a):
        print result 
    print np_en.transliterate("sha")
