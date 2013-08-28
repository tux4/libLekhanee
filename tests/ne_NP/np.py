#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Sample/test transliterator for Nepali (Devanaagari)
# based on libLekhanee
# 
# Copyright (c) 2013 Prasanna Suman <prasanna.tux@gmail.com>
# GNU GPL 3.0
#
###########################################
from ...core import transliterator
from ...keymaps.ne_NP import base_keymap


np_base_keymap = base_keymap.base_keymap
np_dictionary_file = "libLekhanee/dictionaries/ne_NP/ne_NP_plain.dic"

np_transliterator = transliterator.Transliterator("ne_NP", np_base_keymap, np_dictionary_file)

#Simple words
print "Simple words" 
print np_transliterator.transliterate("kalama")
print np_transliterator.transliterate("lekhanee")

#Words with ambiguity
print "Ambiguity for 'pranav'"
pranav = np_transliterator.transliterate("pranava")
for p in  np_transliterator.ambiguity(pranav):
    print p

#With Dictionary
print "Dictionary example"
nepal = np_transliterator.transliterate("nepaata")
for s in np_transliterator.check_and_suggest(nepal):
    print s
