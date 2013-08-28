#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set et sts=4 sw=4:
#
# libLekhanee - Transliteration Library for Indic Scripts 
# Copyright (c) 2013 Prasanna Suman <prasanna.tux@gmail.com>
# 
#  
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


import enchant

class Transliterator:
    def __init__(self, lang, base_keymap, full_dictionary_file=None):
        self.__lang = lang
        self.__base_keymap = base_keymap 
        self.__keymap= self.__generate_full_keymap(base_keymap)
        self.__full_dictionary_file = full_dictionary_file
        if full_dictionary_file:
            self.__dict = enchant.request_pwl_dict(full_dictionary_file)  

    def __generate_full_keymap(self, base_keymap):
        """Returns full keymap based on supplied base_keymap
        """
        assert base_keymap.default_consonants
        assert base_keymap.default_vowels
        assert base_keymap.default_vowels_full
        full_keymap = {}
        for consonant_latin in base_keymap.default_consonants.keys():
            for vowel_latin in base_keymap.default_vowels.keys():
                letter_latin = consonant_latin[:-1] + vowel_latin
                consonant_indic = base_keymap.default_consonants[consonant_latin]
                vowel_indic = base_keymap.default_vowels[vowel_latin]
                letter_indic = base_keymap.default_consonants[consonant_latin] + base_keymap.default_vowels[vowel_latin]
                full_keymap[letter_latin] = letter_indic
        return dict(base_keymap.default_consonants.items() + full_keymap.items() + base_keymap.default_vowels_full.items()) 

    def check_and_suggest(self, text):
        """Matches a text in dictionary, if not found returns 
            suggestions as a list
        """
        try:
            if not self.__dict.check(text):
                return self.__dict.suggest(text)
            return text
        except:
            pass

    def transliterate(self, text):
        """Returns the indic text equivalent of latin input based 
            on the given keymap
        """
        return self.__trans(text)

    def ambiguity(self, text):
        """Resolves the consonant ambiguity like T, t, n, N, d, D etc, by 
            returning all possible transliterations as a list
        """
        assert self.__base_keymap.ambiguity 
        results = []
        for i in range(0, len(text)):
            pivot = text[i]
            pre_pivot = text[:i]
            post_pivot = text[i+1:]
            for amb in self.__base_keymap.ambiguity:
                if pivot in amb:
                    #print "Text:%s, i:%s, len:%s, Pre:%s, Post:%s" %(text, i, len(text), pre_pivot, post_pivot)
                    results += map(lambda p: pre_pivot + p + post_pivot, amb)

        return results                

    def __trans(self, part1, part2 = "", result = ""):
        """This is the core transliteration function. Recurcively matches the input string with a 
            dictionary until the final result is attained. Leaves as-is if no match is found.
        """
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



