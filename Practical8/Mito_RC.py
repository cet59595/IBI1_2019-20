Name=[]
gene=[]
a=''
#I have tried and checked the code for more than an hour but It still lack 4 sequences in the file that I want to creat
#Could it possible to let me what had happened in my code? If it is possible, could you sent a email to Ertuo.19@intl.zju.edu.cn?
#I would appreciate it if you could give my any advices. Thanks
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
X=input('please input the file name here')
fout=open(X,'w')
for i in range (b):
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
