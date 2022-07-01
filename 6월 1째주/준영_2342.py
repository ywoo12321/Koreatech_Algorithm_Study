from runpy import run_path
import sys
input = sys.stdin.readline
#fun
def ddr(li):
    f_p = [0,0]
    answer = 0 
    f_p[0] = li[0]
    ck = 1
    for i in range(1, len(li)):
        if li[i] == 0:
            break
        if li[i] != li[i-1]:
            f_p[ck] = li[i]
            answer += graph[li[i]][li[i-1]]
        else:
            f_p[1-ck] = li[i]
            answer += graph[li[i]][li[i]]
    return answer
#in
li = list(map(int, input().split()))
graph = [[1,2,2,2,2],[2,1,3,4,3],[2,3,1,3,4],[2,4,3,1,3],[2,3,4,3,1]]
#out
print(ddr(li))