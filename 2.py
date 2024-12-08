from typing import Iterator, List, Callable
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
        if reading[1] > reading[0]:
            if (error_count(reading, increasing_ok) == 0):
                safe_count += 1
        else:
            if (error_count(reading, decreasing_ok) == 0):
                safe_count += 1
    return safe_count

def increasing_ok(x: int, y:int) -> bool:
   return (y - x) > 0 and (y - x) < 4

def decreasing_ok(x: int, y:int) -> bool:
   return (x - y) > 0 and (x - y) < 4

def error_count(reading: List[int], valid: Callable):
    count = 0
    current = reading[0]
    for v in reading[1:]: 
        if valid(current,v):
            current = v
        else:
            count += 1
    if count > 0:
        print(f"Is {valid.__name__} {reading} {count}")
    return count


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