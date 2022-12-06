#!/usr/bin/env python

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000433515/0000000000433738

from pprint import pprint
import fileinput
import unittest


def solution(audience_str):
    audience = list(map(int, audience_str))
    predecessors = 0
    predecessor_list = [0]
    for i in range(1, len(audience)):
        predecessors += audience[i - 1]
        predecessor_list.append(predecessors)

    #pprint(predecessor_list)
    need = 0
    for i in range(1, len(audience)):
        n = i - predecessor_list[i] - need
        if n > 0:
            need += n

    return need


if __name__ == "__main__":
    fi = fileinput.FileInput()

    # throw away first line
    fi.readline()

    # now read the text lines
    line = fi.readline().strip()
    case_number = 1
    while line:
        count, audience_str = line.split(' ')
        print("Case #%s: %s" % (case_number, solution(audience_str)))
        line = fi.readline().strip()
        case_number += 1


class MyTest(unittest.TestCase):
    def test_2(self):
        audience_str = '01020304'
        expecting = 2
        result = solution(audience_str)
        print(result)
        self.assertEqual(expecting, result)

    def test_1(self):
        audience_str = '650032'
        expecting = 0
        result = solution(audience_str)
        print(result)
        self.assertEqual(expecting, result)
