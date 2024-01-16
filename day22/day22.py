from collections import deque

from utils.reader import read_lines

lines = read_lines("input")
diffs = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_used(node: ((int, int), int, int)) -> int:
    return node[2]
def get_size(node: ((int, int), int, int)) -> int:
    return node[1]
def get_avail(node: ((int, int), int, int)) -> int:
    return node[1] - node[2]
def adjust_used(loc, new_used):
    nodes[loc] = (loc, nodes[loc][1], new_used)

# pos -> (pos, size, used)
nodes = dict()
node_locations = list()
max_x, zero_loc = -1, (-1, -1)
for i in range(2, len(lines)):
    parts = lines[i].split(" ")
    values = list()
    for p in parts:
        if len(p) == 0:
            continue
        values.append(p)
    x, y = int(values[0].split("-")[1][1:]), int(values[0].split("-")[2][1:])
    max_x = max(max_x, x)
    size = int(values[1][:len(values[1]) - 1])
    used = int(values[2][:len(values[2]) - 1])
    loc = (x, y)
    nodes[loc] = (loc, size, used)
    node_locations.append(loc)
    if used == 0:
        zero_loc = loc

count = 0
for i in range(len(node_locations)):
    for j in range(len(node_locations)):
        if i == j:
            continue
        node1, node2 = nodes[node_locations[i]], nodes[node_locations[j]]
        if get_used(node1) != 0 and get_avail(node2) >= get_used(node1):
            count += 1

print('Part 1: ', count)  # 955

# ----- Part 2 Begins -----


def move_zero_loc(from_loc, to_loc, skip_visit=None):
    curr_dest = to_loc
    current = from_loc
    q, visited = deque(), {(int, int)}
    q.append((current, list()))
    if skip_visit is not None:
        visited.add(skip_visit)
    visited.add(current)

    moved_path = None
    while len(q) != 0:
        (curr, path) = q.popleft()
        if curr == curr_dest:
            moved_path = path
            break
        for diff in diffs:
            can_move = (curr[0] + diff[0], curr[1] + diff[1])
            # `curr` will be emptied along the way, so we're checking if curr's size can hold can_move's data
            if can_move in nodes and can_move not in visited and get_used(nodes[can_move]) <= get_size(nodes[curr]):
                new_path = path.copy()
                new_path.append(curr)
                q.append((can_move, new_path))
                visited.add(can_move)
    # adjust the sizes of the locations that we visited along the way
    prev_loc = None
    for moved_loc in moved_path:
        if prev_loc is None:
            prev_loc = moved_loc
        else:
            adjust_used(prev_loc, get_used(nodes[moved_loc]))
            prev_loc = moved_loc
    adjust_used(prev_loc, get_used(nodes[to_loc]))
    adjust_used(to_loc, 0)
    return len(moved_path)


total_steps = 0
# we'll move the destination along the top row
to_move = (max_x, 0)
while True:
    if to_move == (0, 0):  # Reached the destination
        break
    dest = (to_move[0] - 1, 0)
    # Go from zero_loc to dest
    cur_loc = zero_loc
    # last argument `to_move` is being sent because we don't want the zero marker to move to that position
    total_steps += move_zero_loc(zero_loc, dest, to_move)
    # Now that we have reached the dest, dest will become the new to_move and zero_loc will be shifted to to_move
    total_steps += move_zero_loc(dest, to_move)
    to_move, zero_loc = dest, to_move
    # print('Zero Loc moved to ', zero_loc, ', data moved to ', to_move, ', total steps ', total_steps)

print('Part 2: ', total_steps) # 246
