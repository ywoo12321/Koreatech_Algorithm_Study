from operator import pos
import sys, copy
input = sys.stdin.readline
#fun
def earthWarming(coloum, row, ice_mountain):
    global year
    mountain_num = 0
    while True:
        if mountain_num >= 2:
            break
        dfs()
        year += 1
        print (*ice_mountain, sep = '\n')
        for i in range(coloum):
            for j in range(row):
                if isOneMountain(i,j) == True:
                    mountain_num += 1
    
                #빙하녹이고
                #연수 증가
                #빙하가 나위어져있는지 확인 2개면 끝내고 아니면 처음으로 돌아가서
                

def isOneMountain(ice_coloum, ice_row):
    global row, coloum, visited
    if ice_row <= -1 or ice_row >= row or ice_coloum <= -1 or ice_coloum >= coloum:
        return False
    if ice_mountain[ice_coloum][ice_row] != 0 and visited[ice_coloum][ice_row] == 0:
        visited[ice_coloum][ice_row] = 1
        for i in range(4):
            isOneMountain(ice_coloum + dx[i] ,ice_row + dy[i])
            return True
    return False
    #한덩어리인지
    #아니면 출력하게
def dfs():
    global ice_mountain, row, coloum
    global visit
    bef_ice_mountain = copy.deepcopy(ice_mountain)
    for i in range(coloum):
        for j in range(row):
            ck_zero  = 0
            if bef_ice_mountain[i][j] != 0:
                for dir in range(4):
                    new_x = j + dx[dir]
                    new_y = i + dy[dir]
                    if 0 > new_y and new_y >= coloum and 0 > new_x and new_x >= row:
                        continue
                    if bef_ice_mountain[new_y][new_x] == 0:
                        ck_zero += 1
                if ice_mountain[i][j] - ck_zero >=0:
                    ice_mountain[i][j] -= ck_zero
                else:
                    ice_mountain[i][j] = 0
                                      

    #주위에 연결되어있는게 몇개인지 확인
#in
coloum, row = map(int,input().split())
ice_mountain = list(map(int,input().split()) for _ in range(coloum))
visit = [[False] * row for _ in range(coloum)] 
visited = [[False] * row for _ in range(coloum)] 
for i in range(coloum):
    ice_mountain[i] = list(ice_mountain[i])

year = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
#out
earthWarming(coloum,row,ice_mountain)
print(year)
