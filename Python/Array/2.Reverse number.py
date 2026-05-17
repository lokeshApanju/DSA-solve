num = 1432

def revNum(num):
    reve = 0
    while num > 0:
        ld  = num // 10
        reve = reve * 10 + ld 
        num = num % 10
        print(reve, num)

revNum(num)