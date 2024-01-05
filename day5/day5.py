import hashlib
from utils.reader import read_lines

string = read_lines("input")[0]
code = ''
suffix = 0
while len(code) != 8:
    md5 = hashlib.md5((string + str(suffix)).encode('utf-8')).hexdigest()
    if md5.startswith("00000"):
        code += md5[5]
    suffix += 1
print('Part 1 :', code)  # d4cd2ee1

code_arr = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
suffix = 0
x = 8
while x != 0:
    md5 = hashlib.md5((string + str(suffix)).encode('utf-8')).hexdigest()
    if md5.startswith("00000") and '0' <= md5[5] <= '7':
        pos = int(md5[5])
        if code_arr[pos] == 'x':
            code_arr[pos] = md5[6]
            x -= 1
    suffix += 1
code = ''
for char in code_arr:
    code += char
print('Part 2 :', code)  # f2c730e5
