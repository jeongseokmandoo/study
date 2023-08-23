# G 딕셔너리 이용

def BFS(graph, start_node):
    visit = list()
    queue = list()
    visit.append(start_node)
    queue.append(start_node)
    while len(queue) > 0:
        for each_node in graph[queue[0]]:
            if (each_node in visit) == False :
                visit.append(each_node)
                queue.append(each_node)
        del queue[0]
    return visit

# G 인접 리스트 이용

from collections import deque

visited = [False] * 9

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True