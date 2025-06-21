# dna_decoding
Decodes DNA/mRNA strand and outputs amino acids with respect to their specific codons

---

##Overview
This project is meant done with the following constraints:
- No external libraries to be used in main.py
- All ideas and applications in this project must come from high school concepts
- All functions, excluding main, are under 20 line

---

## The technical aspect of DNA transcription:
- mRNA is always read from the 5' to 3' end
- When you've got a template strand, the first step is to convert the template strand to a coding strand by reversing the template strand
- To convert the coding strand to mRNA, exchange each thymine (T) for a uracil (U)
- To start decoding the mRNA strand, you must locate the 'AUG' codon (mapped to methionine), which acts as the start to the sequence of proteins you are decoding for
- The mRNA strand must be traversed in groups of 3 amino acids until it either runs out (indicating a continuing protein sequence) or until it hits one of the "UGA", "UAG", or "UAA" codons, the stop codons preventing further decoding
- In main.py, all proteins are mapped to a specific codon
- A single protein may be mapped to multiple codons

---

## Testing:
main.py imports a testing file, create_random_strands.py. The testing script allows for a file to be generated and written to in order to test the functionality of main.py randomly generated strands (mRNA, coding or template). The user is asked for five_to_three and type_strand input every time a new line in the file is reached in order to test efficiently during a single run of the scripts.

---

## How to run:
1. Download the repository
2. Make sure main.py and create_random_strands.py are in the same directory
3. Run main.py through an IDE or python main.py in terminal
