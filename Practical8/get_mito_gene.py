
Name=[]
gene=[]
a=''
b=0
c=0
count=0
i=0
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.tar','r')
for line in xfile:
    if line.startswith('>'):
        if a!='':
            gene.append(a)
        a=line[1:8]
        Name.append(a)
        b=b+1
        a=''
    else:
        a=a+line
gene.append(a)
X=input('please input the gene name here')
Y=input('please in put the gene length here')
for i in range (b):
    if X == Name[i] and Y == str(len(gene[i])):
        print(gene[i])
        c=1
        break
if c == 0:
    print('No such sequence here')
fout=open('mito_gene.fa','w')
line1 = Name[i]+'\n'
line2 = gene[i]
fout.write(line1)
fout.write(line2)
fout.close
try:
    xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.tar','r')
finally:
    if xfile:
        xfile.close()


