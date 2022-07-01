import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
#fun
def maxlen_branch(start):
    global max_branch
    global branch
    if start == n:
        if max_branch < branch:
            max_branch = branch
            branch = 0
    else:
        for i in graph[start]:
            branch += i[1]
            maxlen_branch(i[0])
def len_pillar(start,end):
    root = [start]
    global n
    global graph
    visited = [0]*(n+1)
    way = [0]*(n+1)
    while root:
        k = root.pop(0)
        if k == end:
            break
        if visited[k] == 0:
            visited[k] = 1
            for i in graph[k]:
                root.append(i[0])
                way[i[0]] = way[k] + i[1]
    return way[end]
#in
n, r = map(int,input().split())
li = list(map(int,input().split()) for _ in range(n-1))
for i in range(n-1):
    li[i] = list(li[i])
graph = [[] for _ in range(n+1)]
for x,y,z in li:
    graph[x].append((y,z))
    graph[y].append((x,z))
pillar = 0
max_branch = 0
branch = 0
giga_idx = 0
visit = [False] * (n + 1)
for i in range(1, n+1):
    if len(graph[i]) >= 3:
        giga_idx = i
        break
 
#out
print(*graph,sep='\n')
print (len_pillar(1,giga_idx))
maxlen_branch(giga_idx)
print (max_branch, branch)