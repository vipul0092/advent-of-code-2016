from collections import deque
from utils.reader import read_lines

total = int(read_lines("input")[0])


def josephus(n, k):
    q = deque()
    for i in range(1, n + 1):
        q.append(i)
    while len(q) != 1:
        for j in range(k - 1):
            temp = q.popleft()
            q.append(temp)
        q.popleft()
    return q.popleft()


def josephus2(n):
    # Create 2 queues of equal size or (a diff or 1 for odd lengths)
    # we'll always pop from q2, so in odd lengths, length of q2 will be one more than q1
    q1 = deque()
    q2 = deque()

    for i in range(1, n // 2 + 1):
        q1.append(i)
    for i in range(n // 2 + 1, n + 1):
        q2.append(i)

    while not (len(q1) == 0 and len(q2) == 1):
        temp = q2.popleft()
        # print('Removed ', temp)
        removed_from_1st = q1.popleft()
        q2.append(removed_from_1st)  # This will always be done, move the current item to end of second queue
        # If length diff is 2, balance the queues by inserting an element in first queue, and remove from second queue
        if abs(len(q1) - len(q2)) == 2:
            q1.append(q2.popleft())
    return q2.pop()


print('Part 1: ', josephus(total, 2))  # 1816277
print('Part 2: ', josephus2(total))  # 1410967
