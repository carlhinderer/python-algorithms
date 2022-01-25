from enum import IntEnum

Nucleotide = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))


def string_to_gene(s):
    gene = []

    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):         # Don't run off end!
            return gene

        codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon) # add codon to gene

    return gene


def linear_contains(gene, key_codon):
    for codon in gene:
        if codon == key_codon:
            return True
    return False


def binary_contains(gene, key_codon):
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False



if __name__ == '__main__':
    gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

    # Conversion to gene structure
    gene = string_to_gene(gene_str)
    print(gene)

    # Linear Search    
    acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
    assert linear_contains(gene, acg)
    assert not linear_contains(gene, gat)

    # Get Sorted String
    groups = [gene_str[i:i+3] for i in range(0, len(gene_str), 3)]
    codons = [group for group in groups if len(group) == 3]
    codons.sort()
    sorted_gene_str = ''.join(codons)
    sorted_gene = string_to_gene(sorted_gene_str)

    # Binary Search
    assert binary_contains(sorted_gene, acg)
    assert not binary_contains(sorted_gene, gat)
