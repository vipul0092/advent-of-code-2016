from utils.reader import read_lines

lines = read_lines("input")


class Comparator(tuple):
    def __lt__(self, other):
        return self[0] > other[0] if self[1] == other[1] else self[1] < other[1]


part1 = 0
part2 = -1
for line in lines:
    parts = line.split('-')
    count_map = {}
    for i in range(0, len(parts) - 1):
        for char in parts[i]:
            count_map.setdefault(char, 0)
            count_map[char] += 1
    count_map = sorted(count_map.items(), key=Comparator, reverse=True)
    # print(count_map)
    last = parts[len(parts)-1]
    checksum = last[last.find('[')+1: last.find(']')]
    sector_id = int(last[:last.find('[')])

    foundsum = ''
    for i in range(0, len(checksum)):
        foundsum += count_map[i][0]
    if foundsum == checksum:
        part1 += sector_id
        decrypted = ''
        for i in range(0, len(parts) - 1):
            for char in parts[i]:
                decrypted += chr(ord('a') + ((ord(char[0]) - ord('a') + sector_id) % 26))
            decrypted += ' '
        if decrypted == 'northpole object storage ':
            part2 = sector_id


print('Part 1: ', part1)  # 245102
print('Part 2: ', part2)  # 324
