#!/usr/bin/env python

from pprint import pprint
import fileinput

MAPPING = {
    # maps gibberish letters back to english
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q',
    ' ': ' '
    }

def translate(gibberish):
    result = ''.join([MAPPING[c] for c in gibberish])
    return result

if __name__ == "__main__":
    fi = fileinput.FileInput()

    # throw away first line
    fi.readline()

    # now read the text lines
    glunk = fi.readline().strip()
    case_number = 1
    while glunk:
        print("Case #%s: %s" % (case_number, translate(glunk)))
        case_number += 1
        glunk = fi.readline().strip()

              
