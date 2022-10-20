
def dfs(seen,Graph,v):
    seen[v] = True
    for i in range(len(Graph[v])):
        next_v = Graph[v][i]
        if(seen[next_v] == True):
            continue
        dfs(seen,Graph,next_v)


# 以下dfsに必要な変数
seen = [[False for i in range(10)]for i in range(10)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
#-------------------
def dfs_grid(h,w,field):#fieldは2次元配列でもstrでOK
    seen[h][w] = True
    for i in range(4):
        nh = h+dx[i]
        nw = w+dy[i]
        #print(field[nh][nw],nh,nw)
        if(nh<0 or nh>=10 or nw<0 or nw>=10):#範囲外
            #print(field[nh][nw])
            continue
        if(field[nh][nw] == "#"):#壁
            continue
        if(seen[nh][nw]):#訪問済み
            continue
        #print(nh,nw)
        dfs_grid(nh,nw,field)

import sys
import io

_INPUT = """\
10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#...
"""
sys.stdin = io.StringIO(_INPUT)


h,w = map(int,input().split())
G = []
for i in range(h):
    G.append(input())
dfs_grid(0,0,G)
print(seen)

for i in range(10):
    print(seen[i])