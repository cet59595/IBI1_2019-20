# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:35:23 2020

@author: english
"""
import matplotlib.pyplot as plt
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#it can also change into: for i in range(0,10):
#gene_lengths[i]=int(input())
b=0
c=0
for a in range (0,10):  
    if gene_lengths[a]>gene_lengths[b]:
        b=a
    if gene_lengths[c]>gene_lengths[a]:
        c=a
max=gene_lengths[c]
min=gene_lengths[b]
if c>b:   #it is used to make sure that we delete the number at the back
    gene_lengths.remove(max)
    gene_lengths.remove(min)
else:
    gene_lengths.remove(max)
    gene_lengths.remove(min)
    
plt.boxplot(gene_lengths,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,#I can not understand how the showflier works
            notch=False,
            )
plt.show()
