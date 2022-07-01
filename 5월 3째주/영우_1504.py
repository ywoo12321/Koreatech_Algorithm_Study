import sys
import heapq
input = sys.stdin.readline
INF = 10**9
#fun
def dijkstra(start):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start]= 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance
#in
v, e = map(int,input().split())
li = list(map(int,input().split()) for _ in range(e))
v1,v2 = map(int,input().split())
for i in range(e):
    li[i] = list(li[i])
graph = [[] for _ in range(v+1)]
for x,y,z in li:
    graph[x].append((y,z))
    graph[y].append((x,z))

#out
one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
min_dist = min(one[v1] + v1_[v2] + v2_[v], one[v2] + v2_[v1] + v1_[v])
print(min_dist if min_dist < INF else -1)