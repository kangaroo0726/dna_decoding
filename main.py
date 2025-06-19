import random


def five_three(answer, strand):
    if answer == "Y":
        return strand
    elif answer == "N":
        new_strand = strand[::-1]
        return new_strand


def convert(type_strand, strand):
    if type_strand == "m":
        for char in strand:
            if char not in ["A", "U", "C", "G"]:
                raise ValueError(f"Malformed Strand: {char} not valid")
        return strand
    elif type_strand == "t":
        new_strand = strand[::-1]
        new_strand = list(new_strand)
        complement_dict = {"T": "A", "A": "U", "G": "C", "C": "G"}
        for i in range(len(new_strand)):
            try:
                new_strand[i] = complement_dict[new_strand[i]]
            except KeyError:
                raise ValueError(f"Malformed Strand: {new_strand[i]} not valid")
        new_strand = ''.join(new_strand)
        return new_strand
    elif type_strand == "c":
        new_strand_l = []
        for char in strand:
            if char in ["A", "C", "G", "T"]:
                new_strand_l.append(char)
            else:
                raise ValueError(f"Malformed Strand: {char} not valid")
        for i in range(len(new_strand_l)):
            if new_strand_l[i] == "T":
                new_strand_l[i] = "U"
        new_strand_s = ''.join(new_strand_l)
        return new_strand_s


def split(strand):
    first_strand_l = []
    i = 0
    while i + 2 < len(strand):
        if strand[i] == "A" and strand[i + 1] == "U" and strand[i + 2] == "G":
            first_strand_l.append("AUG")
            i += 3
            while i + 2 < len(strand):
                codon = strand[i:i + 3]
                if codon not in ["UGA", "UAA", "UAG"]:
                    first_strand_l.append(codon)
                    i += 3
                else:
                    first_strand_l.append(codon)
                    break
            return first_strand_l
        else:
            i += 1
    return first_strand_l


def form_proteins(strand):
    proteins = []
    protein_dict = {"AUG": "methionine", ("UUU", "UUC"): "phenylalanine",
                    ("UUA", "UUG", "CUA", "CUU", "CUC", "CUG"): "leucine", ("AUA", "AUU", "AUC"): "isoleucine",
                    ("GUA", "GUU", "GUC", "GUG"): "valine", ("UCA", "UCU", "UCC", "UCG"): "serine",
                    ("CCA", "CCU", "CCC", "CCG"): "proline", ("ACA", "ACU", "ACC", "ACG"): "threonine",
                    ("GCA", "GCU", "GCC", "GCG"): "alanine", ("UAU", "UAC"): "tyrosine", ("CAU", "CAC"): "histidine",
                    ("CAA", "CAG"): "glutamine", ("AAU", "AAC"): "asparagine", ("AAA", "AAG"): "lysine",
                    ("GAU", "GAC"): "aspartate", ("GAA", "GAG"): "glutamate", ("UGU", "UGC"): "cysteine",
                    "UGG": "tryptophan", ("AGA", "AGG", "CGA", "CGU", "CGC", "CGG"): "arginine",
                    ("GGA", "GGU", "GGC", "GGG"): "glycine", ("UAA", "UGA", "UAG"): "stop"}
    if len(strand) != 0:
        for sequence in strand:
            for key in protein_dict.keys():
                if sequence in key:
                    proteins.append(protein_dict[key])
                    break
        if "stop" not in proteins:
            proteins.append("...")
        return proteins
    else:
        raise ValueError("Error: Methionine not found")


def read_parse_file(filename):
    try:
        with open(filename) as file_in:
            for line in file_in:
                line = line.strip()
                line = line.replace(" ", "")
                joined_strand = line
                strand_type = input("Type of Strand (m, t, c): ").lower()

                while strand_type not in ["m", "t", "c"]:
                    print("Please enter a valid value.")
                    strand_type = input("Type of Strand (m, t, c): ").lower()

                five_to_three = input("Five to Three? (Y/N): ").upper()
                
                while five_to_three not in ["Y", "N"]:
                    print("Please enter a valid value.")
                    five_to_three = input("Five to Three? (Y/N): ").upper()

                prime = five_three(five_to_three, joined_strand)
                converted = convert(strand_type, prime)
                print(f"\nFor the code:\n{check_random}\nYour mRNA strand is:\n{converted}\n")
                outcome = split(converted)
                protein = form_proteins(outcome)
                print("Your proteins are:\n")
                [print(f"{p}") for p in protein]
    except FileNotFound:
        print("File has not been found. Please enter a valid filename.")


def main():
    try:
        read_parse_file("example_text.txt")
    except ValueError as error:
        print(error)


try:
    main()
except KeyboardInterrupt:
    print("\n\nGoodbye!")
