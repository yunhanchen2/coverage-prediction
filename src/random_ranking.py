import random

def generate_rankings():
    num_lines = int(input("How many sushi rankings do you want to generate? "))

    output_file = "random_sushi_rankings.txt"
    sushi_ids = list(range(10))
    rankings = []

    for _ in range(num_lines):
        ranking = random.sample(sushi_ids, len(sushi_ids))
        rankings.append(' '.join(map(str, ranking)))

    with open(output_file, "w") as f:
        for line in rankings:
            f.write(line + "\n")

if __name__ == "__main__":
    generate_rankings()

