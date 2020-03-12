# -*- coding: utf-8 -*-
#1024 
n=2019
b=0
c=str(n)+'='
while b <= 12:
 if n > 2**13:
   print("the number is too large")
 else:
   for b in range (0,13):
       if n>=2**(12-b) and n<=2**(13-b):
           c=c+ "+ 2**" +str(12-b)
           n=n-2**(12-b)
       b=b+1
print(c)