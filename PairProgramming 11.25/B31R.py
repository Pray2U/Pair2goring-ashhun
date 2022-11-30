# 사용자 컴퓨터 -> 인풋 1~3 31아웃

import random

def computer(n, mu):
    x = random.randrange(1, 3)
    for i in range(1, x+1):
        if n + i > 31:
            break
        print(f"컴퓨터 {n + i}") # f-string
    n = n + x
    if n >= mu:
        print("computer 짐")
        return
    player(n, mu)

def player(n, mu):
    t = (mu-n-1) % 4
    for i in range(1, t+1):
        print(f"플레이어 {n + i}") # f-string
    n = n + t
    if n >= mu:
        print("player 짐")
        return
    computer(n, mu)


bas=0
m = int(input("몇개 완? "))
player(bas, m)

