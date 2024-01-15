import sys

from utils.reader import read_lines
sys.setrecursionlimit(100000)

instructions = read_lines("input")
start = "abcdefgh"


def rotate(arr, times, right):
    times = times % len(arr)
    new_arr, nidx = [char for char in arr], 0
    if not right:
        for k in range(times, len(arr)):
            new_arr[nidx] = arr[k]
            nidx += 1
        for k in range(times):
            new_arr[nidx] = arr[k]
            nidx += 1
    else:
        return rotate(arr, len(arr) - times, False)
    return new_arr


def scramble(string):
    curr = [char for char in string]
    for j in range(len(instructions)):
        instruction = instructions[j]
        if instruction.startswith("swap position"):
            pos1 = int(instruction.split("p position ")[1].split(" with")[0])
            pos2 = int(instruction.split("with position ")[1])
            tmp = curr[pos1]
            curr[pos1] = curr[pos2]
            curr[pos2] = tmp
        elif instruction.startswith("swap letter"):
            letter1 = instruction.split("p letter ")[1].split(" with")[0][0]
            letter2 = instruction.split("with letter ")[1][0]
            pos1, pos2 = -1, -1
            for i in range(len(curr)):
                if curr[i] == letter1:
                    pos1 = i
                if curr[i] == letter2:
                    pos2 = i
            tmp = curr[pos1]
            curr[pos1] = curr[pos2]
            curr[pos2] = tmp
        elif instruction.startswith("rotate based"):
            letter = instruction.split("letter ")[1][0]
            pos = -1
            for i in range(len(curr)):
                if curr[i] == letter:
                    pos = i
                    break
            curr = rotate(curr, 1 + pos + (1 if pos >= 4 else 0), True)
        elif instruction.startswith("rotate"):
            parts = instruction.split("otate ")[1].split(" step")[0].split(" ")
            curr = rotate(curr, int(parts[1]), parts[0] == "right")
        elif instruction.startswith("reverse positions"):
            parts = instruction.split("positions ")[1].split(" through ")
            i, j = int(parts[0]), int(parts[1])
            while i <= j:
                tmp = curr[i]
                curr[i] = curr[j]
                curr[j] = tmp
                i += 1
                j -= 1
        elif instruction.startswith("move"):
            parts = instruction.split("ve position ")[1].split(" to position ")
            pos1, pos2 = int(parts[0]), int(parts[1])
            replace = curr[pos1]
            if pos1 > pos2:
                for i in range(pos1 - pos2):
                    curr[pos1-i] = curr[pos1-i-1]
            else:
                for i in range(pos2 - pos1):
                    curr[pos1 + i] = curr[pos1 + i + 1]
            curr[pos2] = replace
        # print(''.join(curr))
    return ''.join(curr)


print('Part 1: ', scramble(start))  # bfheacgd


def recurse(string, bitmap):
    if len(string) == 8:
        scrambled = scramble(string)
        if scrambled == "fbgdceah":
            return string
        else:
            return ''

    for i in range(8):
        if bitmap & (1 << i) == 0:
            result = recurse(string + chr(ord('a') + i), bitmap | (1 << i))
            if result != '':
                return result
    return ''


print('Part 2: ', recurse('', 0))  # gcehdbfa


