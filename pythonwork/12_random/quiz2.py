from random import randrange

lotto=[]

def show(lotto):
    for i in range(len(lotto)):
        print(f"{i+1}번 숫자 : {lotto[i]}")

while len(lotto)!=6:
    num=randrange(1,46);
    if num in lotto:
        pass
    else:
        lotto.append(num);

show(lotto);
    