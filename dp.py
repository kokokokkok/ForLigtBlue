from operator import not_
import sys
import io

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)


def sushi_choice(cost_Li,kcal_Li,limit):
    list_len = len(kcal_Li)
    #print(list_len)
    dp = [[0 for i in range(limit+1)]for j in range(list_len)]#横軸は制限数、縦軸は選ぶアイテム数

    for i in range(limit+1):#最初の行はcalが8以上なら食える！ 1からはじめないと、0はなにもできないから
        if(kcal_Li[0] <= i):
            dp[0][i] = cost_Li[0]

    for i in range(1,list_len):#縦軸はその寿司を喰うか、喰わないかなので寿司の数
        for j in range(limit+1):#横軸はcalの限界なので、limitとなる
            not_choice = dp[i-1][j]
            if(j < kcal_Li[i]):#jとkcalが同じときはchoiceしてほしいので、食べられない時で条件をつける
                dp[i][j] = not_choice
            else:
                #寿司iを選ぶ場合は、寿司iのカロリーが食べられる状態のDPに、寿司iを食べたコストを足す
                #この食べられる状態のDPはその制限下での最大値
                choice = dp[i-1][j - kcal_Li[i]] + cost_Li[i]
                dp[i][j] = max(not_choice,choice)
                print(choice,not_choice)
    return dp

cost = [120,150,140,110,100] 
kcal = [8,10,7,6,7] 
ans = sushi_choice(cost,kcal,30)
print(ans)