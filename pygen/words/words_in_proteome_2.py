# WORDS

mots_filtres = []     #creating an empty list to store filted words 

def read_words(file_path):   #we define the read_words function to use the english-common-words.txt
    try:
        with open(file_path, 'r') as fichier: #we open the file in read mode and asigne it to fichier 
            for ligne in fichier:
                mots = ligne.split()  # spliting the words by line 
                for mot in mots:
                    if len(mot) >= 3:
                        mots_filtres.append(mot.upper())  # Convert words to uppercase

        print(mots_filtres)
        long_mots_filtres = len(mots_filtres)  #calculates the length (number of elements) of the mots_filtres list
        print("The number of selected words are:", long_mots_filtres) 
        return long_mots_filtres
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0


# PROTEINS

def read_sequences(file_name): # we define the function read_sequences
    sequences = {}
    current_id = None #These lines initialize an empty dictionary called sequences and a variable current_id with a value of None. 
    with open(file_name, 'r') as file: #opens the file specified by file_name in read mode ('r') and assigns it to the variable file.
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Extract protein identifier
                identifier = line.split('|')    # we split the identifier by line 
                if len(identifier) >= 2:       # if verify that their is at least 2 element making it a sequency 
                    current_id = identifier[1]
                    sequences[current_id] = ''
                else:
                    # Handle lines that do not match the expected format
                    pass
            else:
                if current_id is not None:
                    sequences[current_id] += line

    return sequences  # number of seaquences read 


# SEARCHING FOR WORDS 

def search_words_in_proteome(mots_filtres, sequences_dict):  # we define that the function search_words_in_proteome has 2 parameters : the list created in WORDS and the fasta file
    sequences_with_words = {word: 0 for word in mots_filtres} 

    for word in mots_filtres:    
        for sequence_id, sequence in sequences_dict.items(): 
            if word in sequence: 
                sequences_with_words[word] += 1  # if word are in the previous sequence, we pu them in "sequences_with_words"

    # Display requested messages
    for word, count in sequences_with_words.items():     
        print(f"{word} found in {count} sequences") 

    return sequences_with_words


# THE MOST FREQUENT WORD

def find_most_frequent_word(dictionnaire_mots_sequences):   #we define the function  
    mot_plus_frequent = max(dictionnaire_mots_sequences, key=dictionnaire_mots_sequences.get) #the most frequend words is the maximum found dictionaire_mots_sequences
    compte = dictionnaire_mots_sequences[mot_plus_frequent] #we count in how many sequence this most frequent word appear 

    print(f"=> {mot_plus_frequent} found in {compte} sequences")
    print("2. What is this word?")
    print("This word is:", mot_plus_frequent)
    print("What percentage of the proteome sequences contain this word?")
    nombre_total_sequences = len(sequences_dict)  # Assuming sequences_dict contains all the sequences in the proteome
    pourcentage = (compte / nombre_total_sequences) * 100 #we calculate the precentage with a cross product 
    print(round(pourcentage, 2), "% of the proteome sequences contain this word.")


# BEING MORE COMPREHENSIVE

def search_words_in_proteome2(mots_filtres, sequences_dict):    #we define that the function search_words_in_proteome2 has the same 2 parameters as the first one
    sequences_with_words2 = {word: {'count_sequences': 0, 'count_occurrences': 0} for word in mots_filtres}  #

    for word in mots_filtres:
        for sequence_id, sequence in sequences_dict.items():
            if word in sequence:
                sequences_with_words2[word]['count_sequences'] += 1
                sequences_with_words2[word]['count_occurrences'] += sequence.count(word) #we count the occurence of the sequences 

    # Display requested messages
    for word, counts in sequences_with_words2.items():
        print(f"{word} found in {counts['count_sequences']} sequences with {counts['count_occurrences']} occurrences.")

    # Find the most frequent word
    most_frequent_word = max(sequences_with_words2, key=lambda k: sequences_with_words2[k]['count_occurrences'])
    occurrences = sequences_with_words2[most_frequent_word]['count_occurrences']

    print(f"The most frequent word in the human proteome is '{most_frequent_word}' with {occurrences} occurrences.")

    return sequences_with_words2


# Call the read_words() function
read_words('english-common-words.txt')

# Read protein sequences
sequences_dict = read_sequences('human-proteome.fasta')

# Display the number of sequences read
print(f"Number of sequences read: {len(sequences_dict)}") 

# Display the sequence associated with the protein O95139 (for testing purposes)
protein_id = 'O95139'
print("Sequence associated with the protein", protein_id)
print(sequences_dict.get(protein_id, "Protein not found"))

print("SEARCHING FOR WORDS 1")

# Call the search_words_in_proteome() function and store the returned dictionary in a variable
sequences_with_words_dict = search_words_in_proteome(mots_filtres, sequences_dict)

# Using the find_most_frequent_word() function with the returned dictionary
find_most_frequent_word(sequences_with_words_dict)

print("SEARCHING FOR WORDS 2")

# Call the search_words_in_proteome2() function and store the returned dictionary in a variable
sequences_with_words_dict2 = search_words_in_proteome2(mots_filtres, sequences_dict)
