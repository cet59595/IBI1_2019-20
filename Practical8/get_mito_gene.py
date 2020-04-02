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
fout=open('mito_gene.fa','w')
for i in range (b):
    if re.search('Mito',L[i]):        
        line1 = Name[i]+'   '+str(len(gene[i]))+'\n'
        line2 = gene[i]+'\n'
        fout.write(line1)
        fout.write(line2) 
        c=1
if c == 0:
    print('No such sequence here')
fout.close
try:
    xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.tar','r')
finally:
    if xfile:
        xfile.close()


