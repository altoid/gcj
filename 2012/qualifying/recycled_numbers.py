#!/usr/bin/env python

import fileinput
from pprint import pprint
import unittest

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b33/0000000000432be6

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


def y_rotation(n, ndigits):
    x = n
    p = 10 ** (ndigits - 1)
    for i in range(ndigits):
        d = x % 10
        rest = x // 10

        x = rest + d * p
        yield x


def rotation(n, ndigits, power_of_10):
    x = n
    result = set()
    for i in range(ndigits):
        d = x % 10
        rest = x // 10

        x = rest + d * power_of_10
        result.add(x)
    return result


def solution(a, b):
    l = len_digits(a)
    if l < 2:
        return 0

    power_of_10 = 10 ** (l - 1)
    total = 0
    values = [x for x in range(a, b + 1)]
    for i in range(a, b + 1):

        if values[i - a] == 0:
            continue

        s = rotation(i, l, power_of_10)
        f = filter(lambda x: a <= x <= b and i < x, s)

        c = 0
        for n in f:
            # print(n, end=' ')
            values[n - a] = 0
            c += 1

        total += (c * (c + 1)) // 2

    return total


if __name__ == '__main__':
    fi = fileinput.FileInput()

    # throw away first line
    fi.readline()

    # now read the text lines
    line = fi.readline().strip()
    case_number = 1
    while line:
        a, b = map(int, line.split())
        print("Case #%s: %s" % (case_number, solution(a, b)))
        case_number += 1
        line = fi.readline().strip()

    # n = 123456
    # ndigits = len_digits(n)
    # r = set(rotation(123456, ndigits))
    # pprint(r)
    #
    # print(solution(1000000, 2000000))


class MyTest(unittest.TestCase):
    def test_time(self):
        print(solution(1000000, 2000000))

    def test_ndigits(self):
        self.assertEqual(1, len_digits(0))
        self.assertEqual(1, len_digits(1))
        self.assertEqual(1, len_digits(9))
        self.assertEqual(2, len_digits(10))
        self.assertEqual(2, len_digits(11))
        self.assertEqual(3, len_digits(100))
        self.assertEqual(3, len_digits(101))
        self.assertEqual(3, len_digits(999))

    def test_5(self):
        a = 1111
        b = 1111
        expecting = 0
        self.assertEqual(expecting, solution(a, b))

    def test_4(self):
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
