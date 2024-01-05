from utils.reader import read_lines

lines = read_lines("input")

count = 0
numbers: list[list[int]] = []
for line in lines:
    parts = []
    for p in line.split(" "):
        if len(p) == 0:
            continue
        parts.append(int(p.strip()))
    numbers.append(parts.copy())
    parts.sort()
    if parts[0] + parts[1] > parts[2]:
        count += 1

print('Part 1: ', count)  # 869

count = 0
for j in range(0, 3):
    for i in range(0, len(numbers), 3):
        parts = [numbers[i][j], numbers[i+1][j], numbers[i+2][j]]
        parts.sort()
        if parts[0] + parts[1] > parts[2]:
            count += 1
print('Part 2: ', count)  # 1544
