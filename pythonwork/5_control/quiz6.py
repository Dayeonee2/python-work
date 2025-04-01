# 문제 만들어 보세요

# 베스킨라빈스 31 게임 
# 인원수는 2명
# 선 후 공 정하기

# 프로그램 종료를 위한 논리형 변수
# main = True;
# while main:
#     # 선 후공을 저장 하는 변수
#     attack = input("선/후공 설정 : ");

#     # 사용자가 입력한 횟수 저장
#     userCtn = 0;
#     # 마지막으로 입력한 숫자 저장
#     last = 0;
#     # 컴퓨터가 입력한 마지막 숫자
#     com = 0;
#     # 후공일때 사용자 입력을 위한 조건 변수
#     retire = True;

#     while True:
#         # 선공일때
#         if attack == "선" or attack == "선공":
#             robbins = int(input("사용자 - 1 부터 입력 (0:턴넘김) : "));

#             # 사용자가 31을 입력했을때
#             if robbins == 31:
#                 print("사용자가 졌습니다.");
#                 # 게임이 끝나고 재시작 또는 종료 선택
#                 select = 0;
#                 while True:
#                     select = int(input("1. 재시작 0. 종료 : "));
#                     if select == 1 or select == 0:
#                         # 선택이 잘 되었을 경우 while 문 종료
#                         break;
#                     else:
#                         print("잘못된 선택 입니다. 다시 선택하세요.");

#                 # select 가 정상적으로 선택된 경우 재시작 또는 종료 실행
#                 if select == 1:
#                     print("게임을 다시 시작합니다.");
#                     break;
#                 elif select == 0:
#                     main = False;
#                     print("프로그램을 종료합니다.");
#                     break;
#             # 값을 입력하지 않고 다음 턴을 넘겼을 때
#             elif robbins == 0 and com == last:
#                 print(f"다음 값은 {last + 1} 부터 입니다. 다시 입력하세요");
#                 continue;
#             # 다음값이 아닌 값이 입력 되었을 때
#             elif last + 1 != robbins and robbins != 0:
#                 print(f"다음 값은 {last + 1} 입니다. 확인해서 다시 입력하세요");
#                 continue;
#             # 턴넘김이 아닐때 
#             elif robbins != 0:
#                 last = robbins;
#                 userCtn += 1;

#             # 컴퓨터가 입력
#             if robbins == 0 or userCtn == 3:
#                 if last == 30 :
#                     # 컴퓨터가 질 경우
#                     last += 1;
#                     print("컴퓨터 - 1 부터 입력 :", last);
#                     print("컴퓨터가 졌습니다.");
#                 else :
#                     # 컴퓨터가 가질 수 있는 최적의 수 입력 
#                     for i in range(1,4):
#                         last+=1;
#                         com = last;
#                         print("컴퓨터 - 1 부터 입력 :", last);
#                         if last == 2 or last%4 == 2:
#                             break;
#                 # 사용자 입력 횟수 초기화
#                 userCtn = 0;
#         # 후공일때
#         elif attack == "후" or attack == "후공":
#             # 컴퓨터가 입력
#             if retire:
#                 if last == 30 :
#                     # 컴퓨터가 질 경우
#                     last += 1;
#                     print("컴퓨터 - 1 부터 입력 :", last);
#                     print("컴퓨터가 졌습니다.");
#                 else :
#                     # 컴퓨터가 가질 수 있는 최적의 수 입력 
#                     for i in range(1,4):
#                         last+=1;
#                         com = last;
#                         print("컴퓨터 - 1 부터 입력 :", last);
#                         if last == 2 or last%4 == 2:
#                             break;
#                 # 사용자 입력 횟수 초기화
#                 userCtn = 0;

#             robbins = int(input("사용자 - 1 부터 입력 (0:턴넘김) : "));

#             # 사용자가 31을 입력했을때
#             if robbins == 31:
#                 print("사용자가 졌습니다.");
#                 # 게임이 끝나고 재시작 또는 종료 선택
#                 select = 0;
#                 while True:
#                     select = int(input("1. 재시작 0. 종료 : "));
#                     if select == 1 or select == 0:
#                         # 선택이 잘 되었을 경우 while 문 종료
#                         break;
#                     else:
#                         print("잘못된 선택 입니다. 다시 선택하세요.");

