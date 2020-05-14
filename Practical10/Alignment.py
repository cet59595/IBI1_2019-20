#Input three given DNA sequence
seq_mouse = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq_human = "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq_random = "WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
#Compare the human sequence with the mouse sequence
edit_distance1	=	0
for	i in range(len(seq_mouse)):
    if seq_mouse[i] != seq_human[i]:
        edit_distance1 += 1
print(100-edit_distance1/len(seq_mouse)*100)#Output the percentage

#Compare the mouse sequence with the random sequence
edit_distance2	=	0 
for	i in range(len(seq_mouse)):
    if seq_mouse[i] != seq_random[i]:
        edit_distance2 += 1
print(100-edit_distance2/len(seq_mouse)*100)#Output the percentage

#Compare the human sequence with the random sequence
edit_distance3	=	0 
for	i in range(len(seq_human)):
    if seq_random[i] != seq_human[i]:
        edit_distance3 += 1
print(100-edit_distance3/len(seq_human)*100)#Output the percentage