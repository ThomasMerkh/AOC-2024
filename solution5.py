from collections import defaultdict

# part one
switchparser = False
graph = defaultdict(set)
updates = []
with open('input5.txt', 'r') as f:
    for line in f:
        if line == "\n":
            switchparser = True
        elif not switchparser:
            line = [int(n) for n in line.strip("\n").split("|")]
            graph[line[0]].add(line[1])
        else:
            updates.append([int(n) for n in line.strip("\n").split(",")])
        
def valid(update):
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if update[i] in graph[update[j]]:
                return False
    return True


total_sum = 0
incorrects = []
for update in updates:
    if valid(update):
        total_sum += update[len(update)//2]
    else:
        incorrects.append(update)
print(total_sum)

# part two
def sort_update(update) -> int:
    i = 0
    while i < len(update)-1:
        j = i+1
        while j < len(update):
            if update[i] in graph[update[j]]:
                update[i], update[j] = update[j], update[i]
            else:
                j += 1
        i += 1
    return update[len(update)//2]

total_incorrect_sum = 0
for incorrect in incorrects:
    total_incorrect_sum += sort_update(incorrect)
print(total_incorrect_sum)
