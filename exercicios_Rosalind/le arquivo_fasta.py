from Bio import SeqIO

seqs = []
# Lê arquivo fasta
records = SeqIO.parse('rosalind_splc.txt', 'fasta')
# itera sobre cada registro no arquivo fasta
for record in records:
    #imprime a sequencia de dna
    seqs.append(record.seq)
print(seqs)
print(seqs[0])
