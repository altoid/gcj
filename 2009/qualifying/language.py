#!/usr/bin/env python

# url for problem is here

from pprint import pprint
import fileinput
import unittest

def split_pattern(pattern):
    # return the pattern as a list of disjunctions or letters.
    # ex:  a(bcd)ef(gh)i()j ==> a bcd e f gh i j

    pieces = []
    in_parens = False

    i = 0
    paren_at = None
    for c in pattern:
        if c == '(':
            in_parens = True
            paren_at = i
        elif c == ')':
            in_parens = False
            piece = pattern[paren_at + 1:i]
            if len(piece) > 0:
                pieces.append(piece)
        elif not in_parens:
            pieces.append(c)
        i += 1

    return pieces


def solution(language, pattern):
    wordlength = len(language[0])
    pieces = split_pattern(pattern)
    if wordlength != len(pieces):
        return 0

    filtered_language = language
    for i in range(wordlength):
        filtered_language = list(filter(lambda x: x[i] in pieces[i], filtered_language))
        if len(filtered_language) == 0:
            break

    return len(filtered_language)


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

    # pprint(language)
    # pprint(patterns)

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

    def test_2(self):
        language = ['abc', 'bca', 'dac', 'dbc', 'cba']
        pattern = '(zyx)bc'
        expecting = 0
        self.assertEqual(expecting, solution(language, pattern))

    def test_split_pattern(self):
        pattern = "a(bcd)ef(gh)i()j"
        pprint(split_pattern(pattern))
