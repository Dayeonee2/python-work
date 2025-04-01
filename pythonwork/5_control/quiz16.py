# 문제 만들어 보세요

# 베스킨라빈스 31 게임 
# 인원수는 2명
# 선 후 공 정하기

# 프로그램 종료를 위한 논리형 변수
main = True;
while main:
    # 선 후공을 저장 하는 변수
    attack = input("선/후공 설정 : ");

    # 사용자가 입력한 횟수 저장
    userCtn = 0;
    # 마지막으로 입력한 숫자 저장
    last = 0;
    # 컴퓨터가 입력한 마지막 숫자
    com = 0;
    # 후공일때 사용자 입력을 위한 조건식
    retire= True;

    while True:
        # 선공일때
        if attack == "선" or attack == "선공":
            robbins = int(input("사용자 - 1 부터 입력 (0:턴넘김) : "));

            # 사용자가 31을 입력했을때
            if robbins == 31:
                print("사용자가 졌습니다.");
                # 게임이 끝나고 재시작 또는 종료 선택
                select = 0;
                while True:
                    select = int(input("1. 재시작 0. 종료 : "));
                    if select == 1 or select == 0:
                        # 선택이 잘 되었을 경우 while 문 종료
                        break;
                    else:
                        print("잘못된 선택 입니다. 다시 선택하세요.");

                # select 가 정상적으로 선택된 경우 재시작 또는 종료 실행
                if select == 1:
                    print("게임을 다시 시작합니다.");
                    break;
                elif select == 0:
                    main = False;
                    print("프로그램을 종료합니다.");
                    break;
            # 값을 입력하지 않고 다음 턴을 넘겼을 때
            elif robbins == 0 and com == last:
                print(f"다음 값은 {last + 1} 부터 입니다. 다시 입력하세요");
                continue;
            # 다음값이 아닌 값이 입력 되었을 때
            elif last + 1 != robbins and robbins != 0:
                print(f"다음 값은 {last + 1} 입니다. 확인해서 다시 입력하세요");
                continue;
            # 턴넘김이 아닐때 
            elif robbins != 0:
                last = robbins;
                userCtn += 1;

            # 컴퓨터가 입력
            if robbins == 0 or userCtn == 3:
                if last == 30 :
                    # 컴퓨터가 질 경우
                    last += 1;
                    print("컴퓨터 - 1 부터 입력 :", last);
                    print("컴퓨터가 졌습니다.");
                else :
                    # 컴퓨터가 가질 수 있는 최적의 수 입력 
                    for i in range(1,4):
                        last+=1;
                        com = last;
                        print("컴퓨터 - 1 부터 입력 :", last);
                        if last == 2 or last%4 == 2:
                            break;
                # 사용자 입력 횟수 초기화
                userCtn = 0;
        # 후공일때
        elif attack == "후" or attack == "후공":
            if retire:
    # 컴퓨터가 입력:
                if last == 30 :
                    # 컴퓨터가 질 경우
                    last += 1;
                    print("컴퓨터 - 1 부터 입력 :", last);
                    print("컴퓨터가 졌습니다.");
                else :
                    # 컴퓨터가 가질 수 있는 최적의 수 입력 
                    for i in range(1,4):
                        last+=1;
                        com = last;
                        print("컴퓨터 - 1 부터 입력 :", last);
                        if last == 2 or last%4 == 2:
                            break;
                # 사용자 입력 횟수 초기화
                userCtn = 0;
                
            robbins = int(input("사용자 - 1 부터 입력 (0:턴넘김) : "));

            # 사용자가 31을 입력했을때
            if robbins == 31:
                print("사용자가 졌습니다.");
                # 게임이 끝나고 재시작 또는 종료 선택
                select = 0;
                while True:
                    select = int(input("1. 재시작 0. 종료 : "));
                    if select == 1 or select == 0:
                        # 선택이 잘 되었을 경우 while 문 종료
                        break;
                    else:
                        print("잘못된 선택 입니다. 다시 선택하세요.");

                # select 가 정상적으로 선택된 경우 재시작 또는 종료 실행
                if select == 1:
                    print("게임을 다시 시작합니다.");
                    break;
                elif select == 0:
                    main = False;
                    print("프로그램을 종료합니다.");
                    break;
            # 값을 입력하지 않고 다음 턴을 넘겼을 때
            elif robbins == 0 and com == last:
                print(f"다음 값은 {last + 1} 부터 입니다. 다시 입력하세요");
                retire=False;
                continue;
            # 다음값이 아닌 값이 입력 되었을 때
            elif last + 1 != robbins and robbins != 0:
                print(f"다음 값은 {last + 1} 입니다. 확인해서 다시 입력하세요");
                retire=False;
                continue;
            # 턴넘김이 아닐때 
            elif robbins != 0:
                last = robbins;
                userCtn += 1;
                retire=False;
            if robbins==0 or userCtn==3:
                retire=True;
        # 잘못 입력 했을 때
        else :
            print("잘 못 입력 하셨습니다. 다시 입력하세요");
            break;
 

 
        
        #후공일때
        #elif attack == '후' or attack == '후공':