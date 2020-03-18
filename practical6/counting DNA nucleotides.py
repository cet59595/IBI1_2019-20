# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:02:37 2020

@author: english
"""
import matplotlib.pyplot as plt
a="ATGCTTCAGAAAGGTCTTACG"#we can also change it into a=input()
b=a.count('A')
c=a.count('T')
d=a.count('G')
e=a.count('C')#it is a method to count evert letter in the DNA
f=['A','T','G','C']
sizes=[b,c,d,e]
explode=[0,0,0,0]
plt.pie(sizes,explode=explode,labels=f,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("pie of the four DNA nucleotides")
plt.show()