from Bio import SeqIO


def remove_intron(dna, introns):
    for intron in introns:
        if intron in dna:
            dna = dna.replace(intron, '')
    print(dna)


seqs = []
# Lê arquivo fasta
records = SeqIO.parse('rosalind_splc.txt', 'fasta')
# itera sobre cada registro no arquivo fasta
for record in records:
    # imprime a sequencia de dna
    seqs.append(record.seq)

dna = seqs[0]
introns = []
for intron in seqs[1:]:
    introns.append(intron)


remove_intron(dna,introns)