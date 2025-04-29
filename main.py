import sys
import random


def five_three(answer, strand):
    if answer == "Y":
        return strand
    elif answer == "N":
        new_strand = strand[::-1]
        return new_strand


def generate_random_code(random_response, type_strand):
    code_possibilities_m = ["A", "U", "C", "G"]
    code_possibilities_c_t = ["A", "T", "C", "G"]
    random_code = []
    if random_response == "R":
        for i in range(64):
            if type_strand == "m":
                base = random.choice(code_possibilities_m)
                random_code.append(base)
            elif type_strand == "c" or type_strand == "t":
                base = random.choice(code_possibilities_c_t)
                random_code.append(base)
        return "".join(random_code)
    else:
        return random_response


def convert(type_strand, strand):
    if type_strand == "m":
        for char in strand:
            if char not in ["A", "U", "C", "G"]:
                sys.exit("Error: Malformed strand")
        return strand
    elif type_strand == "t":
        new_strand = strand[::-1]
        new_strand_l = []
        for char in new_strand:
            new_strand_l.append(char)
        for i in range(len(new_strand_l)):
            if new_strand_l[i] == "T":
                new_strand_l[i] = "A"
            elif new_strand_l[i] == "A":
                new_strand_l[i] = "U"
            elif new_strand_l[i] == "G":
                new_strand_l[i] = "C"
            elif new_strand_l[i] == "C":
                new_strand_l[i] = "G"
            else:
                sys.exit("Error: Malformed strand")
        new_strand_s = ''.join(new_strand_l)
        return new_strand_s
    elif type_strand == "c":
        new_strand_l = []
        for char in strand:
            if char in ["A", "C", "G", "T"]:
                new_strand_l.append(char)
            else:
                sys.exit("Error: Malformed strand")
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
    protein_dict = {"AUG": "methionine", ("UUU", "UUC"): "phenylalanine", ("UUA", "UUG", "CUA", "CUU", "CUC", "CUG"):
        "leucine", ("AUA", "AUU", "AUC"): "isoleucine", ("GUA", "GUU", "GUC", "GUG"): "valine", ("UCA", "UCU", "UCC",
                                                                                                 "UCG"): "serine",
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
        return proteins
    else:
        sys.exit("Error: Methionine not found")


def main():
    first_strand = input("Enter the original strand ('r' for random strand): ").upper()
    joined_strand = first_strand.replace(" ", "")
    strand_type = input("Type of Strand (m, t, c): ").lower()

    while strand_type not in ["m", "t", "c"]:
        print("Please enter a valid value.")
        strand_type = input("Type of Strand (m, t, c): ").lower()

    five_to_three = input("Five to Three? (Y/N): ").upper()

    while five_to_three not in ["Y", "N"]:
        print("Please enter a valid value.")
        five_to_three = input("Five to Three? (Y/N): ").upper()

    check_random = generate_random_code(joined_strand, strand_type)
    prime = five_three(five_to_three, check_random)
    converted = convert(strand_type, prime)
    print(f"\nFor the code:\n{check_random}\nYour mRNA strand is:\n{converted}\n")
    outcome = split(converted)
    protein = form_proteins(outcome)
    print("Your proteins are:\n")
    [print(f"{p}") for p in protein]


main()
