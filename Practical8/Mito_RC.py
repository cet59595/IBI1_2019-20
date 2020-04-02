import re
Name=[]
gene=[]
L=[]
a=''
b=0
c=0
count=0
i=0
X=' '
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.tar','r')
for line in xfile:
    if line.startswith('>'):
        if a!='':
            gene.append(a)
        a=line[1:6]
        X=line
        L.append(X)
        Name.append(a)
        b=b+1
        a=''
    else:
        a=a+line
gene.append(a)
Y=input('please input the file name here')
fout=open(Y,'w')
for i in range (b):
    if re.search('Mito',L[i]):
        seq=gene[i]
        d=len(seq)
        f=''
        for e in range (0,d): 
            if seq[e] == 'A':
                f='T'+f
            elif seq[e] == 'T':
                f='A'+f
            elif seq[e] == 'G':
                f='C'+f
            elif seq[e] == 'C':
                f='G'+f
        line1 = Name[i]+'    '+str(len(gene[i]))+'\n'
        line2 = f+'\n'
        fout.write(line1)
        fout.write(line2)
fout.close
try:
    xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.tar','r')
finally:
    if xfile:
        xfile.close()
