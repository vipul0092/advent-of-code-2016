from utils.interpreter import run_interpreter
from utils.reader import read_lines

lines = read_lines("input")
instructions = list()

for ins in lines:
    parts = ins.split(" ")
    instructions.append((parts[0], parts[1], None if len(parts) == 2 else parts[2]))

registers = [0, 0, 0, 0]
run_interpreter(instructions, registers)
print('Part 1: ', registers[0])  # 318117

registers = [0, 0, 1, 0]
run_interpreter(instructions, registers)
print('Part 2: ', registers[0])  # 9227771


