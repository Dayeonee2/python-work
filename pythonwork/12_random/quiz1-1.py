from random import randrange 

# 컴퓨터 랜덤값 저장
com = 0;
# 사용자 입력값 저장
user = 0;
# 컴퓨터 가진 랜덤값을 문자열로 출력
comOutput = ["", "가위", "바위", "보"];
# 승, 무, 패
game = [0,0,0];

import os
while True:
    print("#"*30);
    print("#"*8,'가위 바위 보',"#"*8)
    print("#"*30);
    print();
    print("사용자 및 컴퓨터가 먼저 5승 하면 승리합니다.");
    os.system("pause");
    os.system("cls");
    while True:
        # 1 ~ 3 랜덤값 저장
        com = randrange(1,4);
        
        user = int(input("1. 가위 2. 바위 3. 보 : "));
        
        print("-"*30);
        print("컴퓨터 : 사용자");
        print(f"{comOutput[com]} : {comOutput[user]}");
        print(f"{game[0]}승 {game[1]}무 {game[2]}패")
        print("-"*30);

        if user == com:
            print("비겼습니다.");
            game[1]+=1
        elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
            print("사용자가 이겼습니다.");
            game[0]+=1
        elif (user == 1 and com == 2) or (user == 2 and com == 3) or (user == 3 and com == 1):
            print(f"{comOutput[com]} : 컴퓨터가 이겼습니다.");
            game[2]+=1
        print(f"{game[0]}승 {game[1]}무 {game[2]}패")
        
        if game[0]==5:
            print(f"사용자가 5승을 먼저 달성했습니다. 게임을 종료합니다.");
            break;
        elif game[2]==5:
            print(f"컴퓨터가 5승을 먼저 달성했습니다. 게임을 종료합니다.");
            break;
        os.system("pause");
        os.system("cls");

        