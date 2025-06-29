import create_random_strands as generator
from random import choice


def five_three(answer, strand):
    if answer == "Y":
        return strand
    elif answer == "N":
        new_strand = strand[::-1]
        return new_strand
    return None


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
    return None


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
                    ("GUA", "GUU", "GUC", "GUG"): "valine", ("UCA", "UCU", "UCC", "UCG", "AGC"): "serine",
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


def main():
    generator.main()
    with open("example_text.txt") as file_in:
        for line in file_in:
            try:
                line = line.strip()
                line = line.replace(" ", "")
                line = line.split(",")
                joined_strand = line[1]
                strand_type = line[0]
                five_to_three = choice(["Y", "N"])
                prime = five_three(five_to_three, joined_strand)
                converted = convert(strand_type, prime)
                print(f"\nFor the code:\n{joined_strand}\nYour mRNA strand is:\n{converted}\n")
                outcome = split(converted)
                protein = form_proteins(outcome)
                print("Your proteins are:\n")
                [print(f"{p}") for p in protein]
                print("\n")
            except ValueError as error:
                print(f"{error}\n")


try:
    main()
except KeyboardInterrupt:
    print("\n\nGoodbye!")
