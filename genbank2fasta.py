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

def main():
    file_name = 'NC_001133.GBK'  # Replace with your GenBank file name
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
    else:
        print("Failed to read file or file is empty.")

if __name__ == "__main__":
    main()

# Function to find genes in the GenBank file content
def find_genes(file_content):
    genes = []

    for line in file_content:
        if line.startswith('     gene            '):  # Check if the line indicates a gene
            is_antisense = 'complement' in line  # Check if it's an antisense gene
            line = line.replace('     gene            ', '')  # Remove unnecessary prefix
            line = line.replace('<', '').replace('>', '')  # Remove < and > symbols
            start, end = map(int, line.split('..'))  # Split and convert to integers

            if is_antisense:
                genes.append([start, end, 'antisense'])
            else:
                genes.append([start, end, 'sense'])

    return genes

def main():
    file_name = 'NC_001133.GBK'  # Replace with your GenBank file name
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

    else:
        print("Failed to read file or file is empty.")

if __name__ == "__main__":
    main()