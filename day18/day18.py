import time

from utils.reader import read_lines

start = read_lines("input")[0]


def solve2(row: str, max_rows: int):
    rows = 1
    bits = [1 if row[i] == '^' else 0 for i in range(len(row))]
    count = 0
    while rows <= max_rows:
        for bit in bits:
            if bit == 0:
                count += 1
        new_bits = list()
        new_bits.append(0 if bits[1] == 0 else 1)
        for i in range(1, len(bits) - 1):
            new_bits.append(0 if bits[i - 1] == 0 and bits[i + 1] == 0 else bits[i - 1] ^ bits[i + 1])
        new_bits.append(0 if bits[len(bits) - 2] == 0 else 1)
        bits = new_bits
        rows += 1
    return count


start_time = time.time()
print('Part 1: ', solve2(start, 40))  # 1984
print("--- Took %s seconds ---" % (time.time() - start_time))
print('')
start_time = time.time()
print('Part 2: ', solve2(start, 400000))  # 19999894
print("--- Took %s seconds ---" % (time.time() - start_time))
