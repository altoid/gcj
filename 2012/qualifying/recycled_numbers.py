#!/usr/bin/env python

import fileinput
from pprint import pprint
import unittest


# 11 isn't recyclable.  we require m != n.  leading 0 prohibited.
#
# a and b have the same number of digits.

def len_digits(n):
    """
    return the number of digits in n, where n >= 0.
    :param n:
    :return:
    """
    if not n:
        return 1

    exp = 0
    while (10 ** exp) <= n:
        exp += 1
    return exp


def rotation(n, ndigits):
    x = n
    p = 10 ** (ndigits - 1)
    for i in range(ndigits):
        d = x % 10
        rest = x // 10

        x = rest + d * p
        yield x


def solution(a, b):
    l = len_digits(a)

    total = 0
    for i in range(a, b + 1):

        s = set(rotation(i, l))
        f = filter(lambda x: a <= x <= b and i < x, s)

        c = 0
        for n in f:
            #print(n, end=' ')
            total += 1
            c += 1
        # if c:
        #     print("%s (%s, %s)" % (i, c, total))

    return total


if __name__ == '__main__':
    n = 123456
    ndigits = len_digits(n)
    r = set(rotation(123456, ndigits))
    pprint(r)

    print(solution(1000000, 2000000))


class MyTest(unittest.TestCase):
    def test_ndigits(self):
        self.assertEqual(1, len_digits(0))
        self.assertEqual(1, len_digits(1))
        self.assertEqual(1, len_digits(9))
        self.assertEqual(2, len_digits(10))
        self.assertEqual(2, len_digits(11))
        self.assertEqual(3, len_digits(100))
        self.assertEqual(3, len_digits(101))
        self.assertEqual(3, len_digits(999))

    def test_4(self):
        # 1920/2019

        # 1112/1121/1211/2111
        # 1113/1131/1311
        # 2221/2212/2122/1222
        # 1112 numbers in this range
        # 9 start with 111
        # 80 start with 11 but not 111
        # 800 start with 1 but not 11 or 111
        a = 1111
        b = 2222
        expecting = 287
        self.assertEqual(expecting, solution(a, b))

    def test_3(self):
        a = 100
        b = 500
        expecting = 156
        self.assertEqual(expecting, solution(a, b))

    def test_2(self):
        a = 10
        b = 40
        expecting = 3
        # 12/21, 13/31, 23/32
        self.assertEqual(expecting, solution(a, b))

    def test_1(self):
        a = 1
        b = 9
        expecting = 0
        self.assertEqual(expecting, solution(a, b))
