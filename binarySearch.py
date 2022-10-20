import sys
import io

_INPUT = """\
8 6
1 3 5 7 9 11 13 15
"""
sys.stdin = io.StringIO(_INPUT)

n,k = map(int,input().split())
A = list(map(int,input().split()))
bf = 0
af = n-1
#ans = -1
while(bf <= af):
    if(A[-1]<k):
        af = -10
        break
    middle = int((bf+af)/2)
    #print(bf,af)
    #print("mid: ",A[middle])
    if(A[middle] == k):
        bf = middle
        break
    elif(A[middle] < k):
        bf = middle +1
    elif(A[middle] > k):
        af = middle -1

if(af == -10):
    print(-1)
else:
    ans = A[middle]
    if(ans < k):
        middle +=1
    #print(ans)
    print(middle)
"""
bf = 0
af = n-1
while(bf <= af):
    middle = int((bf+af)/2)
    #print(bf,af)
    #print("mid: ",A[middle])
    if(A[middle] == k):
        bf = middle
        break
    elif(A[middle] < k):
        bf = middle +1
    elif(A[middle] > k):
        af = middle -1
"""