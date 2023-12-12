# genbank2fasta.py

# Function to read the file and return its content as a list of lines
def read_file(file_name):
    try:
         # Attempt to open the specified file in read mode
        with open(file_name, 'r') as file:
             # Read the file content line by line and store it as a list
            content = file.readlines()
             # Return the content of the file as a list of lines
        return content
    except FileNotFoundError:
          # If the file is not found, handle the FileNotFoundError and display an error message
        print(f"File '{file_name}' not found.")
        #used to display output or information to the console
        return []
    #used within a function to exit the function and return a value to the caller

# Function to extract the organism name from the GenBank file content
def extract_organism(file_content):
    organism_name = ''
    for line in file_content:
        #  # Look for a line that starts with 'ORGANISM'
        if line.startswith('  ORGANISM'):
            # Extract the organism name by splitting the line and getting the part after 'ORGANISM'
            organism_name = line.split('  ORGANISM')[1].strip()
            break
    return organism_name
## Exit the loop after finding the organism name
    # Return the extracted organism name


# Function to find genes in the GenBank file content

# Function to find genes in the GenBank file content
def find_genes(file_content):
    genes = []  # Initialize an empty list to store gene information

    for line in file_content:
        if line.startswith('     gene            '):  # Check if the line indicates a gene
            is_antisense = 'complement' in line  # Check if it's an antisense gene
            line = line.replace('     gene            ', '')  # Remove unnecessary prefix
            line = line.replace('<', '').replace('>', '')  # Remove < and > symbols

            # Extract the start and end positions of the gene
            positions = [int(pos.strip()) for pos in line.replace('complement(', '').replace(')', '').split('..')]

            # Determine the start and end positions of the gene
            if len(positions) == 1:
                #checks if the positions list contains only one element. 
                #If so, it assigns that single element to both start and end variables.
                start = end = positions[0]
            else:
                start, end = positions
                #else: is executed when there are two elements in the positions list,
                # assigning them to start and end separately, denoting the gene's start and end positions respectively.

            # Append gene information (start, end, and type) to the list of genes
            if is_antisense:
                genes.append([start, end, 'antisense'])  # Store as antisense gene
            else:
                genes.append([start, end, 'sense'])  # Store as sense gene

    return genes  # Return the list containing information about found genes


#EXTRACTING THE NUCLEOTIDE SEQUENCE OF THE GENOME


def extract_sequence(file_content):
    is_dnaseq = False  # Initialize a boolean flag to track DNA sequence extraction ( variable that holds a boolean value, which can be either True or False)
    dna_sequence = ""  # Initialize an empty string to store the DNA sequence

    for line in file_content:
        if line.strip() == "//":
            is_dnaseq = False  # Set the flag to False when encountering '//' indicating the end of sequence
        if is_dnaseq:
            # Remove non-DNA characters and append valid DNA bases to the 
            #the program considers the current line to be part of the DNA sequence
            #It filters out non-DNA characters from the line and appends valid DNA bases
            dna_sequence += ''.join(filter(lambda x: x.lower() in 'actg', line))
        if line.startswith("ORIGIN"):
            is_dnaseq = True  # Set the flag to True when encountering the 'ORIGIN' line

    # Calculate the length of the extracted DNA sequence
    sequence_length = len(dna_sequence)
    print(f"Number of bases in the extracted sequence: {sequence_length}")

    return dna_sequence  # Return the extracted DNA sequence


    # Calculate the length of the sequence
    sequence_length = len(dna_sequence)
    print(f"Number of bases in the extracted sequence: {sequence_length}")

    return dna_sequence


        #CREATING THE REVERSE COMPLEMENTARY SEQUENCE
        

#dna_sequence = extract_sequence(file_content) #Utilisation de la fonction extract_sequence()


# Function to construct the reverse complementary sequence
def construct_comp_inverse(dna_sequence):
    # Define a dictionary to store the complement of each base
    complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}

    # Create the complementary sequence by replacing each base with its complement
    complementary_sequence = ''.join([complement[base] for base in dna_sequence])
    #replacing each base in dna_sequence with its complement using list comprehension

    # Reverse the complementary sequence to get the reverse complement
    reverse_complement = complementary_sequence[::-1]

    return reverse_complement  # Return the reverse complementary sequence

    
        #WRITING A FASTA FILE
        
