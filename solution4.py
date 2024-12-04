# part one
xmas_count = 0
word_search = []
with open('input4.txt', 'r') as f:
    for line in f:
        word_search.append(list(line.strip("\n")))

n, m = len(word_search), len(word_search[0])
directions = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1),
]
def check_valid(i, j):
    return 0 <= i < n and 0 <= j < m

mapping = {0: "M", 1: "A", 2: "S"}
def search_all_directions(i, j) -> int:
    counts = 0
    for di, dj in directions:
        I = i
        J = j
        for indx in range(3):
            I += di
            J += dj
            if not (check_valid(I, J) and word_search[I][J] == mapping[indx]):
                break
            if indx == 2:
                counts += 1
    return counts

for i in range(n):
    for j in range(m):
        if word_search[i][j] == "X":
            xmas_count += search_all_directions(i, j)
print(xmas_count)



# part two
XMAS_mappings = [
    {(-1, -1): "M", (1, -1): "M", (-1, 1): "S", (1, 1): "S"},
    {(-1, -1): "S", (1, -1): "M", (-1, 1): "S", (1, 1): "M"},
    {(-1, -1): "M", (1, -1): "S", (-1, 1): "M", (1, 1): "S"},
    {(-1, -1): "S", (1, -1): "S", (-1, 1): "M", (1, 1): "M"},
]

x_mas_count = 0

def search_xs(i, j) -> int:
    counts = 0
    for XMAS_mapping in XMAS_mappings:
        for idx, (di, dj) in enumerate(XMAS_mapping):
            I = i+di
            J = j+dj
            if not (check_valid(I, J) and word_search[I][J] == XMAS_mapping[(di,dj)]):
                break
            if idx == 3:
                counts += 1
    return counts

# Need to check in every direction.
for i in range(n):
    for j in range(m):
        if word_search[i][j] == "A":
            x_mas_count += search_xs(i, j)
print(x_mas_count)
# 470 too low