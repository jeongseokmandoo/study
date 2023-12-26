from collections import deque

case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    doc = deque(doc)

    result = 1
    while doc:
        if M == 0 and max(doc) == doc[0]:
            print(result)
            break
        if doc[0] < max(doc):
            doc.rotate(-1)
            M = (M - 1) % len(doc)
        else:
            doc.popleft()
            M -= 1
            result += 1

            