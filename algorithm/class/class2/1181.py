import sys

n = int(sys.stdin.readline())

word = list()

for _ in range(n):
    w = sys.stdin.readline().strip()
    if w in word:
        continue
    word.append(w)

word.sort()
word.sort(key=len)

for i in word:
    print(i)