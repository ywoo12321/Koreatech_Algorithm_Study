import sys
from collections import deque
input = sys.stdin.readline
cnt = 1
#fun
def bfs(x,y,z):
    global cnt, turn
    visit[x][y][z] = 1
    queue = deque()
    queue.append((x,y,z))
    while queue:
        x, y, z = queue.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if li[nx][ny] == 0 and visit[nx][ny][z] == 0:
                cnt += 1
                visit[nx][ny][z] = visit[x][y][z] + 1
                queue.append((nx,ny,z))
            if li[nx][ny] == 1 and z == 0:
                visit[nx][ny][z+1] = visit[x][y][z] + 1
                queue.append((nx,ny,z+1))
    return -1
#in
n,m = map(int,input().split())
li = list(map(int,input().rstrip()) for _ in range(n))
for i in range(n):
    li[i] = list(li[i])
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
#out
print (bfs(0,0,0))
