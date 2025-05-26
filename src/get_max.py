import itertools

def load_preferences(filename, p):
    preferences = []
    with open(filename, 'r') as f:
        for line in f:
            ranking = list(map(int, line.strip().split()))
            preferences.append(set(ranking[:p]))
    return preferences

def compute_reward(S, preferences):
    return sum(1 for pref in preferences if not pref.isdisjoint(S))

def find_best_assortment(preferences, k, n):
    best_S = None
    best_reward = -1
    for S in itertools.combinations(range(n), k):
        reward = compute_reward(set(S), preferences)
        if reward > best_reward:
            best_reward = reward
            best_S = set(S)
    return best_S, best_reward

def main():
    filename = input("Please input the filename: ")
    p = int(input("How many top preferred categories will be picked? (e.g., 3): "))
    k = int(input("How many sushi do you want to pick to serve customers? (e.g., 5): "))
    n = int(input("How many total sushi types are there? (e.g., 100): "))

    preferences = load_preferences(filename, p)
    best_S, reward = find_best_assortment(preferences, k, n)

    print(f"\n Best S (size {k}): {sorted(best_S)}")
    print(f" Covered {reward} out of {len(preferences)} customers")

if __name__ == "__main__":
    main()
