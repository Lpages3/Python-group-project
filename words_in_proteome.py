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
    
    return mots_filtres


read_words()