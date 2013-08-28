#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Prasanna Suman
# GNU GPL 3.0
##########################
class base_keymap:
    default_consonants = {
        "ka" : u"क",
        "kha" : u"ख",
        "ga" : u"ग",
        "gha" : u"घ",
        "na" : u"ङ",

        "cha" : u"च",
        "chha" : u"छ",
        "ja" : u"ज",
        "jha" : u"झ",
        "na" : u"ञ",

        "Ta" : u"ट",
        "Tha" : u"ठ",
        "Da" : u"ड",
        "Dha" : u"ढ",
        "Na" : u"ण",

        "ta" : u"त",
        "tha" : u"थ",
        "da" : u"द",
        "dha" : u"ध",
        "na" : u"न",

        "pa" : u"प",
        "pha" : u"फ",
        "ba" : u"ब",
        "bha" : u"भ",
        "ma" : u"म",

        "ya" : u"य",
        "ra" : u"र",
        "la" : u"ल",
        "va" : u"व",
        "sa" : u"स",
        "sha" : u"श",
        "Sa" : u"ष",
        "ha" : u"ह",
    }

    default_vowels = {
        "" : u"्",
        "aa" : u"ा",
        "i" : u"ि",
        "ee" : u"ी",
        "u" : u"ु",
        "oo" : u"ू",
        "e" : u"े",
        "ai" : u"ै",
        "o" : u"ो",
        "au" : u"ौ",

    }

    default_vowels_full = {
        "a" : u"अ",
        "aa" : u"आ",
        "i" : u"इ",
        "ee" : u"ई",
        "u" : u"उ",
        "oo" : u"ऊ",
        "e" : u"ए",
        "ai" : u"ऐ",
        "o" : u"ओ",
        "au" : u"औ",
    }

    ambiguity = [
        [u"त", u"ट"],
        [u"थ", u"ठ"],
        [u"द", u"ड"],
        [u"ध", u"ढ"],
        [u"स", u"ष"],
        [u"न", u"ण", u"ञ",],
        ]

