import sys
input = sys.stdin.readline
#fun
def is_pelindrom(start, end):
    a = []
    b = []
    
    e_s = (end - start)
    if start == end:
        return 1
    if e_s % 2 == 0:            #검사 지점의 중간 값이 한개 일때
        if start <= n//2:        #시작 값이 총 개수의 중간보다 작을 때
            for i in range(start , e_s// 2 + 1):
                a.append(li[i])
            for i in range(e_s//2, end + 1):
                b.append(li[i])
        else:                        #시작 값이 총 개수의 중간보다 클 때
            for i in range(start , e_s//2 + start + 1):
                a.append(li[i])
            for i in range(e_s//2 + start, end + 1):    
                b.append(li[i])
    else:            #검사 지점의 중간 값이 두개 일때
        if start <= n//2:        #시작 값이 총 개수의 중간보다 작을 때
            for i in range(start , e_s// 2 + 2):
                a.append(li[i])
            for i in range(e_s//2 + 2, end + 1):
                b.append(li[i])
        else:                        #시작 값이 총 개수의 중간보다 클 때
            for i in range(start , e_s//2 + start + 2):
                a.append(li[i])
            for i in range(e_s//2 + start + 2, end + 1):
                b.append(li[i])
    print (a, b)
    b.sort()
    a.sort()
    if a == b:
        return 1
    else:
        return 0
#in
n = int(input().rstrip())
li = list(map(int,input().split()))
m = int(input().rstrip())
qu = list(map(int,input().split()) for _ in range(m))
for i in range(m):
    qu[i] = list(qu[i])
#out
for x, y in qu:
    print(is_pelindrom(x-1,y-1))
