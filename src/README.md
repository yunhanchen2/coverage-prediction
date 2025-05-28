# coverage-prediction

## Code Files Description

### Data Generation

1. **Random Data Generation (`random_ranking.py`)**

   - **Description:**  
     This script is the baseline for sushi ranking generation. It randomly generates a specified number of sushi rankings.

     **Input:** the number of sushi rankings to generate  
     **Output:** file called `random_sushi_rankings.txt` containing rankings, located in the same directory as `random_ranking.py`

   - **Running Instruction:**  
     Run the script using:
     ```
     python3 random_ranking.py
     ```
     After executing, the terminal will prompt:
     ```
     How many sushi rankings do you want to generate?
     ```
     You can input a number like `50`, `100`, `500`, `1000`, etc.

2. **0 shot LLM Generation (`gpt_persona_0_shot.py`)**

   - **Description:**
     This script is 0 shot LLM Generation. The basic idea is each time when LLM generates a line of ranking, it will first receive a random persona of examers and then receive prompts which include the sushi features and task discription. Here we use the gpt-4o and generate `50`, `100`, `500`, `1000` numbers of rankings. To encourage GPT to be more exploratory when generating data, we shuffle the sushi feature list before each generation and set the temperature to 1.05.

     **Input:** the number of sushi rankings to generate  
     **Output:** file called `sushi_ranking.txt` containing rankings, located in the same directory as `gpt_persona_0_shot.py`

     An example of 0-shot prompt:
     ```
     User profile:
     User 1234 is a female aged 20–29. They have spent most of their life in Tokyo (Kanto and Shizuoka, Eastern Japan).

     Sushi items:
     ebi (ID 0) is a non-maki type from the shrimp or crab group, belonging to the seafood category. It is light in taste, very frequently eaten, very commonly found in sushi restaurants, and has a price score of 1.84.
     anago (ID 1) is a non-maki type from the tare (eel sauce) group, belonging to the seafood category. It is heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.99.
     maguro (ID 2) is a non-maki type from the akami (red meat fish) group, belonging to the seafood category. It is moderate in taste, very frequently eaten, very commonly found in sushi restaurants, and has a price score of 1.87.
     ika (ID 3) is a non-maki type from the squid or octopus group, belonging to the seafood category. It is light in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.52.
     uni (ID 4) is a non-maki type from the other seafood group, belonging to the seafood category. It is heavy in taste, sometimes eaten, very commonly found in sushi restaurants, and has a price score of 3.29.
     ikura (ID 5) is a non-maki type from the roe group, belonging to the seafood category. It is heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 2.70.
     tamago (ID 6) is a non-maki type from the egg group, belonging to the non-seafood category. It is moderate in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.03.
     toro (ID 7) is a non-maki type from the akami (red meat fish) group, belonging to the seafood category. It is very heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 4.49.
     tekka_maki (ID 8) is a maki roll from the akami (red meat fish) group, belonging to the seafood category. It is moderate in taste, often eaten, occasionally found in sushi restaurants, and has a price score of 1.58.
     kappa_maki (ID 9) is a maki roll from the vegetable group, belonging to the non-seafood category. It is very light in taste, sometimes eaten, occasionally found in sushi restaurants, and has a price score of 1.02.

     Please simulate a sushi ranking this person would produce.
     Please avoid always ranking the same item first across people.
     Return exactly 10 unique integers from 0 to 9, in order of preference, like:
     3 1 7 2 5 0 8 9 4 6
     ```

   - **Running Instruction:**
      First get your OpenAI api:
     ```
     export OPENAI_API_KEY=sk-xxxxx...  (your api)
     ```
      Run the script using:
     ```
     python3 gpt_persona_5_shot.py
     ```
     After executing, the terminal will prompt:
     ```
     How many data to generate?
     ```
     You can input a number like `50`, `100`, `500`, `1000`, etc.

