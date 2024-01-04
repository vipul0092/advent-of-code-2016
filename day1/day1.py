from utils.reader import read_lines


def solve():
    line = read_lines("day1/input")[0]
    operations = line.split(", ")
    current, direction, locations, repeat = (0, 0), (0, 0), set(), (0, 0)
    locations.add(current)

    for opr in operations:
        dis, dirr = int(opr[1:]), opr[0]
        if current == (0, 0):
            direction = (1, 0) if dirr == 'R' else (-1, 0)
        else:
            direction = (direction[1], -direction[0]) if dirr == 'R' else (-direction[1], direction[0])
        # print(direction)
        first = direction[0] != 0
        value = direction[0] * dis if first else direction[1] * dis
        temp = current
        for v in range(1, abs(value) + 1):
            v = -v if value < 0 else v
            temp = (current[0] + v if first else current[0], current[1] if first else current[1] + v)
            if temp in locations and repeat == (0, 0):
                repeat = temp
            locations.add(temp)
        # print(temp)
        current = temp

    print('Part 1: ', abs(current[0]) + abs(current[1]))  # 246
    print('Part 2: ', abs(repeat[0]) + abs(repeat[1]))  # 124
