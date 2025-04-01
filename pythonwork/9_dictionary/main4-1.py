# 키오스크 - 커피숍
# 제품 - 아메리카노, 카누치노(핫), 라떼, 에이드(아이스), TEA

# 아메리카노 - 아이스, 핫
# 라떼 - 고구마, 바닐라, 슈크림, 녹차, 말차 (아이스, 핫)
# 에이드 - 레몬, 청포도, 딸기, 복숭아
# TEA - 녹차, 아이스티, 얼그레이, 밀크티 (아이스, 핫)

# 선택 - 선택이 완료 될때 까지 결제 대기

# 결제 - 카드(페이류, 신용카드)

##########################################################
# 회원 관리 프로그램
# 학생 정보 관리 프로그램
# 주식 구매 프로그램
# 은행 계좌 프로그램
# 길찾기 
# SNS 검색 프로그램
##########################################################

import os
product = "아메리카노", "라떼", "에이드", "TEA";
shopping = {};
main = "메뉴", "결제", "종료";

while True:
    payment = 0;
    if len(shopping) != 0:
        for i,(k,v) in enumerate(shopping.items()):
            print(f"{i+1}. {k} - {v[1]} 잔");
            payment += v[0] * v[1];
        print(f"총 결제 금액 : {payment}");
    
    for i in range(len(main)):
        print(f"{i+1}. {main[i]}");
    select = input("메뉴 선택 : ");

    if select == "1": # 음료 메뉴 선택
        print("###### 메뉴 선택창 ######");
        for i in range(len(product)):
            print(f"{i+1}. {product[i]}");
        select = input("메뉴 선택 : ");

        if select == "1" : # 아메리카노 선택
            os.system("pause");
            os.system("cls");
            print("### 아메리카노 선택 ###")
            print("1. 아이스 : 2000원");
            print("2. 핫 : 1500원");
            select = input("선택 : ");
            
            if select != "1" and select != "2":
                print("선택된 메뉴 번호가 없습니다.");
            else:
                account = input("수량 입력 : ");
                if select == "1" and account.isdigit():
                    print(f"아메리카노(아이스) : {account} 잔 주문");
                    shopping["아메리카노(아이스)"] = [2000, int(account)];
                elif select == "2" and account.isdigit():
                    print(f"아메리카노(핫) : {account} 잔 주문");
                    shopping["아메리카노(핫)"] = [1500, int(account)];
        elif select == "2" : # 라떼 선택
            # 라떼 - 고구마, 바닐라, 슈크림, 녹차, 말차 (아이스, 핫)
            os.system("pause");
            os.system("cls");
            print("### 라떼 선택 ###");
            print("1. 고구마라떼 : 4000원");
            print("2. 바닐라라떼 : 3500원");
            print("3. 슈크림라떼 : 3800원");
            print("4. 녹차라떼 : 3500원");
            select = input("선택 : ");

            if not select.isdigit() or (int(select) < 1 or int(select) > 4) :
                print("선택된 메뉴 번호가 없습니다.");
            else:
                print("=== 옵션 선택 ===")
                print("1. 아이스");
                print("2. 핫");
                option = input("선택 : ");

                if option != "1" and option != "2":
                    print("선택된 메뉴 번호가 없습니다.");
                else:
                    account = input("수량 입력 : ");

                    if not account.isdigit():
                        print("숫자로 입력해 주세요.");
                    elif select == "1":
                        if option == "1":
                            print(f"고구마라떼(아이스) : {account} 잔 주문");
                            shopping["고구마라떼(아이스)"] = [4000, int(account)];
                        elif option == "2":
                            print(f"고구마라떼(핫) : {account} 잔 주문");
                            shopping["고구마라떼(핫)"] = [4000, int(account)];
                    elif select == "2":
                        if option == "1":
                            print(f"바닐라라떼(아이스) : {account} 잔 주문");
                            shopping["바닐라라떼(아이스)"] = [3500, int(account)];
                        elif option == "2":
                            print(f"바닐라라떼(핫) : {account} 잔 주문");
                            shopping["바닐라라떼(핫)"] = [3500, int(account)];
                    elif select == "3":
                        if option == "1":
                            print(f"슈크림라떼(아이스) : {account} 잔 주문");
                            shopping["슈크림라떼(아이스)"] = [3800, int(account)];
                        elif option == "2":
                            print(f"슈크림라떼(핫) : {account} 잔 주문");
                            shopping["슈크림라떼(핫)"] = [3800, int(account)];
                    elif select == "4":
                        if option == "1":
                            print(f"녹차라떼(아이스) : {account} 잔 주문");
                            shopping["녹차라떼(아이스)"] = [3500, int(account)];
                        elif option == "2":
                            print(f"녹차라떼(핫) : {account} 잔 주문");
                            shopping["녹차라떼(핫)"] = [3500, int(account)];        
        elif select == "3" : # 에이드 선택
            # 에이드 - 레몬, 청포도, 딸기, 복숭아
            os.system("pause");
            os.system("cls");
            print("### 에이드 선택 ###");
            print("1. 레몬에이드 : 4500원");
            print("2. 청포도에이드 : 4500원");
            print("3. 딸기에이드 : 4500원");
            print("4. 복숭아에이드 : 4500원");
            select = input("선택 : ");

            if not select.isdigit() or (int(select) < 1 or int(select) > 4) :
                print("선택된 메뉴 번호가 없습니다.");
            else:
                account = input("수량 입력 : ");
                if select == "1":
                    print(f"레몬에이드 : {account} 잔 주문");
                    shopping["레몬에이드"] = [4500, int(account)];
                elif select == "2":
                    print(f"청포도에이드 : {account} 잔 주문");
                    shopping["청포도에이드"] = [4500, int(account)];
                elif select == "3":
                    print(f"딸기에이드 : {account} 잔 주문");
                    shopping["딸기에이드"] = [4500, int(account)];
                elif select == "4":
                    print(f"복숭아에이드 : {account} 잔 주문");
                    shopping["복숭아에이드"] = [4500, int(account)];
        elif select == "4" : # TEA 선택
            # TEA - 녹차, 아이스티, 얼그레이, 밀크티 (아이스, 핫) 
            os.system("pause");
            os.system("cls");
            print("### TEA 선택 ###");
            print("1. 녹차 : 2800원");
            print("2. 얼그레이 : 2800원");
            print("3. 밀크티 : 2800원");
            print("4. 아이스티 : 3000원");
            select = input("선택 : ");

            if not select.isdigit() or (int(select) < 1 or int(select) > 4) :
                print("선택된 메뉴 번호가 없습니다.");
            else:
                print("=== 옵션 선택 ===")
                print("1. 아이스");
                print("2. 핫");
                option = input("선택 : ");

                if option != "1" and option != "2":
                    print("선택된 메뉴 번호가 없습니다.");
                else:
                    account = input("수량 입력 : ");
                    if select == "1":
                        if option == "1":
                            print(f"녹차(아이스) : {account} 잔 주문");
                            shopping["녹차(아이스)"] = [2800, int(account)];
                        elif option == "2":
                            print(f"녹차(핫) : {account} 잔 주문");
                            shopping["녹차(핫)"] = [2800, int(account)];
                    elif select == "2":
                        if option == "1":
                            print(f"얼그레이(아이스) : {account} 잔 주문");
                            shopping["얼그레이(아이스)"] = [2800, int(account)];
                        elif option == "2":
                            print(f"얼그레이(핫) : {account} 잔 주문");
                            shopping["얼그레이(핫)"] = [2800, int(account)];
                    elif select == "3":
                        if option == "1":
                            print(f"밀크티(아이스) : {account} 잔 주문");
                            shopping["밀크티(아이스)"] = [2800, int(account)];
                        elif option == "2":
                            print(f"밀크티(핫) : {account} 잔 주문");
                            shopping["밀크티(핫)"] = [2800, int(account)];
                    elif select == "4":
                        if option == "1":
                            print(f"아이스티(아이스) : {account} 잔 주문");
                            shopping["아이스티(아이스)"] = [3000, int(account)];
                        elif option == "2":
                            print(f"아이스티는 아이스만 있습니다.");
        else:
            print("없는 메뉴 선택 입니다.");

    elif select == "2" : # 결제 
        # 결제 - 카드(페이류, 신용카드)
        if payment == 0:
            print("결제 금액이 없습니다. 메뉴 선택 후 진행하세요.");
        else:
            print("###### 결제 ######");
            print("1. 삼성페이");
            print("2. 신용카드");
            select = input("선택 : ");

            import time

            if select == "1":
                print(f"총 결제 금액 : {payment} 원");
                print("스마트폰은 결제기에 대주세요");

                for i in range(5,0,-1):
                    print(f"{i} 초 남았습니다.");
                    time.sleep(1); #1초 기다리기

                print("결제가 완료 되었습니다.");
                shopping.clear();
            elif select == "2":
                print(f"총 결제 금액 : {payment} 원");
                print("카드를 결제기 꼽아주세요");

                for i in range(5,0, -1):
                    print(f"{i} 초 남았습니다.");
                    time.sleep(1);
                print("결제가 완료 되었습니다.");
                shopping.clear();
            else:
                print("없는 메뉴 번호 입니다.");
    elif select == "3":
        print("프로그램 종료");
        break;
    else:
        print("없는 메뉴 번호 입니다. 다시 입력 하세요.");
    
    os.system("pause");
    os.system("cls");