#                 # select 가 정상적으로 선택된 경우 재시작 또는 종료 실행
#                 if select == 1:
#                     print("게임을 다시 시작합니다.");
#                     break;
#                 elif select == 0:
#                     main = False;
#                     print("프로그램을 종료합니다.");
#                     break;
#             # 값을 입력하지 않고 다음 턴을 넘겼을 때
#             elif robbins == 0 and com == last:
#                 print(f"다음 값은 {last + 1} 부터 입니다. 다시 입력하세요");
#                 retire = False;
#                 continue;
#             # 다음값이 아닌 값이 입력 되었을 때
#             elif last + 1 != robbins and robbins != 0:
#                 print(f"다음 값은 {last + 1} 입니다. 확인해서 다시 입력하세요");
#                 retire = False;
#                 continue;
#             # 턴넘김이 아닐때 
#             elif robbins != 0:
#                 last = robbins;
#                 userCtn += 1;
#                 retire = False;
#             if robbins == 0 or userCtn == 3:
#                 retire = True;
#         # 잘못 입력 했을 때
#         else :
#             print("잘 못 입력 하셨습니다. 다시 입력하세요");
#             break;


# main = True;
# while main:
#     # 선 후공을 저장 하는 변수
#     attack = input("선/후공 설정 : ");

#     # 사용자가 입력한 횟수 저장
#     userCtn = 0;
#     # 마지막으로 입력한 숫자 저장
#     last = 0;
#     # 컴퓨터가 입력한 마지막 숫자
#     com = 0;
#     # 후공일때 사용자 입력을 위한 조건 변수
#     retire = True;
#     # 게임 재시작 및 종료 선택 저장 변수
#     select = 100;
#     while True:
#         # 선공일때
#         if attack == "선" or attack == "선공":
#             robbins = int(input("사용자 - 1 부터 입력 (0:턴넘김) : "));

#             # 사용자가 31을 입력했을때
#             if robbins == 31:
#                 print("사용자가 졌습니다.");
#                 # 게임이 끝나고 재시작 또는 종료 선택
#                 while True:
#                     select = int(input("1. 재시작 0. 종료 : "));
#                     if select == 1 or select == 0:
#                         # 선택이 잘 되었을 경우 while 문 종료
#                         break;
#                     else:
#                         print("잘못된 선택 입니다. 다시 선택하세요.");

#                 # select 가 정상적으로 선택된 경우 재시작 또는 종료 실행
#                 if select == 1:
#                     print("게임을 다시 시작합니다.");
#                     break;
#                 elif select == 0:
#                     main = False;
#                     print("프로그램을 종료합니다.");
#                     break;
#             # 값을 입력하지 않고 다음 턴을 넘겼을 때
#             elif robbins == 0 and com == last:
#                 print(f"다음 값은 {last + 1} 부터 입니다. 다시 입력하세요");
#                 continue;
#             # 다음값이 아닌 값이 입력 되었을 때
#             elif last + 1 != robbins and robbins != 0:
#                 print(f"다음 값은 {last + 1} 입니다. 확인해서 다시 입력하세요");
#                 continue;
#             # 턴넘김이 아닐때 
#             elif robbins != 0:
#                 last = robbins;
#                 userCtn += 1;

#             # 컴퓨터가 입력
#             if robbins == 0 or userCtn == 3:
#                 if last == 30 :
#                     # 컴퓨터가 질 경우
#                     last += 1;
#                     print("컴퓨터 - 1 부터 입력 :", last);
#                     print("컴퓨터가 졌습니다.");
#                 else :
#                     # 컴퓨터가 가질 수 있는 최적의 수 입력 
#                     for i in range(1,4):
#                         last+=1;
#                         com = last;
#                         print("컴퓨터 - 1 부터 입력 :", last);
#                         if last == 2 or last%4 == 2:
#                             break;
#                 # 사용자 입력 횟수 초기화
#                 userCtn = 0;
#         # 후공일때
#         elif attack == "후" or attack == "후공":
#             # 컴퓨터가 입력
#             if last == 30 :
#                 # 컴퓨터가 질 경우
#                 last += 1;
#                 print("컴퓨터 - 1 부터 입력 :", last);
#                 print("컴퓨터가 졌습니다.");
#             else :
#                 # 컴퓨터가 가질 수 있는 최적의 수 입력 
#                 for i in range(1,4):
#                     last+=1;
#                     com = last;
#                     print("컴퓨터 - 1 부터 입력 :", last);
#                     if last == 2 or last%4 == 2:
#                         break;
#             # 사용자 입력 횟수 초기화
#             userCtn = 0;

