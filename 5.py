import math
test = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def parse_input(data):
    after = {}
    before = {}
    updates = []
    get_rules = True
    for line in data.split("\n"):
        if line == "":
            get_rules = False
            continue
        
        if get_rules:
            k,v = line.split("|")
            k = int(k)
            v = int(v)
            if k not in after:
                after[k] = set()
            after[k].add(v)
            if v not in before:
                before[v] = set()
            before[v].add(k)     
        else:
            updates.append(line)

    return after,before, updates
    
def get_mid(test):
    valid_updates = []
    after, before, updates = parse_input(test)
    for update in updates:
        tokens = [int(t) for t in update.split(',')]
        valid = True
        candidate_index = 0 
        while candidate_index < len(tokens) and valid:
            # Check the value after the candidate            
            for f in range(candidate_index+1, len(tokens)):
                #print(f"candidate {tokens[candidate_index]} checking: {tokens[f]}: {before.get(tokens[f])} contains {tokens[candidate_index]}")
                if before.get(tokens[f],False) and tokens[candidate_index] not in before[tokens[f]]:
                    valid = False
            # Check the value before the candidate
            for b in range(candidate_index-1, -1,-1):
                #print(f"candidate {tokens[candidate_index]} checking: {tokens[b]}: {after.get(tokens[b])} contains {tokens[candidate_index]}")
                if after.get(tokens[b], False) and tokens[candidate_index] not in after[tokens[b]]:
                    valid = False
            candidate_index += 1
        if valid:
            valid_updates.append(tokens)        
        #print(f"{tokens} {valid}")
    result = 0
    for valid_update in valid_updates:
        mid_index = math.floor(len(valid_update)/2)
        result += valid_update[mid_index]

    return result

with open('./5.txt') as f:
    input = f.read()

print(get_mid(test))
print(get_mid(input))