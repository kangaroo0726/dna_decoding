from random import randint, choice


def generate_coding_template_strand(length):
  code_possibilities_c_t = ["A", "T", "C", "G"]
  random_code = []
  for i in range(length):
    base = random.choice(code_possibilities_c_t)
    random_code.append(base)
  return "".join(random_code)


def generate_mrna_strand(length):
  code_possibilities_m = ["A", "U", "C", "G"]
  random_code = []
  for i in range(length):
    base = random.choice(code_possibilities_m)
    random_code.append(base)
  return "".join(random_code)


def choose_strand_type_and_generate_list(num_entries):
  strand_list = []
  for i in range(num_entries):
    current_length = randint(50, 100)
    template_or_coding = 1
    mrna = 2
    strand_type = randint(1, 2)
    if strand_type == template_or_coding:
      current_strand = generate_coding_template_strand(current_length)
    elif strand_type == mrna:
      current_strand = generate_mrna_strand(current_length)
    strand_list.append(current_strand)
  return strand_list


def write_to_file(filename, strand_list):
  with open(filename, "w") as file_out:
    for strand in strand_list:
      file_out.write(f"{strand}\n")


def main():
  strand_list = choose_strand_type_and_generate_list(10)
  write_to_file("example_text.txt", strand_list)


main()
