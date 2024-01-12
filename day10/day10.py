from utils.reader import read_lines

lines = read_lines("input")

two_bot = set()
bots = [list([]) for _ in range(300)]
output = [-1 for _ in range(300)]
bots_give = [[-1, -1, -1, -1] for _ in range(300)]

for line in lines:
    if line.__contains__(" goes to bot "):
        parts = line.split(" goes to bot ")
        bot = int(parts[1])
        value = int(parts[0].split(" ")[1])
        bots[bot].append(value)
        if len(bots[bot]) == 2:
            two_bot.add(bot)
    else:
        parts = line.split(" gives low to ")
        src = int(parts[0].split(" ")[1])
        parts = parts[1].split(" and high to ")
        op = parts[0].split(" ")
        bots_give[src][2] = 0 if op[0] == "bot" else 1
        bots_give[src][0] = int(op[1])
        op = parts[1].split(" ")
        bots_give[src][3] = 0 if op[0] == "bot" else 1
        bots_give[src][1] = int(op[1])

part1 = -1
while len(two_bot) != 0:
    bot = two_bot.pop()
    values = bots[bot]
    low = values[0] if values[0] <= values[1] else values[1]
    high = values[0] if low == values[1] else values[1]

    if low == 17 and high == 61:
        part1 = bot

    if bots_give[bot][2] == 0:
        bots[bots_give[bot][0]].append(low)
        if len(bots[bots_give[bot][0]]) == 2:
            two_bot.add(bots_give[bot][0])
    else:
        output[bots_give[bot][0]] = low

    if bots_give[bot][3] == 0:
        bots[bots_give[bot][1]].append(high)
        if len(bots[bots_give[bot][1]]) == 2:
            two_bot.add(bots_give[bot][1])
    else:
        output[bots_give[bot][1]] = high

print('Part 1: ', part1)  # 93
print('Part 2: ', output[0] * output[1] * output[2])  # 47101

