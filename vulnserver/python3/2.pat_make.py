# Credit to www.phillips321.co.uk for the inspiration for this script

import argparse

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

def pattern_create(length):
    pattern = ""
    a = 0
    b = 0
    c = 0
    while len(pattern) < length:
        pattern += upper[a] + lower[b] + numbers[c]
        c += 1
        if c == len(numbers):
            c = 0
            b += 1
        if b == len(lower):
            b = 0
            a += 1
        if a == len(upper):
            a = 0
    print(pattern[:length])
    print("Length: %i" % length)
    return pattern

def pattern_find(pattern):
    to_locate = input("Enter section of pattern to be located: ")
    offset = pattern.find(to_locate)
    print("Offset is located at " + str(offset))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", help="Specify the desired number of characters for the pattern")
    args = parser.parse_args()
    length = int(args.length)
    pattern = pattern_create(length)
    pattern_find(pattern)

if __name__ == '__main__':
    main()
