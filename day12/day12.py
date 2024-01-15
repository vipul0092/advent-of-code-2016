from utils.reader import read_lines

lines = read_lines("input")


def get_op(_op: str) -> int:
    if len(_op) == 1 and ord('a') <= ord(_op[0]) <= ord('z'):
        return registers[ord(_op[0]) - ord('a')]
    return int(_op)


def get_register(op: str) -> int:
    return ord(op[0]) - ord('a')


def solve():
    idx = 0
    while idx < len(lines):
        parts = lines[idx].split(" ")
        match parts[0]:
            case "inc":
                register = get_register(parts[1])
                registers[register] += 1
            case "dec":
                register = get_register(parts[1])
                registers[register] -= 1
            case "cpy":
                register = get_register(parts[2])
                op = get_op(parts[1])
                registers[register] = op
            case "jnz":
                op1, op2 = get_op(parts[1]), get_op(parts[2])
                if op1 != 0:
                    idx += op2
                    idx -= 1
        idx += 1


registers = [0, 0, 0, 0]
solve()
print('Part 1: ', registers[0])  # 318117

registers = [0, 0, 1, 0]
solve()
print('Part 2: ', registers[0])  # 9227771