# Function to write a FASTA file
def write_fasta(file_name, comment, sequence):
    try:
        with open(file_name, 'w') as file:
            # Write the comment line at the beginning of the file
            file.write(f">{comment}\n")
            
            # Write the sequence in lines no longer than 80 characters
            for i in range(0, len(sequence), 80):
                file.write(sequence[i:i+80] + '\n')

        # Display a success message if the file was created successfully
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        # If an error occurs during file writing, display the error message
        print(f"Error: {e}")

# Set the file name to be written
file_name = 'NC_001133.gbk'

# EXTRACTING GENE 
#function iterates through genes extracted from the GenBank file. For each gene, it extracts the sequence,
#generates a file name, and writes the gene's sequence into a FASTA file using the write_fasta() function
         # Function to extract genes from the complete DNA sequence and create FASTA files for each gene
def extract_genes(genes, complete_sequence, organism_name):
    # Loop through each gene extracted from the GenBank file
    for i, gene in enumerate(genes, start=1):
        start, end, gene_type = gene

        # Extract the gene's sequence from the complete DNA sequence
        gene_sequence = complete_sequence[start - 1: end]
        
        # If the gene is antisense, take the reverse complementary sequence
        if gene_type == 'antisense':
            gene_sequence = construct_comp_inverse(gene_sequence)

        # Create a comment for the gene in FASTA format
        gene_comment = f"{organism_name}|{i}|{start}|{end}|{gene_type}"

        # Generate a file name for the gene's FASTA file
        gene_file_name = f"gene_{i}.fasta"

        # Write the gene's sequence into a FASTA file using the write_fasta function
        write_fasta(gene_file_name, gene_comment, gene_sequence)

        # Display a message indicating the gene has been saved
        print(f"Gene {i} saved in '{gene_file_name}'")

# Main function
def main():
    #function reads the GenBank file, extracts organism information, etc..
    file_name = 'NC_001133.gbk'  # Replace with your GenBank file name
    # Read the contents of the GenBank file
    file_content = read_file(file_name)

    if file_content:
        # Display the number of lines read from the file
        print(f"Number of lines read from '{file_name}': {len(file_content)}")

        # Extract the organism's name from the GenBank file content
        organism_name = extract_organism(file_content)
        if organism_name:
            print(f"Organism Name: {organism_name}")
        else:
            print("Organism name not found in the file.")

        # Find and display genes in the GenBank file
        genes = find_genes(file_content)
        print(f"Number of genes found: {len(genes)}")

        # Count sense and antisense genes
        sense_genes = [gene for gene in genes if gene[2] == 'sense']
         #This line of code creates a new list containing only the genes that have their type as 'sense'
        antisense_genes = [gene for gene in genes if gene[2] == 'antisense']
        #This line of code creates a new list containing only the genes that have their type as 'antisense'
        print(f"Number of sense genes: {len(sense_genes)}")
        print(f"Number of antisense genes: {len(antisense_genes)}")
#isplay the number of genes categorized as 'sense' and 'antisense' respectively
        
        # Extract the complete DNA sequence from the GenBank file
        sequence = extract_sequence(file_content)
        print(sequence)
        # For testing purposes, construct a reverse complementary sequence
        test_sequences = ['atcg', 'AATTCCGG', 'gattaca']
        for seq in test_sequences:
            reverse_comp_seq = construct_comp_inverse(seq.lower())
            #converts the current sequence to lowercase
            print(f"Original Sequence: {seq}, Reverse Complement: {reverse_comp_seq}")

        # Example of writing a FASTA file with the extracted sequence
        file_n = 'test.fasta'
        comment = 'my comment' # # Comment or description for the sequence in the FASTA file
        sequencetest = 'atcgatcgatcg...'  # This would typically be the extracted sequence
        write_fasta(file_n, comment, sequencetest)

        # Extract genes and create FASTA files for each gene
        extract_genes(genes, sequence, organism_name)

# Execute the main function if this script is run as the main program
if __name__ == "__main__":
    main()