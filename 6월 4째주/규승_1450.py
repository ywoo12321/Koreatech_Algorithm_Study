import sys
from itertools import combinations
input = sys.stdin.readline
#fun
def nepsack(maxWeight, weight, numberOfThings):
    front_weight = weight[:numberOfThings//2]
    back_weight = weight[numberOfThings//2:]
    sum_front = []
    sum_back = []
    for i in range(len(front_weight) + 1):
        comb_front = combinations(front_weight, i)
        for comb in comb_front:
            sum_front.append(sum(comb))
    for i in range(len(back_weight) + 1):
        comb_back = combinations(back_weight, i)
        for comb in comb_back:
            sum_back.append(sum(comb))
    sum_front.sort()
    
    ans = 0
    for element_back in sum_back:
        if element_back > maxWeight:
            continue
        start = 0
        end = len(sum_front) - 1
        while start <= end:
            mid = (start + end) // 2
            if sum_front[mid] + element_back > maxWeight:
                end = mid - 1
            else:
                start = mid + 1
        ans += end + 1
    print(ans)
#in
numberOfThings, maxWeight = map(int, input().split())
weight = list(map(int,input().split()))
#out
nepsack(maxWeight, weight, numberOfThings)