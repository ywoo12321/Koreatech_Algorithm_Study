import sys
limit_number = 10**7
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline
#fun
def fun_5(n,now):
    global n_li
    global k
    global len_n 
    while True:
        if n_li.count('5') >= k:
	        break
        while n_li[now] == '5' and abs(now) < len_n:
            now -= 1
        answer = int(''.join(n_li))
        answer = answer + 10**(abs(now)-1)
        n_li = list(str(answer)) 
        len_n = len(n_li)
    return int(''.join(n_li))
	 
#in 
n, k = map(int,input().split())
n = n + 1 
n_li = list(str(n))
now = -1
len_n = len(n_li)
#out
print(fun_5(n,now))