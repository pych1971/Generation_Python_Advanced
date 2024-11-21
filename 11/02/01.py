dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
rna = ''
for i in input():
    rna += dna_to_rna[i]
print(rna)
