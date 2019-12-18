#!/usr/bin/env python3

#1 list basic command
a = [23,45,1,-3434,43624356,234]
#list append(number)
a.append(45)
#list insert(index,number)
a.insert(0,1)
#list count(number)
a.count(45)
#list remove(number)
a.remove(234)
#list reverse
a.reverse()
#list extend(listname)
b = [45, 56, 90]
a.extend(b)
#list sort()
a.sort()
#list del listname[index]
del a[-1]

#2 list use list as stack and queue
# stack is a LIFO(Last In First Out)data structure.
# we use listname.pop() to implementing the two  principles.
c = [1,2,3,4,5,6]
c.pop()

# queue is a FIFO(First In First Out)data structure.
c.pop(0)

#3 tuple
a = 'Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus'

