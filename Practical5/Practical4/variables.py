# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:42:11 2020

@author: english
"""5
a=int(input('Please in put a 3-digit number (e.g. 123). '))#input a
b=int(input('Please input a six-digit number, created by writing the digits of a twice (in this example, 123123). '))#input b
print(b%7)
c=b/7
d=c/11
e=d/13
print(e)#Test the numerical value of e
if e==a:
    print("It is same to the 'a'because 7*11*13=1001")
x=True
y=False
z=(x and not y) or (y and not x)
w=(x!=y)
print("z=",z ,"w=",w)
if w==z:#Comparew and z to get the final result
    print("W and Z are always same")