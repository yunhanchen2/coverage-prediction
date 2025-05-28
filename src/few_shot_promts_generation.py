import random

# reuse the one in 0_shot
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


    

def main():
    user_file = "sushi_u.txt"
    pref_file = "5000_a_prim.txt"

    # open the file
    with open(user_file, 'r', encoding='utf-8') as f1, open(pref_file, 'r', encoding='utf-8') as f2:
        user_lines = f1.readlines()
        sushi_lines = f2.readlines()

    # get the input of number of lines to pick
    n = int(input("How many lines to sample? ").strip())

    # select random index
    total_lines = len(user_lines)
    indices = list(range(total_lines))   
    selected_indices = sorted(random.sample(indices, n))  
    remaining_indices = [i for i in range(total_lines) if i not in selected_indices]

    #checking
    # print(f"Selected line indices: {selected_indices}")

    # write selected lines as prompts
    with open("prompt_persona.txt", "w") as prompt_out:
        for i in selected_indices:
            user_row = user_lines[i].strip().split('\t')
            sushi_ranking = sushi_lines[i].strip()
            description = user_to_text(user_row)
            prompt_out.write(f"{description} Ranks the sushi as: {sushi_ranking}\n")

    # generate 2 files
    with open("sushi_u_less.txt", "w") as f_user_less, open("5000_a_prim_less.txt", "w") as f_sushi_less:
        for i in remaining_indices:
            f_user_less.write(user_lines[i])
            f_sushi_less.write(sushi_lines[i])

if __name__ == "__main__":
    main()