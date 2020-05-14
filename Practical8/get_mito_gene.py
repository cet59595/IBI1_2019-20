import re
Name=[]
gene=[]
L=[]
a=''
b=0
c=0
count=0
i=0
X=''
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.tar','r')#Open the given file
for line in xfile:
    if line.startswith('>'):#Check the first line Of each part
        if a!='':
            gene.append(a)#Get the name of gene
        a=line[1:6]
        X=line
        L.append(X)#Get the length of the gene
        Name.append(a)
        b=b+1
        a=''
    else:
        a=a+line
gene.append(a)
fout=open('mito_gene.fa','w')
#Print the whole code of specific gene
for i in range (b):
    if re.search('Mito',L[i]):        
        line1 = Name[i]+'   '+str(len(gene[i]))+'\n'
        line2 = gene[i]+'\n'
        fout.write(line1)
        fout.write(line2) 
        c=1#Make sure that there exists the DNA sequence
if c == 0:
    print('No such sequence here')
fout.close
try:
    xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.tar','r')
finally:
    if xfile:
        xfile.close()


