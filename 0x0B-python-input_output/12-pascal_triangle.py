#!/usr/bin/python3
'''
-> pascal_triangle
'''


def pascal_triangle(n):
    ''' Create a list of list representing pascal triangle '''

    tri = []
    if n == 0:
        return tri

    tri.append([1])

    for i in range(1, n):
        b = tri[-1]
        a = [1]
        for i in range(len(b) - 1):
            a.append(b[i] + b[i + 1])
        a += [1]
        tri.append(a)

    return tri
