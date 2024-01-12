from utils.reader import read_lines

lines = read_lines("input")

r, c = 6, 50
on_set = set()

for line in lines:
    if line.startswith("rect"):
        xbyx = line.split("rect ")[1].split("x")
        for j in range(int(xbyx[0])):
            for i in range(int(xbyx[1])):
                on_set.add((i, j))
    elif line.startswith("rotate row y="):
        rowby = line.split("rotate row y=")[1].split(" by ")
        i, shift = int(rowby[0]), int(rowby[1])
        rem, add = set(), set()
        for j in range(c):
            if (i, j) in on_set:
                rem.add((i, j))
                add.add((i, (j + shift) % c))
        for t in rem:
            on_set.remove(t)
        for t in add:
            on_set.add(t)
    elif line.startswith("rotate column x="):
        colby = line.split("rotate column x=")[1].split(" by ")
        j, shift = int(colby[0]), int(colby[1])
        rem, add = set(), set()
        for i in range(r):
            if (i, j) in on_set:
                rem.add((i, j))
                add.add(((i + shift) % r, j))
        for t in rem:
            on_set.remove(t)
        for t in add:
            on_set.add(t)

print('Part 1: ', len(on_set))  # 121

for i in range(r):
    for j in range(c):
        if (i, j) in on_set:
            print('#', end='')
        else:
            print(' ', end='')
    print("\n", end='')

# ^^ prints RURUCEOEIL
