from collections import defaultdict
from utils.reader import read_lines

lines = read_lines("input")

code = ''
code2 = ''
for j in range(0, len(lines[0])):
    count = defaultdict(int)
    for line in lines:
        count[line[j]] += 1
    sorted_items = sorted(count.items(), key=lambda it: it[1], reverse=True)
    code += sorted_items[0][0]
    code2 += sorted_items[len(sorted_items)-1][0]

print('Part 1: ', code)  # umcvzsmw
print('Part 2: ', code2)  # rwqoacfz
