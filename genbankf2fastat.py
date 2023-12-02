


def extract_organism(file_content):
    organism_line = None

    for line in file_content:
        if line.startswith("ORGANISM"):
            organism_line = line.strip()
            break  # Stop searching once the first occurrence is found

    if organism_line:
        # Extract the organism name from the line
        organism_name = organism_line.split(" ", 1)[1].strip()
        return organism_name
    else:
        print("Error: Organism information not found in the file.")
        return None


def write_fasta(file_name, comment, sequence):
    with open(file_name, 'w') as fasta_file:
        # Write comment line
        fasta_file.write(f'>{comment}\n')

        # Write sequence in lines of maximum 80 characters
        for i in range(0, len(sequence), 80):
            line = sequence[i:i + 80]
            fasta_file.write(f'{line}\n')
  
file_name = 'test.fasta'
comment = 'my comment'
sequence = 'atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg'

write_fasta(file_name, comment, sequence)