#dna_sequence = 'GATGGAACTTGACTACGTAAATT'
#rna_sequence = dna_sequence.replace('T', 'U')
with open('rosalind_rna.txt', 'r') as f:
    f = f.read()
    dna_sequence_list = list(f)
    for i in range(len(dna_sequence_list)):
        if dna_sequence_list[i] == 'T':
            dna_sequence_list[i] = 'U'
    rna_sequence = ''.join(dna_sequence_list)
    print(rna_sequence)