import sys
input = sys.stdin.readline
from itertools import combinations
#fun
def dfs():
    comb = combinations(li,n)
    for x in comb:
        mo = 0
        ja = 0
        for i in range(n):
            if x[i] in m:
                mo += 1
            else:
                ja += 1
        if mo >= 1 and ja >= 2:
            a.append(x)
#in
n, s = map(int,input().split())
li = list(map(str, input().split()))
li.sort()
a = []
m = ['a', 'e', 'i', 'o', 'u']
#out
dfs()
for i in range(len(a)):
    a[i] = list(a[i])
for i in range(len(a)):
    print(*a[i],sep='')