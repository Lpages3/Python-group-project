# genbank2fasta.py

# Function to read the file and return its content as a list of lines
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

# Function to extract the organism name from the GenBank file content
def extract_organism(file_content):
    organism_name = ''
    for line in file_content:
        if line.startswith('  ORGANISM'):
            # Extract the organism name after 'ORGANISM'
            organism_name = line.split('  ORGANISM')[1].strip()
            break
    return organism_name


# Function to find genes in the GenBank file content

def find_genes(file_content):
    genes = []

    for line in file_content:
        if line.startswith('     gene            '):  # Check if the line indicates a gene
            is_antisense = 'complement' in line  # Check if it's an antisense gene
            line = line.replace('     gene            ', '')  # Remove unnecessary prefix
            line = line.replace('<', '').replace('>', '')  # Remove < and > symbols

            # Extract the start and end positions
            positions = [int(pos.strip()) for pos in line.replace('complement(', '').replace(')', '').split('..')]

            if len(positions) == 1:
                start = end = positions[0]
            else:
                start, end = positions

            if is_antisense:
                genes.append([start, end, 'antisense'])
            else:
                genes.append([start, end, 'sense'])

    return genes





#EXTRACTING THE NUCLEOTIDE SEQUENCE OF THE GENOME


def extract_sequence(file_content):
    is_dnaseq = False
    dna_sequence = ""

    for line in file_content:
        if line.strip() == "//":
            is_dnaseq = False
        if is_dnaseq:
            # Remove digits, spaces, and special characters from the sequence
            dna_sequence += ''.join(filter(lambda x: x.lower() in 'actg', line))
        if line.startswith("ORIGIN"):
            is_dnaseq = True

    # Calculate the length of the sequence
    sequence_length = len(dna_sequence)
    print(f"Number of bases in the extracted sequence: {sequence_length}")

    return dna_sequence


        #CREATING THE REVERSE COMPLEMENTARY SEQUENCE
        

#dna_sequence = extract_sequence(file_content) #Utilisation de la fonction extract_sequence()


# Function to construct the reverse complementary sequence
def construct_comp_inverse(dna_sequence):
    complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    complementary_sequence = ''.join([complement[base] for base in dna_sequence])
    reverse_complement = complementary_sequence[::-1]
    return reverse_complement

    
        #WRITING A FASTA FILE
        
def write_fasta(file_name, comment, sequence):
    try:
        with open(file_name, 'w') as file:
            # Write the comment line
            file.write(f">{comment}\n")
            
            # Write the sequence in lines no longer than 80 characters
            for i in range(0, len(sequence), 80):
                file.write(sequence[i:i+80] + '\n')

        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

file_name = 'NC_001133.gbk'

         #EXTRACTING GENES
        
def extract_genes(genes, complete_sequence, organism_name):
    for i, gene in enumerate(genes, start=1):
        start, end, gene_type = gene

        # Extract the gene's sequence
        gene_sequence = complete_sequence[start-1:end]

        # If the gene is antisense, take the reverse complementary sequence
        if gene_type == 'antisense':
            gene_sequence = construct_comp_inverse(gene_sequence)

        # Create the FASTA file for the gene
        gene_comment = f"{organism_name}|{i}|{start}|{end}|{gene_type}"
        gene_file_name = f"gene_{i}.fasta"
        write_fasta(gene_file_name, gene_comment, gene_sequence)

        print(f"Gene {i} saved in '{gene_file_name}'")

    
def main():
    file_name = 'NC_001133.GBK'  # Replace with your GenBank file name
    # Read the file
    file_content = read_file(file_name)

    if file_content:
        # Display the number of lines read
        print(f"Number of lines read from '{file_name}': {len(file_content)}")

        # Extract the organism name
        organism_name = extract_organism(file_content)
        if organism_name:
            print(f"Organism Name: {organism_name}")
        else:
            print("Organism name not found in the file.")

        # Find and display genes
        genes = find_genes(file_content)
        print(f"Number of genes found: {len(genes)}")
        
        # Count sense and antisense genes
        sense_genes = [gene for gene in genes if gene[2] == 'sense']
        antisense_genes = [gene for gene in genes if gene[2] == 'antisense']
        print(f"Number of sense genes: {len(sense_genes)}")
        print(f"Number of antisense genes: {len(antisense_genes)}")
        
        #Use of extract_sequence() function
        sequence = extract_sequence(file_content)

        # Constructing reverse complementary sequence for testing
        test_sequences = ['atcg', 'AATTCCGG', 'gattaca']
        for seq in test_sequences:
            reverse_comp_seq = construct_comp_inverse(seq.lower())
            print(f"Original Sequence: {seq}, Reverse Complement: {reverse_comp_seq}")

        file_n='test.fasta'
        comment='my comment'
        sequ='atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg'
        write_fasta(file_n,comment,sequence)

        
        extract_genes(genes,sequence,organism_name)


if __name__ == "__main__":
    main()