# get the top n sushi from the file --- consisting with the corresponding value
def load_user_preferences(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        preferences = []
        for line in f:
            ids = list(map(int, line.strip().split()))
            preferences.append(set(ids[:top_n]))
        return preferences

# get the input from the user --- end when press the enter
def get_user_input():
    print("Enter the sushi IDs you want to serve (space-separated). Press Enter when done:")
    input_ids = input().strip()
    chosen_set = set(map(int, input_ids.split()))
    return chosen_set

# compute the revenue
def compute_revenue(S, user_prefs):
    covered = sum(1 for prefs in user_prefs if not prefs.isdisjoint(S))
    total = len(user_prefs)
    return covered, covered / total

def main():
    filename = "5000_a_prim.txt"
    top_n = int(input("How many top-ranked items per user should be considered? (e.g., 3): "))

    user_prefs = load_user_preferences(filename, top_n)
    S = get_user_input()

    covered_count, revenue = compute_revenue(S, user_prefs)

    print(f"\nChosen sushi set S: {sorted(S)}")
    print(f"Covered {covered_count} out of {len(user_prefs)} users")
    print(f"Revenue (coverage rate): {revenue:.4f}")

if __name__ == "__main__":
    main()