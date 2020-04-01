seq='ATGCGACTACGATCGAGGGCCAT'# it can change into seq=input()
a=len(seq)
c=''
for b in range (0,a): #replace as well as reverasl 
    if seq[b] == 'A':
        c='T'+c
    elif seq[b] == 'T':
        c='A'+c
    elif seq[b] == 'G':
        c='C'+c
    elif seq[b] == 'C':
        c='G'+c
if len(c) == a:
    print(c)
else:
    print('It is not a DNA sequence')
    
    

