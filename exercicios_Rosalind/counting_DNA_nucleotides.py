#f = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#f = "GCTTTATCAACTTACCTGTTTTTACCTAGTTGTTGTAAGAGTTATACTCCCCTTGCGCGGGGCATAAGAGTGTTTCATATAGGGTTAGCACCGCCTGCCCGTCTAACTCCCTAAATCCATAAGAATCAGCTAAGCGGCACAAGCGGTGACTCGGTCACCGAACTTCACATAAGTATTTGTTTTCCCCCGTGATGGGCCATGCCCCCGCGGAGGAGCGAGTAACCTTTGGACTTCGCTCCTCAAGGTGTGCGTTTGGTTACCGCAATAATCCTAACCTAGGAAGAGCTACTCTACGTCATCGCCAGCGTCGAGCATGTGGCAAGTTCACTCTGTTACTATAAGCGAATTTCTACTCAACCACTGGGAGCCTAGTATACCGAGGTTGCCGATGACGAAATCGCATGCTAGATCGGTGAAGAAGGTGTAAGTGATAACCGATCCATAGGATACGCGGTCTGTCACCTATAAGAGAATACTTGCACGTGGGTCCGTGGGCGTCAATCCCCTGAATAACGTCTCCGTCTCGCTTTGAAGATGCTATCGAACACGGTTTTTGGTCGTTACGTAAAGGCCGATCTGCAACTTAAGGCTCTAATCATATCACGTCATGACATCCAACGATCAGCCTAATCTCGTAACAAAGTGATCCGTTAGTGACCTGGTCTTGCTACAGCATTTATAATGGTTAGATGGCCCTCCATATGACCACGACGAAGGCATTGAGGCTGTAACTTTATGAGGTTATCTCCAATTCTTTGTTTCGCCCACCCCAAACGACTAATGTTATCGTGACACATTGCCGTTGGTCACACGCCTATCTTTGTAGGAAAGGCCGGGGACGTTACGCAACTACCGCCATTGCAGACCACTAATCTCGAGTCTTTTGCTCGCCAAACTCCAAAACCGTGACTTTCGGGCAAATGCCTGAAAGACATCGAAAGCTAGTAAAATAACTAAGGTTCAAACCCGTGGAAATCAAGGTTAGAG"
with open('rosalind_dna.txt', 'r') as f:
    f = f.read()
    n_A = f.count('A')
    n_G = f.count('G')
    n_C = f.count('C')
    n_T = f.count('T')
print(n_A,n_C,n_G,n_T)
