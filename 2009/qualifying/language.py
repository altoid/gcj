#!/usr/bin/env python

# url for problem is here

from pprint import pprint
import fileinput
import unittest
import re


def pattern_length(pattern):
    # how many characters will a pattern match?
    length = 0
    in_parens = False
    paren_at = None
    i = 0
    for c in pattern:
        if c == '(':
            paren_at = i
            in_parens = True
        elif c == ')':
            in_parens = False
            nchoices = i - paren_at - 1
            if nchoices > 0:
                length += 1
        elif not in_parens:
            length += 1
        i += 1

    return length


def solution(language, pattern):
    pattern = pattern.replace('(', '[').replace(')', ']')
    #pprint(pattern)
    result = 0
    for word in language:
        m = re.match(pattern, word)
        if bool(m):
            result += 1
    return result


if __name__ == "__main__":
    fi = fileinput.FileInput()

    line = fi.readline().strip()
    l, d, n = line.split()
    d = int(d)
    n = int(n)

    language = []
    for i in range(d):
        word = fi.readline().strip()
        language.append(word)

    patterns = []
    for i in range(n):
        pattern = fi.readline().strip()
        patterns.append(pattern)

    #pprint(language)
    #pprint(patterns)

    case_number = 1
    for p in patterns:
        result = solution(language, p)
        print("Case #%s: %s" % (case_number, result))
        case_number += 1

              
class MyTest(unittest.TestCase):
    def test_1(self):
        language = ['abc', 'bca', 'dac', 'dbc', 'cba']
        pattern = '(ab)(bc)(ca)'
        expecting = 2
        self.assertEqual(expecting, solution(language, pattern))

    def test_pattern_length(self):
        self.assertEqual(0, pattern_length(""))
        self.assertEqual(1, pattern_length("a"))
        self.assertEqual(3, pattern_length("a(d)t"))
        self.assertEqual(1, pattern_length("(d)"))
        self.assertEqual(0, pattern_length("()"))
        self.assertEqual(3, pattern_length("ae()t"))

