#!/usr/bin/env python3
a = [1,2,3]
b = []
for x in a:
    b.insert(x - 1, x**2)
for x in b:
    print(x+1,end=",")