3. **5 shot LLM Generation (`gpt_persona_5_shot.py`)**

   - **Description:**
     This script is 5 shot LLM Generation, which is very similar to 0 shot but will show additional 5 examples of rankings corresponding to persona. Here we use the gpt-4o and generate `50`, `100`, `500`, `1000` numbers of rankings. To encourage GPT to be more exploratory when generating data, we shuffle the sushi feature list before each generation and set the temperature to 1.05.

     **Input:** the number of sushi rankings to generate  
     **Output:** file called `sushi_ranking.txt` containing rankings, located in the same directory as `gpt_persona_0_shot.py`

     An example of 0-shot prompt:
     ```
     First, here is the background:
Generally speaking, the eastern Japanese prefers more oily and more heavily seasoned food than the western Japanese.
The western prefers to UDON noodle, while the eastern loves SOBA noodle.
The way of cooking Kabayaki, grilled eels, is clearly different.

The other preference patterns depending on regions are:
- The SUSHI in Tokyo is specially called Edomaezushi. The typical examples of the Edomae are: anago (ID:1), zuke (ID:76), and kohada (ID:23).
- A nattou (fermented bean) is loved in the Ibaraki prefecture, but is hated in the Kinki region.
- An oceanic bonito is frequently eaten in the Kochi prefecture.
- A mentaiko (chili cod roe) is a noted product in the Fukuoka prefecture.
- A karasumi (dried mullet roe) is a noted product in the Nagasaki prefecture.
- A batttera sushi is mainly eaten in the Kinki region.
     
     We already know some of the rankings correspond to personas:
     User 8295 is a female aged 20–29. They have spent most of their life in Aichi (Chukyo, Eastern Japan). Ranks the sushi as: 5 2 7 8 0 3 6 9 4 1
     User 5585 is a male aged 30–39. They have spent most of their life in Shizuoka (Kanto and Shizuoka, Eastern Japan). Ranks the sushi as: 7 2 3 0 5 4 8 1 6 9
     User 5091 is a male aged 20–29. They have spent most of their life in Mie (Chukyo, Eastern Japan). Ranks the sushi as: 5 0 7 2 3 6 8 9 1 4
     User 1631 is a male aged 40–49. They have spent most of their life in Tokyo (Kanto and Shizuoka, Eastern Japan). Ranks the sushi as: 4 5 7 1 2 3 8 6 9 0
     User 1978 is a female aged 30–39. They have spent most of their life in Osaka (Kinki, Western Japan). Ranks the sushi as: 0 3 6 5 2 9 1 8 7 4
     
     User profile:
     User 1234 is a female aged 20–29. They have spent most of their life in Tokyo (Kanto and Shizuoka, Eastern Japan).

     Sushi items:
     ebi (ID 0) is a non-maki type from the shrimp or crab group, belonging to the seafood category. It is light in taste, very frequently eaten, very commonly found in sushi restaurants, and has a price score of 1.84.
     anago (ID 1) is a non-maki type from the tare (eel sauce) group, belonging to the seafood category. It is heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.99.
     maguro (ID 2) is a non-maki type from the akami (red meat fish) group, belonging to the seafood category. It is moderate in taste, very frequently eaten, very commonly found in sushi restaurants, and has a price score of 1.87.
     ika (ID 3) is a non-maki type from the squid or octopus group, belonging to the seafood category. It is light in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.52.
     uni (ID 4) is a non-maki type from the other seafood group, belonging to the seafood category. It is heavy in taste, sometimes eaten, very commonly found in sushi restaurants, and has a price score of 3.29.
     ikura (ID 5) is a non-maki type from the roe group, belonging to the seafood category. It is heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 2.70.
     tamago (ID 6) is a non-maki type from the egg group, belonging to the non-seafood category. It is moderate in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.03.
     toro (ID 7) is a non-maki type from the akami (red meat fish) group, belonging to the seafood category. It is very heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 4.49.
     tekka_maki (ID 8) is a maki roll from the akami (red meat fish) group, belonging to the seafood category. It is moderate in taste, often eaten, occasionally found in sushi restaurants, and has a price score of 1.58.
     kappa_maki (ID 9) is a maki roll from the vegetable group, belonging to the non-seafood category. It is very light in taste, sometimes eaten, occasionally found in sushi restaurants, and has a price score of 1.02.

     Please simulate a sushi ranking this person would produce.
     Please avoid always ranking the same item first across people.
     Return exactly 10 unique integers from 0 to 9, in order of preference, like:
     3 1 7 2 5 0 8 9 4 6
     ```

   - **Running Instruction:**
      First get your OpenAI api:
     ```
     export OPENAI_API_KEY=sk-xxxxx...  (your api)
     ```
      Run the script using:
     ```
     python3 gpt_persona_0_shot.py
     ```
     After executing, the terminal will prompt:
     ```
     How many data to generate?
     ```
     You can input a number like `50`, `100`, `500`, `1000`, etc.

4. **Random Primary Data Generation (`random_prim.py`)**

   - **Description:**  
     This code randomly selects a specified number of sushi rankings from primary datas.

     **Input:** the number of sushi rankings to select  
     **Output:** file called `random_prim.txt` containing rankings, located in the same directory as `random_prim.py`

   - **Running Instruction:**  
     Run the script using:
     ```
     python3 random_prim.py
     ```
     After executing, the terminal will prompt:
     ```
     How many lines do you want to randomly pick?
     ```
     You can input a number like `50`, `100`, `500`, `1000`, etc.

5. **Few Shot Prompts Generation Helper (`few_shot_prompts_generation.py`)**

   - **Description:**  
     This code generates a specific number of examples in prompts.

     **Input:** the number of examples  
     **Output:** file called `prompt_persona.txt`

   - **Running Instruction:**  
     Run the script using:
     ```
     python3 few_shot_prompts_generation.py
     ```
     After executing, the terminal will prompt:
     ```
     How many lines to sample?
     ```
     You can input a number like `5`, `7`, `10`, etc.


### Bias Checking

1. **Get Optimal Solution and Coverage Rate(`get_max.py`)**

   - **Description:**  
     This code selects *k* sushi items to serve customers in order to maximize overall utility.  It uses a **brute-force algorithm** to search all possible combinations. However, when the number of sushi types is large, a **greedy algorithm** is a more efficient way.  

     **Input:** a filename containing sushi ranking data  
     **Output:** the optimal solution (*k* sushi IDs) and the corresponding coverage rate


   - **Running Instruction:**
     Run the script using:
     ```
     python3 get_max.py
     ```
     After executing, the terminal will prompt:
     ```
     Please input the filename:
     ```
     You can type the txt file name.   
     To set m, the terminal will prompt:
     ```
     How many top preferred categories will be picked? (e.g., 3):
     ```
     To set k, the terminal will prompt:
     ```
     How many sushi do you want to pick to serve customers? (e.g., 5):
     ```
     To get how many types of sushi will be ranked, the terminal will prompt:
     ```
     How many total sushi types are there? (e.g., 100):
     ```
2. **Get the Coverage Rate Over Primary Data(`cal_bias.py`)**
   
   - **Description:**
     This code is for getting the coverage rate of all primary datas.

     **Input:** optimal sushi ids
     **Output:** the corresponding coverage rate

   - **Running Instruction:**
     Run the script using:
     ```
     python3 cal_bias.py
     ```
     To get value of m, the terminal will prompt:
     ```
     How many top-ranked items per user should be considered? (e.g., 3): 
     ```
     To get the optimal sushi ids:
     ```
     Enter the sushi IDs you want to serve (space-separated). Press Enter when done:
     ```
### Bias Elimination

1. 
