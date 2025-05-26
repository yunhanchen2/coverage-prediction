import json
from openai import OpenAI
from tqdm import tqdm
import random


client = OpenAI()

#load the data (sushi features and sushi users)
def load_user_features(path):
    with open(path, 'r') as f:
        return [line.strip().split() for line in f]

def load_sushi_features(path):
    with open(path, 'r') as f:
        return [line.strip().split() for line in f]

#change numbers to text
minor_group_map = {
    "0": "aomono (blue-skinned fish)", "1": "akami (red meat fish)", "2": "shiromi (white-meat fish)",
    "3": "tare (eel sauce)", "4": "clam or shell", "5": "squid or octopus", "6": "shrimp or crab",
    "7": "roe", "8": "other seafood", "9": "egg", "10": "meat", "11": "vegetable"
}

def user_to_text(user):
    gender = "male" if user[1] == "0" else "female"
    age_map = {"0": "15–19", "1": "20–29", "2": "30–39", "3": "40–49", "4": "50–59", "5": "60+"}
    age = age_map.get(user[2], "unknown")
    same_place = "yes" if user[10] == "0" else "no"
    return (
        f"This person is a {gender} aged {age}. "
        f"Has same childhood and current location: {same_place}. "
        f"Moved from prefecture {user[4]} to {user[7]}, region {user[5]} to {user[8]}, east/west {user[6]} to {user[9]}."
    )

def sushi_to_text(sushi):
    style = "maki" if sushi[2] == "0" else "non-maki"
    major = "seafood" if sushi[3] == "0" else "non-seafood"
    minor = minor_group_map.get(sushi[4], "unknown")

    try:
        taste_score = float(sushi[5])
        if taste_score <= 0.8:
            taste_index = 0
        elif taste_score <= 1.6:
            taste_index = 1
        elif taste_score <= 2.4:
            taste_index = 2
        elif taste_score <= 3.2:
            taste_index = 3
        else:
            taste_index = 4
    except:
        taste_index = 2
    taste = ["very heavy", "heavy", "medium", "light", "very light"][taste_index]

    try:
        freq_score = float(sushi[6])
        if freq_score <= 0.5:
            freq_index = 0
        elif freq_score <= 1.5:
            freq_index = 1
        elif freq_score <= 2.5:
            freq_index = 2
        else:
            freq_index = 3
    except:
        freq_index = 2
    eat_freq = ["rarely", "sometimes", "often", "very frequently"][freq_index]

    try:
        price_val = float(sushi[7])
    except:
        price_val = 0.5
    price_label = f"price score {price_val:.2f}"

    try:
        availability_score = float(sushi[8])
        availability = "commonly sold" if availability_score >= 0.5 else "less commonly sold"
    except:
        availability = "unknown"

    return f"{sushi[1]} (ID {sushi[0]}): {style}, {major}, {minor}, taste: {taste}, eaten {eat_freq}, {availability}, {price_label}."


# make prompts and call GPT
def build_prompt(user_row, sushi_rows):
    user_text = user_to_text(user_row)

    sushi_rows = sushi_rows.copy()
    random.shuffle(sushi_rows)

    sushi_info = "\n".join([sushi_to_text(s) for s in sushi_rows])
    
    prompt = f"""
User profile:
{user_text}

Sushi items (format: ID:name:major:minor:taste:freq:price:avail):
{sushi_info}

Please simulate a sushi ranking this person would produce.
Please avoid always ranking the same item first across people.
Return **exactly 10 unique integers from 0 to 9**, in order of preference, like:
3 1 7 2 5 0 8 9 4 6
"""
    return prompt

def get_gpt_ranking(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=1.05,
        messages=[
            {"role": "system", "content": "You are a helpful assistant simulating sushi preferences."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# main func read file ---> construct GPT ---> generate data ---> store the data
def main():
    user_file = "sushi_u.txt"
    sushi_file = "sushi_i_a.txt"
    output_txt = "sushi_ranking.txt"
    sushi_count = 10

    num_users = int(input("How many data to generate? "))

    # load data
    users = load_user_features(user_file)
    sushis = load_sushi_features(sushi_file)
    
    if num_users > len(users):
        raise ValueError(f"Requested {num_users} users, but only {len(users)} available.")

    # randomly get some persona
    sampled_users = random.sample(users, num_users)

    # generate the data
    with open(output_txt, "w", encoding="utf-8") as out:
        for user in tqdm(sampled_users):
            prompt = build_prompt(user, sushis) 
            try:
                ranking = get_gpt_ranking(prompt)
                valid_ids = []
                for x in ranking.split():
                    if x.isdigit():
                        val = int(x)
                        if 0 <= val <= 9 and val not in valid_ids:
                            valid_ids.append(val)
                        if len(valid_ids) == 10:
                            break

                if len(valid_ids) != 10:
                    print(f"Invalid output (not exactly 10 IDs): {ranking}")
                    clean_ranking = "ERROR"
                else:
                    clean_ranking = ' '.join(map(str, valid_ids))

                out.write(clean_ranking + "\n")
  
            except Exception as e:
                print(f"Error for user {user[0]}: {e}")
                out.write("ERROR\n")

    print(f"\nSushi ranking saved to: {output_txt}")


if __name__ == "__main__":
    main()
