gene_lengths = [0 for i in range(10)]
# input gene_lengths
for i in range(0,10):
    gene_lengths[i] = int(input('please a gene lengths for ten times'))
min = 0
max = 0
# Compare the lengths by running the loop ten times
for i in range (1,10):
    if gene_lengths[min] > gene_lengths[i]:
        min = i#Get the smaller gene length
    if gene_lengths[max] < gene_lengths[i]:
        max = i#Get the larger gene length
# Remove the latter one first otherwise some errors may occur
if min>max:
    gene_lengths.remove(gene_lengths[min])
    gene_lengths.remove(gene_lengths[max])
else:
    gene_lengths.remove(gene_lengths[max])
    gene_lengths.remove(gene_lengths[min])
print (gene_lengths)

#The following is the code to draw the image
import matplotlib.pyplot as plt
plt.boxplot(gene_lengths,vert=True,whis=1.5,
            patch_artist=True,meanline=True,showbox=True,
            showcaps=True,showfliers=True,notch=False)
plt.show()