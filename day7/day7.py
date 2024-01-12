from utils.reader import read_lines

lines = read_lines("input")

count = 0
for line in lines:
    bracket_start = False
    correct = False
    for i in range(3, len(line)):
        if line[i] == '[':
            bracket_start = True
        elif line[i] == ']':
            bracket_start = False
        if line[i-1] == line[i-2] and line[i] == line[i-3] and line[i] != line[i-1]:
            if not bracket_start:
                correct = True
            elif bracket_start:
                correct = False
                break
    if correct:
        count += 1

print('Part 1: ', count)  # 118

count2 = 0
for line in lines:
    aba_set = set()
    bab_set: list[int] = []
    bracket_start = False
    for i in range(2, len(line)):
        if line[i] == '[':
            bracket_start = True
        elif line[i] == ']':
            bracket_start = False
        if line[i] == line[i-2] and line[i-1] != '[' and line[i-1] != ']':
            if bracket_start:
                code = ((ord(line[i]) - ord('a')) * 26) + (ord(line[i-1]) - ord('a'))
                bab_set.append(code)
            else:
                code = ((ord(line[i-1]) - ord('a')) * 26) + (ord(line[i]) - ord('a'))
                aba_set.add(code)

    for bab in bab_set:
        if bab in aba_set:
            count2 += 1
            break

print('Part 2: ', count2)  # 260

