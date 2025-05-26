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








