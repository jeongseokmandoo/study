# G 딕셔너리 사용
dfs_visit = list()

def DFS(graph, start_node):
    dfs_visit.append(start_node)
    for each_node in graph[start_node]:
        if (each_node in dfs_visit) == False:
            DFS(graph, each_node)

# 인접 리스트 이용

visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)