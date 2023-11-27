def read_words():
    
    a = 'english-common-words.txt'
    mots_filtres = []
    try:
        with open(a, 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()  # Séparation des mots dans la ligne
                for mot in mots:
                    if mot.isupper() and len(mot) >= 3:
                        mots_filtres.append(mot)
    
        print(mots_filtres)
        long_mots_filtres = len(mots_filtres)
        print("The number of selected wotds are :",long_mots_filtres)
        
    
    except FileNotFoundError:
        print("File not found.")
def read_sequences(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        identifier = None
        sequence = ''
        for line in lines:
            if line.startswith('>'):  # Identifying the protein identifier
                if identifier:
                    sequences[identifier] = sequence
                identifier = line.strip().split('|')[1]  # Extracting protein identifier
                sequence = ''
            else:  # Accumulating protein sequence
                sequence += line.strip()
        if identifier and sequence:  # Adding the last protein sequence
            sequences[identifier] = sequence
    return sequences

def read_sequences(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        identifier = None
        sequence = ''
        for line in lines:
            if line.startswith('>'):  # Identifying the protein identifier
                if identifier:
                    sequences[identifier] = sequence
                identifier = line.strip().split('|')[1]  # Extracting protein identifier
                sequence = ''
            else:  # Accumulating protein sequence
                sequence += line.strip()
        if identifier and sequence:  # Adding the last protein sequence
            sequences[identifier] = sequence
    return sequences

def main():
    file_path = "/Users/lucyarnaud/Desktop/cours_M1/Github_project/Python-group-project/proteins.py"  # Replace with the actual file path
    sequences = read_sequences(file_path)
    
    # Display the number of sequences read
    print(f"Number of sequences read: {len(sequences)}")
    
    # Display the sequence associated with protein O95139
    protein_id = 'O95139'
    if protein_id in sequences:
        print(f"Sequence for protein {protein_id}:")
        print(sequences[protein_id])
    else:
        print(f"No sequence found for protein {protein_id}")

if __name__ == "__main__":
    main()

  