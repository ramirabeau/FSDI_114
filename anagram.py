#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Anagram Checker"""

class anagram:
    def anagram_check():
        s1 = input("Enter first string:")
        s2 = input("Enter second string:")
        if (sorted(s1) == sorted(s2)):
            return True
        else:
            return False

if __name__ == "__main__":
