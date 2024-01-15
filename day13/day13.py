import queue
import sys

from utils.reader import read_lines

diffs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
grid = dict()


def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def is_wall(pos) -> bool:
    if pos not in grid:
        x, y = pos
        bits = countSetBits(((x*x) + (3*x) + (2*x*y) + (y*y) + y) + number)
        grid[pos] = bits % 2 == 1
    return grid[pos]


def get_neighbors(pos: (int, int), visited: set):
    nbors = list()
    for d in diffs:
        tpos = (d[0] + pos[0], d[1] + pos[1])
        if tpos[0] >= 0 and tpos[1] >= 0 and tpos not in visited and not is_wall(tpos):
            nbors.append(tpos)
    return nbors


def bfs(start, end, max_steps=sys.maxsize) -> (int, int):
    steps = 0
    q, visited = queue.Queue(), set()
    q.put_nowait((start, 0))
    visited.add(start)

    while not q.empty():
        curr, cursteps = q.get_nowait()
        if cursteps + 1 > max_steps:
            continue
        if curr == end:
            steps = cursteps
            break

        for nbor in get_neighbors(curr, visited):
            q.put_nowait((nbor, cursteps+1))
            visited.add(nbor)
    return steps, len(visited)


number, pend = int(read_lines("input")[0]), (31, 39)
print('Part 1: ', bfs((1, 1), pend)[0])  # 90
print('Part 2: ', bfs((1, 1), pend, 50)[1])  # 135
