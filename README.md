# Software group project
#### write how to get it strated ?
Summary 

Introduction
I:English words in the human proteome 
Amino acid composition
words
proteins
searching for words
the most frequent word
Being more comprehensive
II:Genbank to fasta converter 
Reading the file
Extracting the organism name
Finding genes
Extracting the nucleotide sequence of the genome
Creating the reverse complementary sequence
writing fasta file
Extracting genes
Building the final script 


Comprehensive Project Description 

This description will provide a broad overview of this project and its stages, processes and objectives. 
The problem and obstacles encoutered during certain processes will be briefly discussed. 



Introduction

This group project's main goal was to create an extensive codebase and documentation that are kept in a GitHub repository called "pythongroup-project.". There are three subdirectories in the structure: words_in_proteome, genbank2fasta, and pygen. Each of these contains pertinent __init__.py files. There is also a Readme.md file which is an essential component that gives a detailed description of the project along with a working example that highlights the functionality of the code. 


I- English Words in Proteome

The first part of the project called "ENGLISH WORDS IN PROTEOME" aims to search for occurrence of English words in the human proteome sequences. First, the 20 amino acids are used to create English words. Next, the 3000 most common English words are retrieved and processed from an external file.

The project then requires that the human proteome sequences be acquired from a specified file that was obtained from the UniProt database. It is necessary to write functions that can read these sequences and look for English words in them. It is necessary to analyze the frequency of word occurrences within sequences, with a focus on determining the word that occurs the most frequently and estimating its abundance within the proteome.

II- GENBANK TO FASTA CONVERTER

Using the genetic data found in the Saccharomyces cerevisiae yeast chromosome I file, the next project phase entails converting GenBank files to FASTA format. Reading the file, extracting the names of the organisms, identifying and differentiating between sense and antisense genes, extracting the genome's nucleotide sequence, creating reverse complementary sequences, creating FASTA files, and extracting genes with their corresponding sequences are among the functionalities that still need to be developed.


Rewriting the script to include command-line arguments for the GenBank file analysis is the last step. If the supplied file is not present or the script is run without arguments, error messages will be shown. During this phase, the os and sys modules will be used to handle file inputs efficiently.


In the section below, you can find the summary of the code and functions used in the project for both principal parts.

Words 
r = requests.get(url) variable holds the URL string pointing to a resource on the web. In this case, it seems to be a link to a FASTA file containing the human proteome data.
requests.get(url) sends an HTTP GET request to the provided URL. It retrieves the content available at that URL.
The response object (r) holds the result of the HTTP request. It contains information such as the response status, headers, and the content retrieved.
r.text retrieves the content received from the HTTP request made to the specified URL. It provides the text content of the HTTP response.
print("HTML:\n", r.text) prints out the retrieved content (in this case, the text of the HTML response) to the console.
The try block is used to execute the code within it.
In case any error occurs during the execution of the code within the try block, the except block catches the exception and handles it.
If an error occurs during the HTTP request (due to an invalid URL or any other issue), it prints an error message indicating that there was an issue with the URL or with making the GET request.
This code snippet demonstrates a simple implementation of making an HTTP GET request using the requests library and handling potential errors that might occur during the request process.


Gene bank to fasta 

The read_file() function takes a file name as an argument and attempts to open and read the file.
Using a try-except block, it opens the specified file in read mode ('r') and reads its content line by line, storing each line in a list called content.
If the file is not found (FileNotFoundError), it prints an error message and returns an empty list.
The extract_organism() function takes the content of the GenBank file as input and searches for the line starting with ' ORGANISM'.
If found, it extracts the organism name by splitting the line at 'ORGANISM' and retrieving the part after it.
It returns the extracted organism name or an empty string if not found.
The main() function initiates the execution of the code.
It reads the GenBank file, checks if the file content is available, displays the number of lines read from the file, and extracts the organism name from the content.
If the organism name is found, it prints the name; otherwise, it displays a message indicating the absence of the organism name or the failure to read the file.
The construct_comp_inverse() function constructs the reverse complementary sequence of a given DNA sequence.
It creates a dictionary complement mapping each DNA base ('a', 't', 'c', 'g') to its complementary base.
Using a list comprehension, it constructs the complementary sequence (complementary_sequence) by replacing each base with its complement.
Finally, it reverses the complementary_sequence to obtain the reverse complementary sequence and returns it.
The main() function executes various operations on the GenBank file.
After extracting the DNA sequence from the file, it conducts a test by creating reverse complementary sequences for a set of test sequences ('atcg', 'AATTCCGG', 'gattaca').
For each test sequence, it converts the sequence to lowercase (.lower()) and calls the construct_comp_inverse() function to obtain the reverse complementary sequence, then prints the original sequence and its reverse complement.

Problems: A lot of problems were due to conflict issues after trying to merge branches. In fact, sometimes, one person created a branch but, meanwhile, another person could commit changes in the main branch before merging the modifications brought to a specific or several files. To resolve these conflicts, we used the tool included in VScode (merge editor) to solve these problems of merging. Usually, it showed the differences between the diverging files and asked if we wanted to accept the current code or the incomming code that was written in branch.


Conclusion: To conclude, this project allowed us to be more comfortable with python and be able to gain experience and knowledge in this field. Overall, with this project, we had to develop a multidisciplinary approach integrating computational and biological sciences. This project required extensive documentation, structured code development, collaborative Git usage, and thorough exploration of biological data formats.