# 3 6 9 게임 369 는 짝으로 대체

for i in range(1,1000):
    hundred = i//100; #백단위 0~9
    ten=(i-hundred*100)//10; # 십단위 0~9
    one=i%10; # 일단위 0~9
    if hundred%3 ==0  and hundred != 0:
        print('짝', end='')
    else:
        if hundred !=0: 
            print(hundred, end='')
    if ten%3 ==0  and ten != 0:
        print('짝', end='')
    else:
        if ten != 0 or hundred >0:
            print(ten, end='')
    if one%3 ==0 and one != 0:
        print('짝')
    else:
        print(one)

