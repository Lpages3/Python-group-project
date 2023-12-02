



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