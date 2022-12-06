#!/usr/bin/env python

# url for problem is here

from pprint import pprint
import fileinput
import unittest


def solution():
    pass


if __name__ == "__main__":
    fi = fileinput.FileInput()

    # throw away first line
    fi.readline()

    # now read the text lines
    line = fi.readline().strip()
    case_number = 1
    while line:
        line = fi.readline().strip()
        case_number += 1

              
class MyTest(unittest.TestCase):
    def test_1(self):
        pass
