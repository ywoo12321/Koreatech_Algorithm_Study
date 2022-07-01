import sys
from collections import deque
input = sys.stdin.readline
cnt = 0
#fun
def solution(n,sns):
    global cnt
    a = 0
    for i in range(n-1):
        sns[i] = list(sns[i]) 
    cnt += graph[1]
    # for i in graph[1]:
    #     visit[i] = True
    for i in range(len(graph),n+1):
        if len(graph[i]) == 1:
            a += 1
    return a
    dfs(1)
    
def dfs(start):
    global cnt,graph,visit
    visit[start] = True
    for i in graph[start]:
        if visit[i] == False:
            dfs(i,visit,graph)
    return
#input
n = int(input().rstrip())
sns = (list(map(int,input().split()) for _ in range(n-1)))
graph = [[] for _ in range(n+1)]
for start, end in sns:
    graph[start].append(end)
    graph[end].append(start)
visit = [False] * (n + 1)   
#output
print(solution(n,sns))
print(cnt)