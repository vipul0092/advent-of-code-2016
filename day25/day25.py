from utils.interpreter import run_interpreter
from utils.reader import read_lines

instr = read_lines("input")
instructions = list()

for ins in instr:
    parts = ins.split(" ")
    instructions.append((parts[0], parts[1], None if len(parts) == 2 else parts[2]))

# Lets make a number first, called Addend = first operand of second instruction * first operand of third instruction
# Now, the instructions given in the input are outputting the bits of the number => register a + Addend
# They start from the lsb and then go to the msb
# So the number (after doing the sum) should have the lsb as 0 and the msb as 1 and alternating bits in between
# Hence the number can only have even number of bits
# We start from 12 bits because a 10 bit number would be less than Addend (A good guess based on the puzzle inputs)
# We create the number with alternating bits and check if it is greater than Addend
# if it is greater, then the answer is simply (number - Addend)
addend = int(instructions[1][1]) * int(instructions[2][1])
ans = -1
for i in range(12, 32, 2):
    number = 0
    for k in range(i):
        number += (0 if k % 2 == 0 else 1 << k)
    if number > addend:
        ans = number - addend
        break
print('Answer:', ans)  # 175

# The answer above can be verified by running the interpreter below by passing `ans` as the input in register a
registers = [ans, 0, 0, 0]
# run_interpreter(instructions, registers)
