from collections import deque
n = int(input())
dq = deque()

for x in range(n):
    usr = input().split()
    first = usr[0]

    if first == "append":
        dq.append(usr[1])
    elif first == "appendleft":
        dq.appendleft(usr[1])
    elif first == "pop":
        dq.pop()
    elif first == "popleft":
        dq.popleft()

print(*dq)
