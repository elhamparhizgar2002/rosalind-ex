ex 1 
sequence="CCGGATCTTTAAGCCGCGCCTGAGCTTGGGAAGCTATGTTCCGGCAAACGTAACCATGTTGTTCCGTGTTTTAGTCCTGCTACTCTAACTCACCGTCCGGCTCGTCGAAGGGTTAGAGTAGCTGAAGGGTGTGCGGCTCACGCGCGCTAGCCAGGGTACCCTCGGAGCGCATCGATGCCTAATGGTTAATCCGCTTGGCGTTAAAATGAAAGAGCCGTTTTGAACCGTATGACTGCGAGACATTCTAGTGATCTAGGTCGAGCGGTATTGTTTGACACTTACCTACCTGTCTCTTTAGATCTCACGGCGATTAGCTCGGGACGATGTATGATCGGATTGTCGGTGTAGCCGTTGCGATTAGAGCGGCTCTATCCGCTATGTGGTCGCTAAGTATAATGTATGCGAATCGCTTCTCCAGGAGGAGACTAGTCACAGATGCTGAAATACGATTTTACATATCGATTCAAGCGACGGGTGGAGCGACAATACATATTTCACGCATCCCACGTTTAGTACTATTTCTGGTACAACAGATGACTTAGAGTATCTGTCGTTCGTGTGTGTACCGCTTAACACTGGAGCAGCGTAGGCCCTGGCCTCCAAGTCCTAATCGGGGGATAATACTAAGAGCGTGAGGACCACTACCCTGGGCAAGTAGTCTCCGTATTAGGGATTAGGTCCCACCCCCAAGTACTCGGCAACATAGAAAAGTTCCTTGGGCATGGGGCAGTCACGATTGTATCAGCGAGAAACAAATCCCCCGTTGCCATACTATATCGATAATTTTTACGTGGTCATTATAATATCGCAGTACCCTTTTTACTCGAACGCAAGGCGCCGAGAACATGGATTCCTACCTGCAATGATCGACTGCGCGG"

A = 0
C = 0
T = 0
G = 0

for symbol in sequence:
    if symbol == 'A':
        A = A+1
    elif symbol == 'C':
        C = C+1
    elif symbol == 'T':
        T = T+1
    elif symbol == 'G':
        G = G+1
print(A,"",C,"",T,"",G)
