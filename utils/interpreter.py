def get_op(_op: str, registers) -> int:
    if len(_op) == 1 and ord('a') <= ord(_op[0]) <= ord('z'):
        return registers[ord(_op[0]) - ord('a')]
    return int(_op)


def get_register(op: str) -> int:
    return ord(op[0]) - ord('a')


def run_interpreter(instructions, registers):
    idx = 0
    iterations = 0
    while idx < len(instructions):
        parts = instructions[idx]
        match parts[0]:
            case "inc":
                register = get_register(parts[1])
                registers[register] += 1
            case "dec":
                register = get_register(parts[1])
                registers[register] -= 1
            case "cpy":
                register = get_register(parts[2])
                op = get_op(parts[1], registers)
                registers[register] = op
            case "jnz":
                op1, op2 = get_op(parts[1], registers), get_op(parts[2], registers)
                if op1 != 0:
                    idx += op2
                    idx -= 1
            case "tgl":
                op = get_op(parts[1], registers)
                to_change = op + idx
                if 0 <= to_change < len(instructions):
                    to_change_instr = instructions[to_change][0]
                    if instructions[to_change][2] is None:  # One argument
                        if to_change_instr == "inc":
                            to_change_instr = "dec"
                        else:
                            to_change_instr = "inc"
                    else:  # Two arguments
                        if to_change_instr == "jnz":
                            to_change_instr = "cpy"
                        else:
                            to_change_instr = "jnz"
                    instructions[to_change] = (to_change_instr, instructions[to_change][1], instructions[to_change][2])
            case "out":
                op = get_op(parts[1], registers)
                print(op)
        idx += 1
        iterations += 1
