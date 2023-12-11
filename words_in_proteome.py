# WORDS

mots_filtres = []  # creating an empty list to store filtered words

def read_words(file_path): #we define the read_words function to use the english-common-words.txt
    try:
        with open(file_path, 'r') as fichier: #we open the file in read mode and asigne it to fichier 
            for ligne in fichier:
                mots = ligne.split()  # splitting the words by line
                for mot in mots:
                    if len(mot) >= 3:
                        mots_filtres.append(mot.upper())  # Convert words to uppercase

        long_mots_filtres = len(mots_filtres)  # calculates the length (number of elements) of mots_filtres
        print("The number of selected words are:", long_mots_filtres)
        return mots_filtres
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []


# PROTEINS

def read_sequences(file_name): # we define the function read_sequences
    sequences = {}
    current_id = None #These lines initialize an empty dictionary called sequences and a variable current_id with a value of None. 
    with open(file_name, 'r') as file:  #opens the file specified by file_name in read mode ('r') and assigns it to the variable file.
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Extract protein identifier
                identifier = line.split('|') # we split the identifier by line 
                if len(identifier) >= 2:    # if verify that their is at least 2 element making it a sequency 
                    current_id = identifier[1]
                    sequences[current_id] = ''
                else:
                    # Handle lines that do not match the expected format
                    pass
            else:
                if current_id is not None:
                    sequences[current_id] += line

    return sequences # number of seaquences read 


# SEARCHING FOR WORDS

def search_words_in_proteome(mots_filtres, sequences_dict): # we define that the function search_words_in_proteome has 2 parameters : the list created in WORDS and the fasta file
    sequences_with_words = {word: {'count_sequences': 0, 'count_occurrences': 0} for word in mots_filtres}

    for sequence_id, sequence in sequences_dict.items():
        for word in mots_filtres:
            occurrences = sequence.count(word)
            if occurrences > 0:
                sequences_with_words[word]['count_sequences'] += 1 # if word are in the previous sequence, we pu them in "sequences_with_words"
                sequences_with_words[word]['count_occurrences'] += occurrences #we count the occurence of the sequences 

    # Find the most frequent word
    most_frequent_word = max(sequences_with_words, key=lambda k: sequences_with_words[k]['count_occurrences']) #the most frequend words is the maximum found dictionaire_mots_sequences
    occurrences = sequences_with_words[most_frequent_word]['count_occurrences'] #we count in how many sequence this most frequent word appear and how many occurrences there are 

    print("SEARCHING FOR WORDS")
    for word, counts in sequences_with_words.items():
        if counts['count_sequences'] > 0:
            print(f"{word} found in {counts['count_sequences']} sequences with {counts['count_occurrences']} occurrences.")

    print(f"The most frequent word in the human proteome is '{most_frequent_word}' with {occurrences} occurrences.")

    # Calculate the percentage of the proteome in which the most frequent word is found
    nombre_total_sequences = len(sequences_dict) # Assuming sequences_dict contains all the sequences in the proteome
    percentage = (sequences_with_words[most_frequent_word]['count_sequences'] / nombre_total_sequences) * 100 #we calculate the precentage with a cross product 

    print(f"{round(percentage, 2)}% of the proteome sequences contain the most frequent word.")

    return sequences_with_words


# Call the read_words() function
mots_filtres = read_words('english-common-words.txt')

# Read protein sequences
sequences_dict = read_sequences('human-proteome.fasta')

# Display the number of sequences read
print(f"Number of sequences read: {len(sequences_dict)}")

# Display the sequence associated with the protein O95139 (for testing purposes)
protein_id = 'O95139'
print("Sequence associated with the protein", protein_id)
print(sequences_dict.get(protein_id, "Protein not found"))

# Call the search_words_in_proteome() function
sequences_with_words_dict = search_words_in_proteome(mots_filtres, sequences_dict)
