
while True:
    qq=int(input('10~ 20 사이의 수를 입력하세요 :'));
    if 10<=qq<=20:
        break;
    else:
        print('잘못입력하셨습니다.')
t=0;
sum=0;
while 10<=qq<=20:
    t+=1;
    sum+=t;
    if t==qq:            
        print(sum);           
        break
