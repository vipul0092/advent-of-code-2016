import copy
import queue
import random
import sys
import time

from utils.reader import read_lines

lines = read_lines("input")
steps = sys.maxsize
states = dict()


def check_safe(pos):
    safe = True
    floors = [[0] * 2 for _ in range(r)]
    for i in range(len(pos)):
        c_f, g_f = pos[i][0], pos[i][1]
        floors[c_f - 1][0] |= 1 << i
        floors[g_f - 1][1] |= 1 << i

    for i in range(r):
        cv, gv = floors[i][0], floors[i][1]
        if floors[i][0] == 0 or floors[i][1] == 0:
            continue
        if ((cv ^ gv) & cv) != 0:
            safe = False
            break
    return safe


initial_pos = [[1, 2], [1, 3]]
initial_pos1 = [[1, 1], [1, 1], [3, 2], [2, 2], [2, 2]]
initial_pos2 = [[1, 1], [1, 1], [3, 2], [2, 2], [2, 2], [1, 1], [1, 1]]
r, p, m, bits, final_hash = 4, -1, -1, [], -1  # m varies according to the number of variables (X) -> 1 + 2X


def game_hash(pos: list[list[int]], floor):
    h = bits[floor - 1][0]  # elevator position
    for i in range(len(pos)):
        chip_floor, gen_floor = pos[i][0], pos[i][1]  # floor location of chip i and gen i
        h ^= bits[chip_floor - 1][i + 1]
        h ^= bits[gen_floor - 1][i + p + 1]
    return h


def move_item_hash(h, tf, ff, item, is_chip) -> int:
    h ^= bits[ff - 1][item + 1 if is_chip else item + p + 1]
    h ^= bits[tf - 1][item + 1 if is_chip else item + p + 1]
    return h


def move_elevator_hash(h, tf, ff) -> int:
    h ^= bits[tf - 1][0]
    h ^= bits[ff - 1][0]
    return h


def get_final_hash():
    _state = [[4] * 2 for _ in range(p)]
    return game_hash(_state, 4)


def getAnswer(init_pos: list[list[int]], floor, part):
    global p, m, bits, final_hash
    p = len(init_pos)
    m = 1 + (2 * p)
    bits = [[0] * m for _ in range(r)]

    # For Zobrist hashing - https://en.wikipedia.org/wiki/Zobrist_hashing
    rand = random.Random()
    for a in range(r):
        for b in range(m):
            bits[a][b] = rand.randint(0, 9999999999999999999999999999)
    final_hash = get_final_hash()

    q = queue.Queue()
    init_hash = game_hash(init_pos, floor)
    q.put_nowait((init_pos, floor, 0))
    visited = set()
    visited.add(init_hash)

    min_val = sys.maxsize
    it = 0
    while not q.empty():
        it += 1
        (pos, self, curlen) = q.get_nowait()
        curhash = game_hash(pos, self)
        # if it % 100_000 == 0:
        #     print('iter: ', it)
        if curhash == final_hash:
            print(pos, curlen, self, len(visited))
            min_val = min(curlen, min_val)
            continue
        items = list()
        for i in range(len(pos)):
            if pos[i][0] == self:
                items.append((i, 0))
            if pos[i][1] == self:
                items.append((i, 1))

        for i in range(len(items)):
            (cg1, tp1) = items[i]
            if self > 1:
                pos[cg1][tp1] = self - 1
                h = move_item_hash(curhash, self - 1, self, cg1, tp1 == 0)
                h = move_elevator_hash(h, self - 1, self)
                if h not in visited and check_safe(pos) and curlen < min_val:
                    q.put_nowait((copy.deepcopy(pos), self - 1, curlen + 1))
                    visited.add(h)
                pos[cg1][tp1] = self
            if self < 4:
                pos[cg1][tp1] = self + 1
                h = move_item_hash(curhash, self + 1, self, cg1, tp1 == 0)
                h = move_elevator_hash(h, self + 1, self)
                if h not in visited and check_safe(pos) and curlen < min_val:
                    q.put_nowait((copy.deepcopy(pos), self + 1, curlen + 1))
                    visited.add(h)
                pos[cg1][tp1] = self
            for j in range(i + 1, len(items)):
                (cg2, tp2) = items[j]
                if self > 1:
                    pos[cg1][tp1] = self - 1
                    pos[cg2][tp2] = self - 1
                    h = move_item_hash(curhash, self - 1, self, cg1, tp1 == 0)
                    h = move_item_hash(h, self - 1, self, cg2, tp2 == 0)
                    h = move_elevator_hash(h, self - 1, self)
                    if h not in visited and check_safe(pos) and curlen < min_val:
                        q.put_nowait((copy.deepcopy(pos), self - 1, curlen + 1))
                        visited.add(h)
                    pos[cg1][tp1] = self
                    pos[cg2][tp2] = self
                if self < 4:
                    pos[cg1][tp1] = self + 1
                    pos[cg2][tp2] = self + 1
                    h = move_item_hash(curhash, self + 1, self, cg1, tp1 == 0)
                    h = move_item_hash(h, self + 1, self, cg2, tp2 == 0)
                    h = move_elevator_hash(h, self + 1, self)
                    if h not in visited and check_safe(pos) and curlen < min_val:
                        q.put_nowait((copy.deepcopy(pos), self + 1, curlen + 1))
                        visited.add(h)
                    pos[cg1][tp1] = self
                    pos[cg2][tp2] = self

    print(part, min_val)


start_time = time.time()
getAnswer(initial_pos, 1, "Sample: ")  # Takes less than 1 sec
getAnswer(initial_pos1, 1, "Part 1: ")  # Takes 10 secs
getAnswer(initial_pos2, 1, "Part 2: ")  # Takes 11 minutes :')
print("--- %s seconds ---" % (time.time() - start_time))
