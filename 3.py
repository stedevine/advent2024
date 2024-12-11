def multiply_alt(input:str, do_dont:bool) -> int:
    result = 0 
    i = 0
    in_mul_block = False
    enabled = True
    digits = {}
    digit_offset = 0
    while i < len(input):
        if enabled and not in_mul_block:
            if input[i:i+4] == "mul(":
                in_mul_block = True
                i += 4
                digits = {0 : [], 1: []}
                digit_offset = 0
                continue
        
        if in_mul_block:
            if input[i].isdigit():
                digits[digit_offset].append(input[i])
                i += 1
                continue
            elif input[i] == ",":
                digit_offset = 1
                i += 1
                continue

            elif input[i] == ")":
                l = int("".join(digits[0]))
                r = int("".join(digits[1]))
                result += l * r
                in_mul_block = False
                i += 1
                continue
            else:
                in_mul_block = False
                i += 1
                continue

        if do_dont:
            if enabled and input[i:i+7] == "don't()":
                enabled = False
                i += 7
                continue            
            
            if not enabled and input[i:i+4] == "do()":
                enabled = True
                i += 4
                continue

        i += 1


    return result

def multiply(input:str) -> int:
    #print(input)
    result = 0
    # find mul block
    mul_blocks = input.split("mul(")[1:]
    for mul_block in mul_blocks:
        #print(mul_block)
        mul_block = list(mul_block)
        digits = {0 : [], 1: []}
        offset = 0
        #valid = True 
        
        while mul_block:
            c = mul_block.pop(0)
            if c.isdigit():
                digits[offset].append(c)
            
            elif c == ',':
                if offset == 0:
                    offset += 1
                else:
                    continue
            
            elif c == ')':
                if offset == 1 and len(digits[1]) > 0:

                    #print(digits)
                    l = int("".join(digits[0]))
                    r = int("".join(digits[1]))
                    if l == 521:
                        print(mul_block)
                        print(f"{l}*{r}")
                    result += l * r
                    break
            else:
                break

    return result

test = "mxul(2,2)xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('./3.txt') as f:
    input = f.readlines()
    input = "".join(input)

print(" ")
print(f"Test - Part 1   : {multiply_alt(test, False)}")
print(f"Part 1          : {multiply_alt(input, False)}")
# 161289189
print(f"Test - Part 2   : {multiply_alt(test_2, True)}")
print(f"Part 2          : {multiply_alt(input, True)}")
