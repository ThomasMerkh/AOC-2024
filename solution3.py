import re

# part one
with open('input3.txt', 'r') as f:
    input = f.readline()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input)
    print(sum([int(a)*int(b) for a, b in matches]))

# part two
with open('input3.txt', 'r') as f:
    input = f.readline()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    matches = re.finditer(pattern, input)
    
    enabled = True
    total_sum = 0
    for match in matches:
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        else:
            if enabled:
                num1, num2 = map(int, match.groups())
                total_sum += num1 * num2
print(total_sum)
