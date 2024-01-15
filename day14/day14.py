import hashlib
import time
from collections import defaultdict

from utils.reader import read_lines
from sortedcontainers import SortedList, SortedDict

string = read_lines("input")[0]
hash_idx = 0
hashes = dict()
triplets = SortedDict()
quintuples = defaultdict(SortedList)
answer = -1


def calc_triplets_quintuplets(md5, idx):
    triplet_found = False
    for i in range(len(md5) - 2):
        if not triplet_found and md5[i] == md5[i + 1] and md5[i + 1] == md5[i + 2]:
            triplets[idx] = md5[i]
            triplet_found = True
        if (i < len(md5) - 4 and md5[i] == md5[i + 1] and md5[i + 1] == md5[i + 2]
                and md5[i + 2] == md5[i + 3] and md5[i + 3] == md5[i + 4]):
            quintuples[md5[i]].add(idx)


def calc_hash(idx, extra_times=0) -> str:
    if idx not in hashes:
        md5 = hashlib.md5((string + str(idx)).encode('utf-8')).hexdigest()
        while extra_times > 0:
            md5 = hashlib.md5(md5.encode('utf-8')).hexdigest()
            extra_times -= 1
        hashes[idx] = md5
        global hash_idx
        hash_idx = max(hash_idx, idx)
        calc_triplets_quintuplets(md5, idx)
    return hashes[idx]


def find_quintuple(_char, idx) -> bool:
    if _char in quintuples:
        right = quintuples[_char].bisect_left(idx + 1000)
        if right != 0 and quintuples[_char][right - 1] > idx:
            global answer
            # print('Key found: ', idx)
            answer = idx
            return True
    return False


def part1(extra_times=0):
    global hash_idx, hashes, triplets, quintuples
    hash_idx, hashes, triplets, quintuples, keys, index = 0, dict(), SortedDict(), defaultdict(SortedList), 0, 0
    while keys != 64:
        calc_hash(index, extra_times)
        if index in triplets:
            char = triplets[index]
            if char in quintuples and find_quintuple(char, index):
                keys += 1
                index += 1
                continue
            found = False
            tmp_hash_idx = hash_idx + 1
            while tmp_hash_idx <= index + 1000:
                calc_hash(tmp_hash_idx, extra_times)
                if find_quintuple(char, index):
                    found = True
                    break
                tmp_hash_idx += 1
            if found:
                keys += 1
        index += 1


start_time = time.time()
part1()
print('Part 1: ', answer)  # 23769
print("--- Took %s seconds ---" % (time.time() - start_time))
print('')
start_time = time.time()
part1(extra_times=2016)
print('Part 2: ', answer)  # 20606
print("--- Took %s seconds ---" % (time.time() - start_time))
