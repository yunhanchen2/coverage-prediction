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
    # maps
    age_map = {
        "0": "15–19", "1": "20–29", "2": "30–39",
        "3": "40–49", "4": "50–59", "5": "60+"
    }

    prefecture_map = {
        "0": "Hokkaido", "1": "Aomori", "2": "Iwate", "3": "Akita", "4": "Miyagi", "5": "Yamagata",
        "6": "Fukushima", "7": "Niigata", "8": "Ibaraki", "9": "Tochigi", "10": "Gunma", "11": "Saitama",
        "12": "Chiba", "13": "Tokyo", "14": "Kanagawa", "15": "Yamanashi", "16": "Shizuoka", "17": "Nagano",
        "18": "Aichi", "19": "Gifu", "20": "Toyama", "21": "Ishikawa", "22": "Fukui", "23": "Shiga",
        "24": "Mie", "25": "Kyoto", "26": "Osaka", "27": "Nara", "28": "Wakayama", "29": "Hyogo",
        "30": "Okayama", "31": "Hiroshima", "32": "Tottori", "33": "Shimane", "34": "Yamaguchi",
        "35": "Ehime", "36": "Kagawa", "37": "Tokushima", "38": "Kochi", "39": "Fukuoka",
        "40": "Nagasaki", "41": "Saga", "42": "Kumamoto", "43": "Kagoshima", "44": "Miyazaki",
        "45": "Oita", "46": "Okinawa", "47": "foreign countries"
    }

    region_map = {
        "0": "Hokkaido", "1": "Tohoku", "2": "Hokuriku", "3": "Kanto and Shizuoka",
        "4": "Nagano and Yamanashi", "5": "Chukyo", "6": "Kinki", "7": "Chugoku",
        "8": "Shikoku", "9": "Kyushu", "10": "Okinawa", "11": "Foreign"
    }

    eastwest_map = {"0": "Eastern Japan", "1": "Western Japan"}

    uid = user[0]
    gender = "male" if user[1] == "0" else "female"
    age = age_map.get(user[2], "invalid age")

    childhood_pref = prefecture_map.get(user[4], f"Prefecture {user[4]}")
    childhood_region = region_map.get(user[5], f"Region {user[5]}")
    childhood_side = eastwest_map.get(user[6], f"Area {user[6]}")

    current_pref = prefecture_map.get(user[7], f"Prefecture {user[7]}")
    current_region = region_map.get(user[8], f"Region {user[8]}")
    current_side = eastwest_map.get(user[9], f"Area {user[9]}")

    if user[10] == "0":
        return (
            f"User {uid} is a {gender} aged {age}. "
            f"They have spent most of their life in {current_pref} ({current_region}, {current_side})."
        )
    else:
        return (
            f"User {uid} is a {gender} aged {age}. "
            f"They grew up in {childhood_pref} ({childhood_region}, {childhood_side}), "
            f"but currently live in {current_pref} ({current_region}, {current_side})."
        )

def sushi_to_text(sushi):
    style = "a maki roll" if sushi[2] == "0" else "a non-maki type"
    major = "seafood" if sushi[3] == "0" else "non-seafood"
    minor = minor_group_map.get(sushi[4], "unknown group")

    taste_score = float(sushi[5])
    if taste_score <= 0.8:
        taste = "very heavy in taste"
    elif taste_score <= 1.6:
        taste = "heavy in taste"
    elif taste_score <= 2.4:
        taste = "moderate in taste"
    elif taste_score <= 3.2:
        taste = "light in taste"
    else:
        taste = "very light in taste"

    freq_score = float(sushi[6])
    if freq_score <= 0.5:
        freq = "rarely eaten"
    elif freq_score <= 1.5:
        freq = "sometimes eaten"
    elif freq_score <= 2.5:
        freq = "often eaten"
    else:
        freq = "very frequently eaten"

    price = float(sushi[7])

    availability = float(sushi[8])

    if availability < 0.25:
        availability_text = "very rarely found in sushi restaurants"
    elif availability < 0.5:
        availability_text = "occasionally found in sushi restaurants"
    elif availability < 0.75:
        availability_text = "commonly found in sushi restaurants"
    else:
        availability_text = "very commonly found in sushi restaurants"

    return (
        f"{sushi[1]} (ID {sushi[0]}) is {style} from the {minor} group, belonging to the {major} category. "
        f"It is {taste}, {freq}, {availability_text}, and has a price score of {price:.2f}."
    )
   
# make prompts and call GPT
def build_prompt(user_row, sushi_rows):
    user_text = user_to_text(user_row)

    sushi_rows = sushi_rows.copy()
    random.shuffle(sushi_rows)

    sushi_info = "\n".join([sushi_to_text(s) for s in sushi_rows])
    
    prompt = f"""
We already know some of the rankings correspond to personas:
User 8295 is a female aged 20–29. They have spent most of their life in Aichi (Chukyo, Eastern Japan). Ranks the sushi as: 5 2 7 8 0 3 6 9 4 1
User 5585 is a male aged 30–39. They have spent most of their life in Shizuoka (Kanto and Shizuoka, Eastern Japan). Ranks the sushi as: 7 2 3 0 5 4 8 1 6 9
User 5091 is a male aged 20–29. They have spent most of their life in Mie (Chukyo, Eastern Japan). Ranks the sushi as: 5 0 7 2 3 6 8 9 1 4
User 1631 is a male aged 40–49. They have spent most of their life in Tokyo (Kanto and Shizuoka, Eastern Japan). Ranks the sushi as: 4 5 7 1 2 3 8 6 9 0
User 1978 is a female aged 30–39. They have spent most of their life in Osaka (Kinki, Western Japan). Ranks the sushi as: 0 3 6 5 2 9 1 8 7 4

User profile:
{user_text}

Sushi items:
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
    user_file = "sushi_u_5_shot.txt"
    sushi_file = "sushi_i_a.txt"
    output_txt = "sushi_ranking_5_shot.txt"
    sushi_count = 10

    num_users = int(input("How many data to generate? "))

    # load data
    users = load_user_features(user_file)
    sushis = load_sushi_features(sushi_file)

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

    manual_rankings = [
    "5 2 7 8 0 3 6 9 4 1",
    "7 2 3 0 5 4 8 1 6 9",
    "5 0 7 2 3 6 8 9 1 4",
    "4 5 7 1 2 3 8 6 9 0",
    "0 3 6 5 2 9 1 8 7 4"
    ]

    with open(output_txt, "a", encoding="utf-8") as out:
        for line in manual_rankings:
            out.write(line + "\n")

    print(f"\nSushi ranking saved to: {output_txt}")

if __name__ == "__main__":
    main()