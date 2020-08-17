#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string

n=int(input())
x=string.ascii_lowercase
list1=[]
for i in range(n):
    a='-'.join(x[i:n])
    list1.append((a[::-1]+a[1:]))

width=len(list1[0]) # or width=(4*n)-3 ; this is basically the maximum width (row length) of the matrix

for i in range(n-1,0,-1):
    print(list1[i].center(width,'-'))

for i in range(n):
    print(list1[i].center(width,'-'))

