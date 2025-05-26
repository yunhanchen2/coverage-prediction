import random

def main():
    input_file = "5000_a_prim.txt"
    output_file = "random_prim.txt"

    n = int(input("How many lines do you want to randomly pick? "))

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sampled = random.sample(lines, n)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(sampled)
    
if __name__ == "__main__":
    main()
