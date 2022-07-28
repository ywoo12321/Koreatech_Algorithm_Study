import sys
input = sys.stdin.readline
#fun
def same_freinds(question_list):
    num_same_friend = 0
    return num_same_friend
#in
answer = []
n = int(input().rstrip())
friend_list = list(map(int,input().rstrip()) for _ in range(n-1))
question = int(input().rstrip())
for _ in range (3):
    question_list = list(map(int, input().split()))
    #out
    answer.append(same_freinds(question_list))
