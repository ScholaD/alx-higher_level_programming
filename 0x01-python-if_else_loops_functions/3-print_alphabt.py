#!/usr/bin/python3
#3-print_alphabt.py
"""Print all the letters except q and e"""
for char in range(ord('a'), ord('z')+1):
    if char != ord('q') and char != ord('e'):
        print(chr(char), end='')
