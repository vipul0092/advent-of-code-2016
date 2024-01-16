import sys
from collections import deque
from utils.reader import read_lines

grid = read_lines("input")
diffs, rows, cols, positions_to_num, lengths = [[-1, 0], [1, 0], [0, -1], [0, 1]], len(grid), len(grid[0]), {}, {}

for i in range(rows):
    for j in range(cols):
        if ord('0') <= ord(grid[i][j]) <= ord('9'):
            n = ord(grid[i][j]) - ord('0')
            positions_to_num[(i, j)] = n

for pos, num in positions_to_num.items():
    q, visited = deque(), set()
    q.append((pos, 0))
    visited.add(pos)
    lengths[num] = {}
    while len(q) != 0:
        (curpos, curlen) = q.popleft()
        if curpos in positions_to_num and curpos != pos:
            lengths[num][positions_to_num[curpos]] = curlen
        for diff in diffs:
            tmp = (curpos[0] + diff[0], curpos[1] + diff[1])
            if 0 <= tmp[0] < rows and 0 <= tmp[1] < cols and tmp not in visited and grid[tmp[0]][tmp[1]] != '#':
                q.append((tmp, curlen + 1))
                visited.add(tmp)
all_bits = (1 << len(positions_to_num.items())) - 1


def recurse(cur_pos, bits, come_back):
    if bits == all_bits:
        return lengths[cur_pos][0] if come_back else 0
    min_len = sys.maxsize
    for (nbor, nlen) in lengths[cur_pos].items():
        if bits & (1 << nbor) == 0:
            cur_len = nlen + recurse(nbor, bits | (1 << nbor), come_back)
            min_len = min(cur_len, min_len)
    return min_len


print('Part 1: ', recurse(0, 1, False))  # 490
print('Part 2: ', recurse(0, 1, True))  # 744

