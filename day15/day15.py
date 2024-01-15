from utils.reader import read_lines

lines = read_lines("input")

discs = list()
for line in lines:
    pos = int(line.split(" positions")[0].split(" has ")[1])
    i_pos = int(line.split("at position ")[1].split(".")[0])
    discs.append((i_pos, pos))


def solve(add_additional_disc=False):
    current_sol = (-1, -1)
    if add_additional_disc:
        discs.append((0, 11))
    for i in range(len(discs)):
        initial_pos, positions = discs[i]
        if current_sol == (-1, -1):
            current_sol = (positions - initial_pos, positions)
        else:
            times = 0
            while True:
                current_time = current_sol[0] + (times * current_sol[1])
                if (current_time + initial_pos + 1) % positions == 0:
                    current_sol = (current_time + 1, positions * current_sol[1])
                    break
                times += 1
    return current_sol[0] - len(discs)


print('Part 1: ', solve())  # 376777
print('Part 2: ', solve(True))  # 3903937
