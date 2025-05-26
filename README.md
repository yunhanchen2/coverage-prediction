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
     This script is the baseline for sushi ranking generation. It randomly generates a specified number of sushi rankings and stores the result in a file called `random_sushi_rankings.txt`, located in the same directory as `random_ranking.py`.

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
     This script is 0 shot LLM Generation. The basic idea is each time when LLM generates a line of ranking, it will first receive a random persona of examers and then receive prompts which include the sushi features and task discription. Here we use the gpt-4o and generate `50`, `100`, `500`, `1000` numbers of rankings, and the result will be stored in a file called `sushi_ranking.txt` located in the same directory as `random_ranking.py`.

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
     This code is to find k sushi id to serve customers and max their utility. Here we use the brute-force algorithm. However, if the sushi types are too many, greedy algorithm is a better way.




