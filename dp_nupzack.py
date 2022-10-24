from operator import not_
from secrets import choice
import sys
import io

_INPUT = """\
6
2 3
1 2
3 6
2 1
1 3
5 85
9
"""
sys.stdin = io.StringIO(_INPUT)

Weight = []
Value = []
dp = [[0 for i in range(10)]for j in range(10)]
n = int(input())
for i in range(n):
    A = list(map(int,input().split()))
    Weight.append(A[0])
    Value.append(A[1])
w = int(input())
print(Weight,Value)

for i in range(n):
    for j in range(w+1):
        not_choice = dp[i][j]
        if(j >= Weight[i]):
            choice = dp[i][j-Weight[i]] + Value[i]
            dp[i+1][j] = max(not_choice,choice)
        else:        
            dp[i+1][j] = not_choice
print(dp[n][w])