# coverage-prediction

## Problem Description
We are given n sushi items: `[n] = {0, 1, 2, ..., n−1}`   
Each user has a preference list: `l = (l₁, ..., lₘ), where lᵢ ∈ [n] `, and there will be `p` items in `lᵢ`.   
Our goal is to select a subset `S ⊆ [n]`, with `|S| ≤ k`, to maximize the following objective:    
Expected coverage over users: max_{S ⊆ [n], |S| ≤ k}  E_{l ~ L} [ r(l, S) ]



