import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y,dx,dy,graph):
    queue = deque()
    queue.append((x,y))
    print("first 큐:",queue)
    while queue:
        x,y = queue.popleft()
        cnt = 0
        print("second 큐:",queue)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx,ny)
            if nx < 0 or nx>=n or ny>=n or ny<0 or ny== y or nx == x:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                cnt += 1
                queue.append((nx,ny))
    return graph[2][2]

def charge_fuel(fuel,cnt):
    fuel += cnt * 2
    return fuel
def go_passenger(n,m,fuel,map_list,taxi_start,passenger):
    graph = []
    for i in range(n):
        map_list[i] = list(map_list[i])
        graph.append(map_list[i])
    for i in range(m):
        passenger[i] = list(passenger[i])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    print (bfs(taxi_start[0]-1,taxi_start[1]-1,dx,dy,graph))
    return 
# def go_destination():

n,m,fuel = map(int,input().split())
map_list = (list(map(int,input().split()) for _ in range(n)))
taxi_start = list(map(int,input().split()))
passenger = (list(map(int,input().split()) for _ in range(m)))
# print(go_passenger(n,m,fuel,map_list,taxi_start,passenger))
go_passenger(n,m,fuel,map_list,taxi_start,passenger)
