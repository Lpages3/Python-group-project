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


import requests

def main():
    github_raw_url = 'https://raw.githubusercontent.com/Lpages3/Python-group-project/main/proteins.py?token=GHSAT0AAAAAACLMLSFRM44WEQFH4OH5CD4EZLUD45A'  # Remplacez cela par l'URL brute du fichier
    response = requests.get(github_raw_url)
    
    if response.status_code == 200:
        content = response.text
        # Maintenant, 'content' contient le contenu du fichier spécifié sur GitHub
        # Utilisez 'content' comme vous le souhaitez dans votre script
        # Par exemple, vous pouvez exécuter exec(content) pour exécuter le code directement
        
        # Vous pouvez lire les lignes du contenu ou le traiter comme un script Python
        print(content)
    else:
        print("Erreur lors de la récupération du fichier depuis GitHub")

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
    sequences_with_words = {word: 0 for word in word_list}

    for word in word_list:
        for sequence_id, sequence in protein_sequences.items():
            if word in sequence:
                sequences_with_words[word] += 1
                #print(f"{word} found in sequence {sequence_id}")

    # Display of requested messages
    for word, count in sequences_with_words.items():
        print(f"{word} found in {count} sequences")

    return sequences_with_words

word_list = ['ACCESS', 'ACID', 'ACT']

# To write in terminal
search_words_in_proteome('human-proteome.fasta')

