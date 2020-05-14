seq=input('Please in put a DNA sequence like"ATGCGACTACGATCGAGGGCCAT"')# it can change into seq=input()
a=len(seq)
c=''
#Get the complementary sequence and change it to 5' to 3'
for b in range (0,a): #replace as well as reverasl 
    if seq[b] == 'A':
        c='T'+c
    elif seq[b] == 'T':
        c='A'+c
    elif seq[b] == 'G':
        c='C'+c
    elif seq[b] == 'C':
        c='G'+c
if len(c) == a:#Test whether the sequence input is a DNA sequence
    print(c)
else:
    print('It is not a DNA sequence')
    
    

