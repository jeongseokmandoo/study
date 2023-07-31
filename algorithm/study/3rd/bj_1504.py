from heapq import heappush
from heapq import heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance

result = []


distance_1 = dijkstra(1)
first_v1 = distance_1[v1]
first_v2 = distance_1[v2]
distance_v1 = dijkstra(v1)
second_v2 = distance_v1[v2]
v1_n = distance_v1[n]
distance_v2 = dijkstra(v2)
second_v1 = distance_v2[v1]
v2_n = distance_v2[n]

result.append(first_v1 + second_v2 + v2_n)
result.append(first_v2 + second_v1 + v1_n)

if min(result) < INF:
    print(min(result))
else:
    print(-1)
