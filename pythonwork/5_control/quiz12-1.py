# while True:
#     charge=int(input("요금(원)을 투입하세요 : "));
#     if charge<200:
#         print('요금을 더 넣어주세요.');
#         continue
#     else:
#         break;
# total=0
# if charge>=200 :
#     print('커피는 200원 입니다.');
#     if charge>=250:
#         print('코코아는 250원 입니다.');
#     while True:
#         choose= input("무엇을 주문하시겠습니까? : ");
#         if choose=='코코아' or choose== '커피':
#             break
#         else:
#             print('다시 입력해주세요.')
#             continue
#     if choose=='코코아' or choose=='커피':
#         if choose== '코코아':
#             total= charge-250;
#         elif choose=='커피':
#             total= charge-200;
#         while True:
#             return1=input('반환하시겠습니까?(네, 아니오) : ');
#             if return1=='네':
#                 print(f'반환된 금액은 {total}입니다.')
#                 break
#             elif return1=='아니오':
#                 print('감사합니다.')
#                 break
#             else:
#                 print('다시 입력해주세요.')
#                 continue



# 메뉴 선택을 저장하는 변수
select = 0;
# 투입된 요금을 저장하는 변수
money = 0;
# main while 을 종료하는 논리 자료 변수
main = True;

#문제 커피 또는 코코아를 선택할 때마다 커피 또는 코코아의 잔량을 1씩 차감

#커피잔량
coffeeCtn = 10;

#코코아 잔량
cocoaCtn = 10;

#컵 잔량
cupCtn = 30 ;

coffeeAccount = 0;
cocoaAccount = 0;
# 문제
# 관리자 메뉴에서 1. 잔량 추가 생성
# 커피, 코코아, 컵 잔량을 추가할 수 있도록 구현
# 최대치 컵은 50, 커피와 코코아는 20으로
while main: # 프로그램을 종료할 때까지 무한 반복
    money= int(input('요금 입력 : '));
    if money == 9876: # 관리자 코드
        # 관리자 메뉴
        while True:
            print("0. 자판기 종료  1. 잔량 추가 2. 판매 수량 및 금액 확인 9. 관리자 메뉴 종료");
            select = int(input("관리자 메뉴 입력 : "));
            if select == 0:
                print("자판기를 종료합니다.");
                main=False;
                break;
            elif select== 9:
                print("관리자 메뉴 종료. 판매 모드로 변경합니다");
                break;
            
            elif select == 1:
                print(f"커피 잔량 : {coffeeCtn} 코코아 잔량 :{cocoaCtn} 컵 잔량 : {cupCtn}")
                while True:
                    print("1. 커피 2. 코코아 3. 컵 0. 관리자 메뉴");
                    sel=int(input('메뉴 입력 :'))
                    if sel==1:
                        coffeeCtn+=int(input('추가할 잔량을 입력하세요 :'));
                        if coffeeCtn>20:
                            print(f'{coffeeCtn-20}만큼 초과했습니다.')
                            print(f'{coffeeCtn-20}만큼 반환합니다.')
                            coffeeCtn = 20;
                            print(f'커피를 {coffeeCtn}만큼 보유하고 있습니다.')
                    elif sel == 2:
                        cocoaCtn+=int(input('추가할 잔량을 입력하세요 :'));
                        if cocoaCtn>20:
                            print(f'{cocoaCtn-20}만큼 초과했습니다.')
                            print(f'{cocoaCtn-20}만큼 반환합니다.')
                            cocoaCtn = 20;
                            print(f'코코아를 {cocoaCtn}만큼 보유하고 있습니다.')
                    elif sel==3:
                        cupCtn+=int(input('추가할 잔량을 입력하세요 :'));
                        if cupCtn>50:
                            print(f'{cupCtn-50}만큼 초과했습니다.')
                            print(f'{cupCtn-50}만큼 반환합니다.')
                            cupCtn = 50;
                            print(f'컵을 {cupCtn}만큼 보유하고 있습니다.')
                    elif sel==0:
                        print('관리자 메뉴로 이동합니다.')
                        break;
                    else:
                        print('잘못된 메뉴 번호입니다. 다시 입력하세요.');
            elif select==2:
                while True:
                    print('1.커피 2. 코코아 3. 총 판매 수량 및 금액 4. 관리자 메뉴')
                    sel=int(input('메뉴 입력 : '));
                    if sel== 1:
                        print(f'커피 판매량 : {coffeeAccount} 판매금액 : {coffeeAccount*200}');
                    elif sel== 2:
                        print(f'코코아 판매량 : {cocoaAccount} 판매금액 : {cocoaAccount*250}');
                    elif sel== 3:
                        print(f'총 판매량 : {coffeeAccount +cocoaAccount} 판매금액 : {coffeeAccount*200 +cocoaAccount*250}');
                    elif sel == 4:
                        print('관리자 메뉴로 이동합니다.');
                        break;
                    else:
                        print('잘못된 메뉴 번호입니다. 다시 입력하세요.');
            elif select == 3:
                print("##### 초기화 #####");
                select = input("초기화 하시겠습까 (y/n) : ");
                if select == "y" or select == "Y":
                    cocoaAccount = 0;
                    coffeeAccount = 0;
                    print('초기화 했습니다.');
                elif select == 'n' or select == 'N':
                    print('초기화를 취소했습니다.')
                else:
                    print('잘못입력하셨습니다.')        
            else:
                print('잘못된 메뉴 번호입니다. 다시 입력하세요.');    
    
    else:
        #자판기 메뉴 선택
        while money>0:
            print(f"잔액 : {money} 원");
            if money>=200 and cupCtn>0:
                print("#"*10,"자판기","#"*10);
                if money>= 200 and coffeeCtn>0:
                    print("1. 커피",end='');
                elif coffeeCtn==0:
                    print("1. 커피(매진)",end='');                 
                if money>=250 and cocoaCtn>0:
                    print("2. 코코아", end='');
                elif cocoaCtn==0:
                    print("3. 코코아 (매진)",end='')
                    
                print("3. 반환 4. 추가 요금 ");
                select = int(input("메뉴 선택 : "));
                if select == 1 and coffeeCtn>0: # 커피를 선택했기 때문에 money에서 200을 뺀다.
                    money -= 200;
                    coffeeCtn-=1
                    cupCtn-=1
                    coffeeAccount+=1
                    print("커피가 나왔습니다.");
                elif select == 2 and cocoaCtn>0: # 코코아 선택했기 때문에 money에서 250을 뺀다.
                    money -= 250;
                    cocoaCtn-=1
                    cupCtn-=1
                    cocoaAccount+=1
                    print("코코아가 나왔습니다.");
                elif select == 3: # money 에 있는 잔액을 0 으로 변경
                    print(f"{money}원을 반환합니다.");
                    money = 0;
                elif select == 4:
                    money+=int(input("추가 요금 입력: "))
                else: # 1 ~ 4 까지의 숫자가 아닐때 출력
                    print("선택된 메뉴 번호가 없습니다.");
            elif cupCtn ==0:
                print(f"컵이 없어 판매가 불가하니 {money}원을 반환합니다.");
                money=0
                break;

            else: 
                print('요금이 부족합니다.');
                choice = input("추가 요금을 투입하시겠습니까? (y/n) :");
                if choice=='y'or choice=='Y':
                    money+= int(input('추가 요금 입력: '));
                elif choice =='n' or choice=='N':
                    print(f'{money}를 반환합니다.');
                    money=0;
                else:
                    print('잘못입력하셨습니다.');
    