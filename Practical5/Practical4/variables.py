# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:42:11 2020

@author: english
"""
a=520
b=520520
print(b%7)
c=b/7
d=c/11
e=d/13
print(e)
print("It is same to the 'a'because 7*11*13=1001")
x=True
y=False
z=(x and not y) or (y and not x)
w=(x!=y)
print("z=",z ,"w=",w)
if w==z:
    print("W and Z are always same")