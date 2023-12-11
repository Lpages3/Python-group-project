# WORDS

mots_filtres = []  # creating an empty list to store filtered words

def read_words(file_path):
    try:
        with open(file_path, 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()  # splitting the words by line
                for mot in mots:
                    if len(mot) >= 3:
                        mots_filtres.append(mot.upper())  # Convert words to uppercase

        long_mots_filtres = len(mots_filtres)  # calculates the length of mots_filtres
        print("The number of selected words are:", long_mots_filtres)
        return mots_filtres
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []


# PROTEINS

def read_sequences(file_name):
    sequences = {}
    current_id = None
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                identifier = line.split('|')
                if len(identifier) >= 2:
                    current_id = identifier[1]
                    sequences[current_id] = ''
                else:
                    pass
            else:
                if current_id is not None:
                    sequences[current_id] += line

    return sequences


# SEARCHING FOR WORDS

def search_words_in_proteome(mots_filtres, sequences_dict):
    sequences_with_words = {word: {'count_sequences': 0, 'count_occurrences': 0} for word in mots_filtres}

    for sequence_id, sequence in sequences_dict.items():
        for word in mots_filtres:
            occurrences = sequence.count(word)
            if occurrences > 0:
                sequences_with_words[word]['count_sequences'] += 1
                sequences_with_words[word]['count_occurrences'] += occurrences

    # Find the most frequent word
    most_frequent_word = max(sequences_with_words, key=lambda k: sequences_with_words[k]['count_occurrences'])
    occurrences = sequences_with_words[most_frequent_word]['count_occurrences']

    print("SEARCHING FOR WORDS")
    for word, counts in sequences_with_words.items():
        if counts['count_sequences'] > 0:
            print(f"{word} found in {counts['count_sequences']} sequences with {counts['count_occurrences']} occurrences.")

    print(f"The most frequent word in the human proteome is '{most_frequent_word}' with {occurrences} occurrences.")

    # Calculate the percentage of the proteome in which the most frequent word is found
    nombre_total_sequences = len(sequences_dict)
    percentage = (sequences_with_words[most_frequent_word]['count_sequences'] / nombre_total_sequences) * 100

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
