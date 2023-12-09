#WORDS

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
        
#PROTEINS
   
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


def main():
    file_path = "C:/Users/pages/Documents/Université/Cours/Cours Master 1 Eco-Evo/Software dev/Python-group-project/proteins.py"  # Replace with the actual file path
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

#SEARCHING FOR WORDS 

def read_fasta(file_path):
    sequences = {}
    current_sequence = ""
    current_id = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # New sequence, register previous one if it exist
                if current_id:
                    sequences[current_id] = current_sequence
                current_id = line[1:]  # the sequence identifier is retrieved
                current_sequence = ""  # reset the current sequence
            else:
                # Adding the line to the current sequence
                current_sequence += line

        # Save the last sequence after playing the file
        if current_id:
            sequences[current_id] = current_sequence

    return sequences

def search_words_in_proteome(file_path):
    protein_sequences = read_fasta(file_path)
    sequences_with_words = {word: {'count': 0, 'occurrences': 0} for word in word_list} #We add "occurrences" key to keep track of the total number of times the word appears accross all protein sequences 

    for word in word_list:
        for sequence_id, sequence in protein_sequences.items():
            if word in sequence:
                sequences_with_words[word]['count'] += 1        # Insertion of 'count" method in order to compute the number 
                sequences_with_words[word]['occurrences'] += sequence.count(word) #of occurrences of each word in the sequences 
                #print(f"{word} found in sequence {sequence_id}")

    # Display of requested messages
    for word, count in sequences_with_words.items():
        print(f"{word} found in {counts['count']} sequences")
        print(f"Total occurrences of {word}: {counts['occurrences']}")

    return sequences_with_words

word_list = ['ACCESS', 'ACID', 'ACT']

# To write in terminal
search_words_in_proteome('human-proteome.fasta')

