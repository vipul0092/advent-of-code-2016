from utils.reader import read_lines

inp = read_lines("input")[0]


def dragon_curve(string: str) -> str:
    flipped = ''.join(['1' if i == '0' else '0' for i in string])
    return string + '0' + flipped[::-1]


def solve1(disk_size):
    string = inp
    while len(string) < disk_size:
        string = dragon_curve(string)
    string = string[:disk_size]
    checksum = string
    while True:
        _sum = ''
        for i in range(0, len(checksum)-1, 2):
            if checksum[i] == checksum[i+1]:
                _sum += '1'
            else:
                _sum += '0'
        checksum = _sum
        if len(checksum) % 2 == 1:
            break
    return checksum


print('Part 1: ', solve1(272))  # 11100110111101110
print('Part 2: ', solve1(35651584))  # 10001101010000101
