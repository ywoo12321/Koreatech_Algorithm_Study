import sys
from collections import deque
input = sys.stdin.readline
#fun
def bfs(start):
    # 안즈는 사탕나무를 생일선물로 받았다.
    # 사탕나무는\(N\)개의 사탕을 트리 형태로 이은 것을 말한다. 
    # 각 사탕은 길이가 1인 간선으로 연결되어있고, 임의의 두 사탕 사이의 최단 경로는 유일하다.
    # 안즈는 이 사탕나무에서 기준이 되는 사탕을 하나 골라, 그 사탕과의 최단거리가
    # \(K\)이하인 모든 사탕을 다 먹어버리려고 한다!
    # 그런데 안즈는 문득 기준으로 어떤 사탕을 골라야 사탕을 가장 많이 먹을 수 있을지 궁금해졌다.
    # 하지만 그 순간 안즈는 매우 귀찮아졌기 때문에, 여러분에게 해결을 부탁했다.
    queue = deque([start])
    visit[start] = 1
    result = 1
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visit[i] == 0:
                visit[i] = 1
                result += 1
                queue.append(i)
    return result
#in
n, k = map(int,input().split())
li = list(map(int,input().split()) for _ in range(n-1))
graph = [[] for _ in range(n+1)]
for x, y in li:
    graph[x].append(y)
    graph[y].append(x)
#out
candy = []
for a,not_visit in li:
        visit = [0] * (n + 1)
        visit[not_visit] = 1
        candy.append(bfs(a))
print(candy)