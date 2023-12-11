# WORDS

mots_filtres = []

def read_words(file_path):
    try:
        with open(file_path, 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()  # Séparation des mots dans la ligne
                for mot in mots:
                    if len(mot) >= 3:
                        mots_filtres.append(mot.upper())  # Convert words to uppercase

        print(mots_filtres)
        long_mots_filtres = len(mots_filtres)
        print("The number of selected words are:", long_mots_filtres)
        return long_mots_filtres
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0


# PROTEINS

def read_sequences(file_name):
    sequences = {}
    current_id = None
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Extract protein identifier
                identifier = line.split('|')
                if len(identifier) >= 2:
                    current_id = identifier[1]
                    sequences[current_id] = ''
                else:
                    # Handle lines that do not match the expected format
                    pass
            else:
                if current_id is not None:
                    sequences[current_id] += line

    return sequences


# SEARCHING FOR WORDS 1

def search_words_in_proteome(mots_filtres, sequences_dict):
    sequences_with_words = {word: 0 for word in mots_filtres}

    for word in mots_filtres:
        for sequence_id, sequence in sequences_dict.items():
            if word in sequence:
                sequences_with_words[word] += 1

    # Display requested messages
    for word, count in sequences_with_words.items():
        print(f"{word} found in {count} sequences")

    return sequences_with_words


# THE MOST FREQUENT WORD

def find_most_frequent_word(dictionnaire_mots_sequences):
    mot_plus_frequent = max(dictionnaire_mots_sequences, key=dictionnaire_mots_sequences.get)
    compte = dictionnaire_mots_sequences[mot_plus_frequent]

    print(f"=> {mot_plus_frequent} found in {compte} sequences")
    print("2. What is this word?")
    print("This word is:", mot_plus_frequent)
    print("What percentage of the proteome sequences contain this word?")
    nombre_total_sequences = len(sequences_dict)  # Assuming sequences_dict contains all the sequences in the proteome
    pourcentage = (compte / nombre_total_sequences) * 100
    print(round(pourcentage, 2), "% of the proteome sequences contain this word.")


# SEARCHING FOR WORDS 2

def search_words_in_proteome2(mots_filtres, sequences_dict):
    sequences_with_words2 = {word: {'count_sequences': 0, 'count_occurrences': 0} for word in mots_filtres}

    for word in mots_filtres:
        for sequence_id, sequence in sequences_dict.items():
            if word in sequence:
                sequences_with_words2[word]['count_sequences'] += 1
                sequences_with_words2[word]['count_occurrences'] += sequence.count(word)

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
