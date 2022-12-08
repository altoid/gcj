#!/usr/bin/env python

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000433515/0000000000433a60#problem
import random
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
        i_prefix_exists = False
        while i < len(s):
            result = multiply(result, s[i])
            i += 1
            if result == 'i':
                i_prefix_exists = True
                break

        if not i_prefix_exists:
            return False

        j_prefix_exists = None
        result = '1'
        while i < len(s):
            result = multiply(result, s[i])
            i += 1
            if result == 'j':
                j_prefix_exists = True
                break

        return j_prefix_exists

    if reduction[-1] == '1':
        return False

    remainder = x % 4
    result = '1'
    for i in range(remainder):
        result = multiply(result, reduction)

    if result != '-1':
        return False

    # are we here?  then the whole string reduces to -1.  so there
    # may be a solution.

    result = '1'
    i = 0
    i_prefix_exists = False

    # look for 'i' prefix. multiply the chars of s together until we get 'i'.  traverse s up to 4 times.
    # any string ** 4 is always 1.  if we haven't found an 'i' prefix by the time we've traversed s 4 times
    # we never will.

    stop_already = 4 * len(s)

    while i < stop_already:
        idx = i % len(s)
        result = multiply(result, s[idx])
        i += 1
        if result == 'i':
            i_prefix_exists = True
            break

    if not i_prefix_exists:
        return False

    j_prefix_exists = None
    d = i % len(s)
    i = d
    result = '1'
    while i < stop_already + d:
        idx = i % len(s)
        result = multiply(result, s[idx])
        i += 1
        if result == 'j':
            j_prefix_exists = True
            break

    return j_prefix_exists


def showtime():
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
        # print("s = %s, x = %s" % (s, x))
        result = solution(s, x)
        print("Case #%s: %s" % (case_number, "YES" if result else "NO"))
        case_number += 1
        line = fi.readline().strip()


def stresstest():
    # generate inputs and run the test until something breaks.

    while True:
        length = random.randint(1, 500)
        s = ''.join(random.choices("ijk", k=length))
        x = random.randint(1, 10000)
        try:

            #print(s, len(s))
            #print(x)
            solution(s, x)
        except Exception as e:
            print("length = %s, x = %s" % (length, s))
            print(e)


if __name__ == '__main__':
    showtime()
    

class MyTest(unittest.TestCase):
    def test_5(self):
        s = 'iii'
        x = 6
        self.assertFalse(solution(s, x))

    def test_4(self):
        s = 'ii'
        x = 6
        self.assertFalse(solution(s, x))

    def test_3(self):
        s = 'i'
        x = 6
        self.assertFalse(solution(s, x))

    def test_2_5(self):
        s = 'ij'
        x = 2
        self.assertTrue(solution(s, x))

    def test_2(self):
        s = 'ji'
        x = 6
        self.assertTrue(solution(s, x))

    def test_1(self):
        s = 'ijk'
        x = 1
        self.assertTrue(solution(s, x))
