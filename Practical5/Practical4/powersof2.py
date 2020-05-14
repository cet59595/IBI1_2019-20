# -*- coding: utf-8 -*-
#1024 
#In order to get the answer,we should test step by step in order to get the consequence.
#So we can creat a method to let us test every step.
n=2019
b=0
c=str(n)+'='

if n > 2**13:#Make sure that the nymber input is not too large
   print("the number is too large")
else:
   for b in range (0,13):
       if n>=2**(12-b) and n<=2**(13-b):#Test every step to make sure that n is in the range
           c=c+ "+ 2**" +str(12-b)
           n=n-2**(12-b)
       b=b+1
print(c)