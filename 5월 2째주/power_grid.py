import sys
from collections import deque
def bfs(start,visit,graph):
    queue = deque([start])
    cnt = 1
    while queue:
        a = queue.popleft()
        
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    print (graph) #그래프 구현 완료
    #bfs를 통해서 하나씩 끊어가면 abs(cnt - (n - cnt)) 출력  << 구현 못하겠음

    return 

n = int(sys.stdin.readline().rstrip())
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(n,wires)