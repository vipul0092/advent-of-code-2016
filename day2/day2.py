from utils.reader import read_lines

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
keypad2 = [[None, None, '1', None, None], [None, '2', '3', '4', None], ['5', '6', '7', '8', '9'],
           [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]

lines = read_lines("input")

number = ''
current = (1, 1)
for line in lines:
    for d in line:
        match d:
            case 'U':
                current = current if current[0] == 0 else (current[0] - 1, current[1])
            case 'D':
                current = current if current[0] == 2 else (current[0] + 1, current[1])
            case 'L':
                current = current if current[1] == 0 else (current[0], current[1] - 1)
            case 'R':
                current = current if current[1] == 2 else (current[0], current[1] + 1)
    number += str(keypad[current[0]][current[1]])

print('Part 1: ', number)  # 18843

number = ''
current = (2, 0)
for line in lines:
    for d in line:
        match d:
            case 'U':
                current = current if (current[0] == 0 or keypad2[current[0] - 1][current[1]] is None) else (
                    current[0] - 1, current[1])
            case 'D':
                current = current if (current[0] == 4 or keypad2[current[0] + 1][current[1]] is None) else (
                    current[0] + 1, current[1])
            case 'L':
                current = current if (current[1] == 0 or keypad2[current[0]][current[1] - 1] is None) else (
                    current[0], current[1] - 1)
            case 'R':
                current = current if (current[1] == 4 or keypad2[current[0]][current[1] + 1] is None) else (
                    current[0], current[1] + 1)
    number += str(keypad2[current[0]][current[1]])

print('Part 2: ', number)  # 67BB9

