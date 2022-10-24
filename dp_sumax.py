import sys
import io

_INPUT = """\
3
7 -6 9
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int,input().split()))

dp = [0 for i in range(100)]
for i in range(n):
    not_choice = dp[i]
    choice = dp[i] + A[i]
    dp[i+1] = max(not_choice,choice)

print(dp)