# coverage-prediction

## Problem Description

We are given $n$ sushi items: $\[n] = \{0, 1, 2, \dots, n - 1\}$  
Each user has a preference list: $l = (l_1, ..., l_m)$, where $l_i \in [n]$, and there will be $p$ items in each $l$.  
Our goal is to select a subset $S \subseteq [n]$, with $|S| \leq k$, to maximize the following objective:  

**Expected coverage over users:**

$$
\max_{S \subseteq [n],\ |S| \leq k} \ \mathbb{E}_{l} [ r(l, S) ]
$$

where  
$r(l, S) = 1$ if $\{l_1, ..., l_m\} \cap S \neq \emptyset$,  
and $r(l, S) = 0$ otherwise.

*(p.s. Here we use the data of `sushi_a`, which containing data id only from 0–9.)*

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

1. **0 shot LLM Generation (`gpt_persona_0_shot.py`)**

   - **Description:**
     This script is 0 shot LLM Generation. The basic idea is each time when LLM generates a line of ranking, it will first receive a random persona of examers and then receive prompts which include the sushi features and task discription. Here we use the gpt-4o and generate `50`, `100`, `500`, `1000` numbers of rankings. To encourage GPT to be more exploratory when generating data, we shuffle the sushi feature list before each generation and set the temperature to 1.05.

     **Input:** the number of sushi rankings to generate  
     **Output:** file called `sushi_ranking.txt` containing rankings, located in the same directory as `gpt_persona_0_shot.py`

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
     To set p, the terminal will prompt:
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
     To get value of p, the terminal will prompt:
     ```
     How many top-ranked items per user should be considered? (e.g., 3): 
     ```
     To get the optimal sushi ids:
     ```
     Enter the sushi IDs you want to serve (space-separated). Press Enter when done:
     ```
