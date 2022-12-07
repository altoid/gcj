#!/usr/bin/env python

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000433515/0000000000433a60#problem

from pprint import pprint
import fileinput
import unittest

# notes
#
# whole string has to reduce to i * j * k == -1
# x ** n == x if n % 4 == 1, i.e. four consecutive multiplications of x gives you back x.
# if L reduces to +/- 1, stop, no solution
# otherwise we still need to do the slog of finding prefixes that reduce to i, but if L doesn't reduce to +- 1 then
# we can just multiply L-groups together rather than individual chars.


space = {
    ('1', '1'): '1',
    ('1', 'i'): 'i',
    ('1', 'j'): 'j',
    ('1', 'k'): 'k',

    ('i', '1'): 'i',
    ('i', 'i'): '-1',
    ('i', 'j'): 'k',
    ('i', 'k'): '-j',

    ('j', '1'): 'j',
    ('j', 'i'): '-k',
    ('j', 'j'): '-1',
    ('j', 'k'): 'i',

    ('k', '1'): 'k',
    ('k', 'i'): 'j',
    ('k', 'j'): '-i',
    ('k', 'k'): '-1',

    #

    ('-1', '-1'): '1',
    ('-1', '-i'): 'i',
    ('-1', '-j'): 'j',
    ('-1', '-k'): 'k',

    ('-i', '-1'): 'i',
    ('-i', '-i'): '-1',
    ('-i', '-j'): 'k',
    ('-i', '-k'): '-j',

    ('-j', '-1'): 'j',
    ('-j', '-i'): '-k',
    ('-j', '-j'): '-1',
    ('-j', '-k'): 'i',

    ('-k', '-1'): 'k',
    ('-k', '-i'): 'j',
    ('-k', '-j'): '-i',
    ('-k', '-k'): '-1',

    #

    ('-1', '1'): '-1',
    ('-1', 'i'): '-i',
    ('-1', 'j'): '-j',
    ('-1', 'k'): '-k',
    ('-i', '1'): '-i',
    ('-i', 'i'): '1',
    ('-i', 'j'): '-k',
    ('-i', 'k'): 'j',
    ('-j', '1'): '-j',
    ('-j', 'i'): 'k',
    ('-j', 'j'): '1',
    ('-j', 'k'): '-i',
    ('-k', '1'): '-k',
    ('-k', 'i'): '-j',
    ('-k', 'j'): 'i',
    ('-k', 'k'): '1',

    #

    ('1', '-1'): '-1',
    ('1', '-i'): '-i',
    ('1', '-j'): '-j',
    ('1', '-k'): '-k',
    ('i', '-1'): '-i',
    ('i', '-i'): '1',
    ('i', '-j'): '-k',
    ('i', '-k'): 'j',
    ('j', '-1'): '-j',
    ('j', '-i'): 'k',
    ('j', '-j'): '1',
    ('j', '-k'): '-i',
    ('k', '-1'): '-k',
    ('k', '-i'): '-j',
    ('k', '-j'): 'i',
    ('k', '-k'): '1',
}


def multiply(a, b):
    return space[(a, b)]


def reduce(s):
    result = '1'
    for c in s:
        result = multiply(result, c)

    return result


def solution(s, x):
    # s is a string, repeat it x times.
    reduction = reduce(s)

    if x == 1:
        if reduction != '-1':
            return False

        result = '1'
        i = 0
        i_bound = None
        while i < len(s):
            result = multiply(result, s[i])
            if result == 'i':
                i_bound = i

            i += 1
            if i_bound is not None:
                break

        j_bound = None
        result = '1'
        while i < len(s):
            result = multiply(result, s[i])
            if result == 'j':
                j_bound = i

            i += 1
            if j_bound is not None:
                break

        return i_bound is not None and j_bound is not None

    if reduction[-1] == '1':
        return False

    remainder = x % 4
    result = reduction
    for i in range(remainder):
        result = multiply(result, s[i])

    if result != '-1':
        return False

    # are we here?  then the whole string reduces to -1.  so there
    # may be a solution.

    result = '1'
    i = 0
    i_bound = None
    while i < len(s):
        result = multiply(result, s[i])
        if result == 'i':
            i_bound = i

        i = (i + 1) % len(s)
        if i_bound is not None:
            break

    j_bound = None
    while i < len(s):
        result = multiply(result, s[i])
        if result == 'j':
            j_bound = i

        i = (i + 1) % len(s)
        if j_bound is not None:
            break

    return i_bound is not None and j_bound is not None


if __name__ == "__main__":
    fi = fileinput.FileInput()

    # throw away first line
    fi.readline()

    # now read the text lines
    line = fi.readline().strip()
    case_number = 1
    while line:
        l, x = line.split(' ')
        x = int(x)
        line = fi.readline().strip()
        s = line
        #print("s = %s, x = %s" % (s, x))
        result = solution(s, x)
        print("Case #%s: %s" % (case_number, "YES" if result else "NO"))
        case_number += 1
        line = fi.readline().strip()


class MyTest(unittest.TestCase):
    def test_2(self):
        s = 'ji'
        x = 6
        self.assertTrue(solution(s, x))

    def test_1(self):
        s = 'ijk'
        x = 1
        self.assertTrue(solution(s, x))

