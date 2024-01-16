from utils.interpreter import run_interpreter
from utils.reader import read_lines

instr = read_lines("input")
instructions = list()

for ins in instr:
    parts = ins.split(" ")
    instructions.append((parts[0], parts[1], None if len(parts) == 2 else parts[2]))
ins_len = len(instructions)

registers = [7, 0, 0, 0]
run_interpreter(instructions, registers)
print('Part 1: ', registers[0])  # 10880


# The instructions are doing a factorial of the number passed in register `a`
# and then adding the first arguments of 6th last and 7th last instructions
def fact(num):
    return 1 if num == 1 else num * fact(num - 1)


print('Part 1: ', fact(7) + int(instructions[ins_len-6][1]) * int(instructions[ins_len-7][1]))  # 10880
print('Part 2: ', fact(12) + int(instructions[ins_len-6][1]) * int(instructions[ins_len-7][1]))  # 479007440
