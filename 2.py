from typing import Iterator, List
test = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def get_safe_count(lines: List[str]) -> int:
    safe_count = 0
    for reading in get_readings(lines):
        if reading[0] == reading[1]:
            continue
        if reading[1] > reading[0] and is_increasing(reading):
            safe_count += 1
        else:
            if is_decreasing(reading):
                safe_count += 1
    return safe_count

def is_increasing(reading: List[int]):
    result = True
    current = reading[0]
    for v in reading[1:]: 
        if (v - current) > 0 and (v - current) < 4:
            current = v
        else:
            result = False
            break
    print(f"Is Increasing {reading} {result}")
    return result

def is_decreasing(reading: List[int]):
    result = True
    current = reading[0]
    for v in reading[1:]: 
        if (current - v) > 0 and (current - v) < 4:
            current = v
        else:
            result = False
            break
    print(f"Is Decreasing {reading} {result}")
    return result

def get_readings(lines:str) -> Iterator[int]:
    for line in lines:
        tokens = line.split(' ')
        if len(tokens) > 1:
            tokens = [int(x) for x in tokens]
            assert len(tokens) > 2
            yield tokens



lines = test.split('\n')
# Test
print(f"Test safe count:    {get_safe_count(lines)}")

input = []
with open('./2.txt') as f:
    input = f.readlines()

print(f"Safe count:    {get_safe_count(input)}")