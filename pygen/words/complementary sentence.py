# Function to construct the reverse complementary sequence
def construct_comp_inverse(dna_sequence):
    complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    complementary_sequence = ''.join([complement[base] for base in dna_sequence])
    reverse_complement = complementary_sequence[::-1]
    return reverse_complement

def main():
    file_name = 'NC_001133.GBK'  # Replace with your GenBank file name
    file_content = read_file(file_name)
    
    if file_content:
        print(f"Number of lines read from '{file_name}': {len(file_content)}")
        
        organism_name = extract_organism(file_content)
        if organism_name:
            print(f"Organism Name: {organism_name}")
        else:
            print("Organism name not found in the file.")
        
        genes = find_genes(file_content)
        if genes:
            print(f"Number of genes found: {len(genes)}")
            sense_genes = [gene for gene in genes if gene[2] == 'sense']
            antisense_genes = [gene for gene in genes if gene[2] == 'antisense']
            print(f"Number of sense genes: {len(sense_genes)}")
            print(f"Number of antisense genes: {len(antisense_genes)}")
        else:
            print("No genes found in the file.")
        
        sequence = extract_sequence(file_content)
        if sequence:
            print(f"Number of bases in the extracted sequence: {len(sequence)}")
            # Constructing reverse complementary sequence for testing
            test_sequences = ['atcg', 'AATTCCGG', 'gattaca']
            for seq in test_sequences:
                reverse_comp_seq = construct_comp_inverse(seq.lower())
                print(f"Original Sequence: {seq}, Reverse Complement: {reverse_comp_seq}")
        else:
            print("Failed to extract sequence or sequence is empty.")
