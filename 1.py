from typing import List, Tuple
from collections import defaultdict
def get_lists(lines: List[str]) -> Tuple[List[int], List[int]]:
    x = []
    y = []
    for line in lines:
        tokens = line.split("   ")
        if len(tokens)> 1:
            x.append(int(tokens[0]))
            y.append(int(tokens[1]))

    return (x,y)

def get_distance(x: List[int], y: List[int]) -> int:
    x.sort()
    y.sort()   
    score = 0
    assert len(x) == len(y)
    while (len(x) > 0):
        score += abs(x.pop() - y.pop()) 
    return score

def get_similarity_score(x: List[int], y: List[int]) -> int:
    score = 0
    # map the values in y as value -> count of value
    value_count = defaultdict(int)
    for n in y:
        value_count[n] += 1
    for n in x:
        score += n * value_count[n]
    return score
    

test = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
lines = test.split('\n')
# Test
print(f"Test distance score:    {get_distance(*get_lists(lines))}")
print(f"Test similarity score:  {get_similarity_score(*get_lists(lines))}")

input = []
with open('./1.txt') as f:
    input = f.readlines()

print(f"Distance score:    {get_distance(*get_lists(input))}")
print(f"Similarity score:  {get_similarity_score(*get_lists(input))}")
