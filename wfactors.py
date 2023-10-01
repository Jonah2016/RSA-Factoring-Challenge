#!/usr/bin/python3
import sys

def factorize_func(num):
    """ Generate the two factors for an unknown num"""
    factor_one = 2
    while (num % factor_one):
        if (factor_one <= num):
            factor_one += 1

    factor_two = num // factor_one
    return (factor_two, factor_one)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

file_name = sys.argv[1]

file = open(file_name, 'r')
content_lines = file.readlines()

for ln in content_lines:
    num = int(ln.rstrip())
    factor_two, factor_one = factorize_func(num)
    print(f"{num} = {factor_two} * {factor_one}")
