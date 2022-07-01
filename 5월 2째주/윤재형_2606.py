import sys
from collections import deque
input = sys.stdin.readline

#fun
def solution(n,m,network):
    for i in range(m):
        network[i] = list(network[i])
    graph = [[] for _ in range(n+1)]
    for start, end in network:
        graph[start].append(end)
        graph[end].append(start)
    for i in range(n+1):
        graph[i].sort()
    visit = [False] * (n + 1)
    bfs(1,visit,graph)
    a = visit.count(True) -1
    return a

def bfs(start,visit,graph):
    queue = deque([start])
    visit[start] = True
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visit[i] == False:
                queue.append(i)
                visit[i] = True

#input
n = int(input().rstrip())
m = int(input().rstrip())
network = (list(map(int,input().split()) for _ in range(m)))
#output
print(solution(n,m,network))