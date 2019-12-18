#!/usr/bin/env python3
a = [1,2,3]
b = [x+1 for x in [x ** 2 for x in a]]
print(b,end=",")
