import hashlib
import queue

from utils.reader import read_lines

passcode = read_lines("input")[0]
diffs = [[-1, 0, 'U'], [1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R']]


def get_neighbors(pos, move_string: str) -> dict:
    md5 = hashlib.md5((passcode + move_string).encode('utf-8')).hexdigest()
    nbors = dict()
    for i in range(len(diffs)):
        tp = (diffs[i][0] + pos[0], diffs[i][1] + pos[1])
        if 0 <= tp[0] < 4 and 0 <= tp[1] < 4 and ord('b') <= ord(md5[i]) <= ord('f'):
            nbors[tp] = diffs[i][2]
    return nbors


start, end, part1, longest = (0, 0), (3, 3), '', -1
q = queue.Queue()
q.put_nowait((start, ''))

while not q.empty():
    (curr, move_str) = q.get_nowait()
    if curr == end:
        if part1 == '':
            part1 = move_str
        longest = max(longest, len(move_str))
        continue
    for nbor in get_neighbors(curr, move_str).items():
        q.put_nowait((nbor[0], move_str + nbor[1]))


print('Part 1: ', part1)  # DUDDRLRRRD
print('Part 2: ', longest)  # 578




