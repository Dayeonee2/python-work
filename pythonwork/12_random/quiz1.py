from random import random, randrange

def func(com,user): # 컴퓨터와 사용자가 낸 상황 출력
    print()
    print("컴퓨터\t\tvs\t사용자")
    print(f">>{com}\t\t:\t{user}")
    

win=0 # 사용자가 이긴 횟수
winq=0 # 컴퓨터가 이긴 횟수

def winn(): #사용자가 이겼을 때
    global win,winq
    win+=1;
    winq-=1;
    
def winqq(): # 컴퓨터가 이겼을 때
    global win,winq
    win-=1;
    winq+=1;
    

import os    
while True:
    print("########## 가위바위보 ##########")
    print(f"사용자가 이긴 횟수 : {win}")
    print(f"컴퓨터가 이긴 횟수 : {winq}")
    com=randrange(1,4); #1~3 사이의 수를 뽑음

    user=input("가위, 바위, 보 중에 선택하세요: ")

    if user =='가위':
        if com==1:
            com='가위';
            func(com,user);
            print("\n무승부");
        elif com==2:
            com='바위';
            func(com,user);
            print('\n사용자 패');
            winqq();
        elif com==3:
            com='보'
            func(com,user);
            print('\n사용자 승');
            winn();
    elif user =='바위':
        if com==1:
            com='가위';
            func(com,user);
            print('\n사용자 승');
            winn();
        elif com==2:
            com='바위';
            func(com,user);
            print("\n무승부");
        elif com==3:
            com='보';
            func(com,user);
            print('\n사용자 패');
            winqq();
    elif user =='보':
        if com==1:
            com='가위';
            func(com,user);
            print('\n사용자 패');
            winqq();
        elif com==2:
            com='바위';
            func(com,user);
            print("\n무승부");
        elif com==3:
            com='보'
            func(com,user);
            print('사용자 승');
            winn();
    else:
        print("가위, 바위, 보 중에 입력하세요.");
        
    if win==2:
        print(f"\n사용자가 {win} 번 이겼으므로 최종승리입니다.");
        break;
    if winq==2:
        print(f"\n컴퓨터가 {winq} 번 이겼으므로 최종승리입니다.");
        break;
    os.system("pause");
    os.system("cls");


