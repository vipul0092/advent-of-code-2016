from utils.reader import read_lines

ranges_str = read_lines("input")
ranges = list()
for r in ranges_str:
    start = int(r.split('-')[0])
    end = int(r.split('-')[1])
    ranges.append((start, end))
ranges = sorted(ranges, key=lambda it: it[0])

# Ranges merge logic
merged = list()
for r in ranges:
    if len(merged) == 0:
        merged.append(r)
        continue
    index = -1
    # Find the first range after which the current range can be inserted
    for i in range(len(merged)):
        if merged[i][0] <= r[0] <= merged[i][1]:
            index = i
            break
    if index == -1:
        index = 0 if r[0] <= merged[0][0] else len(merged)
    merged.insert(index+1, r)

    current = merged[0]
    new_merged = list()
    for i in range(1, len(merged)):
        if not (current[1]+1 < merged[i][0] or merged[i][1]+1 < current[0]):
            current = (min(current[0], merged[i][0]), max(current[1], merged[i][1]))
        else:
            new_merged.append(current)
            current = merged[i]
    new_merged.append(current)
    merged = new_merged

print('Part 1: ', merged[0][1] + 1)  # 31053880

total_ips = 4294967295 + 1
for r in merged:
    total_ips -= (r[1]-r[0]+1)

print('Part 2: ', total_ips)  # 117


