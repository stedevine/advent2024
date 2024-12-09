from typing import Iterator, List, Callable
test = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def get_safe_count(readings: Iterator[int]) -> int:
    safe_count = 0
    print(type(readings))
    for reading in readings:
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

def is_safe_modified(reading: List[int]) -> List[int]:
    dropped = False
    x = []
    i = 0 
    j = 1
    if (reading[0] == reading[1]):
        i += 1
        j += 1
        dropped = True
        dropped_index = -1
    
    if (reading[1] < reading[0] and reading[1] < reading[2]):
        i = 0
        j = 2
    if (reading[1] > reading[0] and reading[1] > reading[2]):
        i = 0
        j = 2


    if (reading[i] - reading[j])  == 0:
        return False

    increasing = (reading[i] - reading[j]) > 0

    while j < len(reading):
        print(f"{i} {j} : {increasing} {reading[i]} - {reading[j]} = {reading[i] - reading[j]}")
        if not (is_valid(increasing, reading[i] - reading[j])):
            if dropped:
                return False
            dropped = True
            dropped_index = j
            if dropped_index == 1:
                increasing = not increasing
            j += 1
            continue
        #x.append(d)
        #c = reading[j]
        i += 1
        if (dropped and i == dropped_index):
            i += 1
        j += 1
    #print(f"{reading} {x}")
    return True

def is_valid(increasing: bool, difference:int) -> bool:
    if (increasing):
        return difference in [1,2,3] 
    return difference in [-1,-2,-3]

def get_modified_safe_count(readings: Iterator[int]) -> List[int]:
    modified_safe_count = 0
    for reading in readings:
        if (is_safe_modified(reading)):
            modified_safe_count += 1
        # print(f"read: {reading} {get_differentials(reading)}")
        # print(f"diff:   {get_differentials(reading)}")
    return modified_safe_count

lines = test.split('\n')
# Test
print(f"Test safe count 1:    {get_safe_count(get_readings(lines))}")
print(f"Test safe count 2:    {get_modified_safe_count(get_readings(lines))}")

input = []
with open('./2.txt') as f:
    input = f.readlines()


# Tests
def test(reading: List[int]) -> None:
    print(f"{reading} {is_safe_modified(reading)}")
"""
test([4,4,3,2,1])
test([4,4,4,2,1])
test([1,2,3,4,8,3])
test([1,2,3,4,8])
test([1,2,3,4,8,8])
test([1,2,3,4,8,7])
test([1,4,7,10,11,13])
"""
test([1,2,99,4,5,6])
test([1,2,4,5,6])
test([1,2,4,5,99,99])
test([1,2,4,5,99,5])
test([1,2,4,5,99,9])
test([-1,-2,-4,-5,99,-9])
test([1,-2,3,4])
test([-1,-2,3,-4])



#print(is_safe_modified([4,4,3,2,1]))

#print(f"Safe count:    {get_safe_count(get_readings(input))}")
#print(f"Safe count:    {get_modified_safe_count(get_readings(input))}")

