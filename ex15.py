#Transitions and transversions



def calculate_transition_transversion_ratio(s1, s2):
    transitions = sum(base1 != base2 and (base1 in "AG" and base2 in "AG" or base1 in "CT" and base2 in "CT") for base1, base2 in zip(s1, s2))
    transversions = sum(base1 != base2 and (base1 in "AG" and base2 in "CT" or base1 in "CT" and base2 in "AG") for base1, base2 in zip(s1, s2))

    if transversions == 0:
        return 0 
    else:
        return transitions / transversions

# Example usage
if __name__ == "__main__":
    s1 ="AACTATTCTCAAGTTAGCGGTGTTAACATGCTGTTCTTAGTCAACAGTTCGACCTACTTACACAGACTAAAAAGAAAAGTACCGGAATCTCGCGCTAATTATTTTGCATAATTTAGGCCACCCTACTTTGGGTTCGAATCTCTATAGGGCCTCCTAGCGCTTGGGTTCCAACCCACATAAGAAATTCCGGTCTCGGAGCCATCATTTATAATGTTTCCCGACGGACAATAGGTGTACAATACGATGATGGGATTACCACGCTACTGCATAGGTTCCTAAGGTCCTGTGGTTTTTTCGTCTCGTTGATTCTATGCCATCACCGGGATGTGTGACCCCCGGCCGAACAGTACCGGTTCATGACGATTGTTTGACATAAACTACTAGACGTGATAATTTGCCAGAACATACAGGATGGGCTGCCCCCAATAGACGGGAAAAATGCCCACTATGGTGCCCCAGTCCGGTGGACTTGCGCACGCTGTAAACGACAATGCTATGTGTGTTCCAAAAGGACGCTAAGTCCGAGTCCATTGGGAAAGATCTGATTCGACGGTACGTCGTATATAGTGTCCAAATTACCTCATCCATAAAGCTAGGAACAAACGATCCACCTTAGTCGTGCATGAATTACTACGACCCTAAGTCAGCGACCAGCCCGGTAGAAAACTTACTTGAACTTTTAGAGAAACTAAGTGGCCAAGCTCAAAAAACGGACCGTGTTATGAGAATCCGTTACGACGCACAACAGTAAAGCTTGACGCGTACGACGGTTCAGCAGCACCCTAAGTTACGTTGACCTCATTAGGAAACGAGGCGTGCACTTTGCTCTTCTTATTACAAACTATGCTATAGAGGGTTGGATTGGTACAGCTAGTGGCAGGGTGA" 
    s2 ="AAATTGCATTAGGTTAGCGGCATTTACTCGAACTTCTTAATCAACAGTTCGACGTATTGACACAGATTCGAGAGAAAGGTGACAGAATTTCACGCTAATCAACCTGCAAAGCTGAGGTCACCCTTTGCTAGGTTCGAACCTCAATAGAGTTTCTTAACGCCTGAGTTCCAATCCACATGAGAAGTCCCGGTCTCGGAACCATCATTTATCAATTCTTCCGACAGACAACATGTATACCATACGCTAATGGTGTAGTCATGTTACTGCATAAGTCCCTAGGGCCCTGCGTTTTACGGATGCCTTTGATTCCATGCCACCACTGGGATGCGTGGCCCCCGGCCGAAAGCTACCGGTCCATGAGAAGTGGTTGACATAAGTAATTAGCTATAATAATTTGCCAATACACTAATGATAGGCTACTCCCAATATACAAAAAGAGTGCCCCTTATGGTACGCTAATGCGGTAGGGTTACGTACGCTGCGAACGACAGAGCTATGTGTGTCCTAAAAGGACACTAAATCCGAACCCACTAGGCCAAATCTTATAGTGTGATAAGTTGTACGGAGTACCTGAACTATCTCATCGGGAGAACAAAGAACCTCCGAACCATTTCGGTAATGCACGGATCACATCGACTCTAAGTCACCGAACGGCCCGTTAAAAAATTCGGTCGATCTTCGGAAGGAGCTAAGTGGCAAAATTTAAAAATTGATTCACGTTATGAGAACCCACCGCCACGAATAACGGTAAAGGTTGACATCTACGATGGTTCAGCAGAACCCCAGGTTGTGTTCGCCATATCGGGACGCGAAGTGCGCACTTTACTCTCTTTATTGCGAGTTACACCACAAATGTTTGGGTTGCTACGGCAAGTGGCAGAGTGT"
    if len(s1) != len(s2):
        print("Error.")
    else:
        ratio = calculate_transition_transversion_ratio(s1, s2)
        print("Transition/Transversion Ratio:", ratio)