#             while True:
#                 robbins = int(input("사용자 - 1 부터 입력 (0:턴넘김) : "));

#                 # 사용자가 31을 입력했을때
#                 if robbins == 31:
#                     print("사용자가 졌습니다.");
#                     # 게임이 끝나고 재시작 또는 종료 선택
#                     select = 0;
#                     while True:
#                         select = int(input("1. 재시작 0. 종료 : "));
#                         if select == 1 or select == 0:
#                             # 선택이 잘 되었을 경우 while 문 종료
#                             break;
#                         else:
#                             print("잘못된 선택 입니다. 다시 선택하세요.");
#                     break;
#                 # 값을 입력하지 않고 다음 턴을 넘겼을 때
#                 elif robbins == 0 and com == last:
#                     print(f"다음 값은 {last + 1} 부터 입니다. 다시 입력하세요");
#                     continue;
#                 # 다음값이 아닌 값이 입력 되었을 때
#                 elif last + 1 != robbins and robbins != 0:
#                     print(f"다음 값은 {last + 1} 입니다. 확인해서 다시 입력하세요");
#                     continue;
#                 # 턴넘김이 아닐때 
#                 elif robbins != 0:
#                     last = robbins;
#                     userCtn += 1;
#                 if robbins == 0 or userCtn == 3:
#                     break;
#             # select 가 정상적으로 선택된 경우 재시작 또는 종료 실행
#             if select == 1:
#                 print("게임을 다시 시작합니다.");
#                 break;
#             elif select == 0:
#                 main = False;
#                 print("프로그램을 종료합니다.");
#                 break;
#         # 잘못 입력 했을 때
#         else :
#             print("잘 못 입력 하셨습니다. 다시 입력하세요");
#             break;
################################

# 눈치 게임
# 인원수 정하기
# 숫자 범위 지정
# 각 인원이 숫자를 입력해서 제일 큰수 이기는 게임
# 높은 숫자 중가 중복되면 다음 숫자가 이긴다.

# inwon = int(input("인원 정하기 : "));
# numRange = int(input("숫자 범위 정하기 : "));
# arr = [];
# for i in range(inwon, 0, -1):
#     arr.append(int(input(f"{numRange} 안의 숫자 입력 : ")));

# index = 1;
# for i in range(numRange, 0, -1):
#     win = arr.count(i);
#     if win == 1:
#         print(f"{arr.index(i)} 님의 {i} 의 값이 제일 높아 우승 했습니다.");
#         break;
#     if win >= 2:
#         print(f"{i} 의 값이 제일 높지만 중복 되어 우승을 놓쳤습니다.")
    
inwon = 5;
num1,num2,num3,num4,num5=0,0,0,0,0;
numRange = int(input("입력할 숫자의 범위 입력 : "));

num1 = int(input(f"{numRange} 안의 수 입력 : "));
num2 = int(input(f"{numRange} 안의 수 입력 : "));
num3 = int(input(f"{numRange} 안의 수 입력 : "));
num4 = int(input(f"{numRange} 안의 수 입력 : "));
num5 = int(input(f"{numRange} 안의 수 입력 : "));

max = 0;
dup = 0;
cnt = 0;

if num1 > num2 or num1 > num3 or num1 > num4 or num1 > num5:
    if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
        if dup < num1:
            dup = num1;
    else :
        if max < num1:
            max = num1;
            cnt = 1;
if num2 > num1 or num2 > num3 or num2 > num4 or num2 > num5:
    if num1 == num2 or num2 == num3 or num2 == num4 or num2 == num5:
        if dup < num2:
            dup = num2;
    else :
        if max < num2:
            max = num2;
            cnt = 2;
if num3 > num1 or num3 > num2 or num3 > num4 or num3 > num5:
    if num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
        if dup < num3:
            dup = num3;
    else :
        if max < num3:
            max = num3;
            cnt = 3;
if num4 > num1 or num4 > num3 or num4 > num2 or num4 > num5:
    if num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
        if dup < num4:
            dup = num4;
    else :
        if max < num4:
            max = num4;
            cnt = 4;
if num5 > num1 or num5 > num2 or num5 > num3 or num5 > num4:
    if num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
        if dup < num5:
            dup = num5;
    else :
        if max < num5:
            max = num5;
            cnt = 5;

if dup > max :
    print(f"{dup} 는 중복되어 우승에 실패했습니다.");
print(f"{cnt} 번님이 {max} 로 우승했습니다.");