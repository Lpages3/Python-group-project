#WORDS

mots_filtres = []
    
def read_words(file_path):
    
    a = file_path
    try:
        with open(a, 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()  # words split
                for mot in mots:
                    if mot.isupper() and len(mot) >= 3:
                        mots_filtres.append(mot)
    
        print(mots_filtres)
        long_mots_filtres = len(mots_filtres)
        print("The number of selected wotds are :",long_mots_filtres)
        return long_mots_filtres
    except FileNotFoundError:
        print(f"Fichier '{a}' introuvable.")
        return 0
        
#PROTEINS
   
    except FileNotFoundError:
        print("File not found.")
def read_sequences(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        identifier = None
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):  # Identifying the protein identifier
                parts = line.split('|')
                if len(parts) > 1:
                    identifier = parts[1]  # Extracting protein identifier
                    sequence = ''
            else:  # Accumulating protein sequence
                sequence += line
                if identifier and sequence:  # Adding the last protein sequence
                    sequences[identifier] = sequence
    return sequences


import requests

def main():
    github_raw_url = 'https://raw.githubusercontent.com/Lpages3/Python-group-project/main/proteins.py?token=GHSAT0AAAAAACLMLSFRM44WEQFH4OH5CD4EZLUD45A'  # Remplacez cela par l'URL brute du fichier
    response = requests.get(github_raw_url)
    
    if response.status_code == 200:
        content = response.text
        print(content)
    else:
        print("Erreur lors de la récupération du fichier depuis GitHub")

if __name__ == "__main__":
    main()

#SEARCHING FOR WORDS 

def search_words_in_proteome(mots_filtres, sequences_dict):
    sequences_with_words = {word: 0 for word in mots_filtres} 

    for word in mots_filtres:
        for sequence_id, sequence in sequences_dict.items():
            if word in sequence:
                sequences_with_words[word] += 1  # Increment count for the word

    # Display the counts
    for word, count in sequences_with_words.items():
        print(f"{word} found in {count} sequences")

    return sequences_with_words


#THE MOST FREQUENT WORD

def find_most_frequent_word(dictionnaire_mots_sequences):
    mot_plus_frequent = max(dictionnaire_mots_sequences, key=dictionnaire_mots_sequences.get)
    compte = dictionnaire_mots_sequences[mot_plus_frequent]


    print(f"=> {mot_plus_frequent} found in {compte} séquences")
    print("2. What is this word ?")
    print("This word is : ",mot_plus_frequent)
    print("What percentage of the proteome sequences contain this word ?")
    nombre_total_sequences = len(sequences_dict)  # Assuming that sequences_dict contains all the sequences in the proteome
    pourcentage = (compte / nombre_total_sequences) * 100
    print(round(pourcentage, 2),"% of the proteome sequences contain this word.")

#BEING MORE COMPREHENSIVE


#we execute every fonctions at the end of the first part : displaying all results 

# Appel de la fonction read_words()
read_words('english-common-words.txt')

# Lecture 
sequences_dict = read_sequences('human-proteome.fasta')

# display the number of sequences read
print(f"Number of sequences read : {len(sequences_dict)}")

# show the sequence  prot O95139 
protein_id = 'O95139'
print("sequence associated with the protein O95139",protein_id)
print(sequences_dict[protein_id])

print("SEARCHING FOR WORDS")

# Call the search_words_in_proteome() function and store the returned dictionary in a variable
sequences_with_words_dict = search_words_in_proteome(mots_filtres, sequences_dict)

# Using the find_most_frequent_word() function with the returned dictionary
find_most_frequent_word(sequences_with_words_dict)

# Call the search_words_in_proteome2() function and store the returned dictionary in a variable
def search_words_in_proteome2(mots_filtres, sequences_dict):
    # Define the functionality of search_words_in_proteome2 here
    pass

sequences_with_words_dict2 = search_words_in_proteome2(mots_filtres, sequences_dict)
