from utils.reader import read_lines

string = read_lines("input")[0]


def decompress(size, start_idx, recurse=False):
    index = start_idx
    total_length = 0
    while index < start_idx + size:
        if string[index] == '(':
            size_string = ''
            while string[index] != ')':
                if string[index] != '(' and string[index] != ')':
                    size_string += string[index]
                index += 1
            s_t = size_string.split("x")
            current_size, times = int(s_t[0]), int(s_t[1])
            total_length += ((current_size if not recurse else decompress(current_size, index + 1, recurse)) * times)
            index += (current_size + 1)
        else:
            total_length += 1
            index += 1
    return total_length


print('Part 1: ', decompress(len(string), 0))  # 152851
print('Part 2: ', decompress(len(string), 0, recurse=True))  # 11797310782
