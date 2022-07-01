import sys
from itertools import combinations
input = sys.stdin.readline
#fun
def max_num(num_li,idx,n,k):
    answer = []
    for i in range(n):
        while idx > 0  and answer and answer[-1] < num_li[i]:
            answer.pop()
            idx -= 1
        answer.append(num_li[i])
    print(answer)
    result = int(''.join(answer[:]))
    return result
#in
n, k = map(int,input().split())
num_li = list(input())
idx = k
#out
print (max_num(num_li,idx,n,k))