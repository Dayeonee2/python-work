#키오스크 만들기 
#제품 출력 - 아메리카노, 카푸치노(Hot), 라떼, 에이드 , 티
#아메리카노- 아이스, 핫
#카푸치노- 핫
#라떼 - 고구마, 바닐라, 슈크림, 녹차, 말차(아이스, 핫)
#에이드- 레몬, 청포도, 딸기, 복숭아
#티-녹차, 아이스티, 얼그레이, 밀크티(아이스, 핫)
#선택- 선택이 완료될때까지 결제 대기
#결제- 현금, 카드(페이류, 카드)
mainmenu= "아메리카노", "카푸치노(Hot)", "라떼" , "에이드" , "티";#아메리카노 3000,카푸치노3500,
purchase = 0;
purchaselist=[]
import os

while True:
    for i in range(len(mainmenu)):
        print(f"{i+1} . {mainmenu[i]}")
    select=input('구매할 음료 번호를 입력하세요 : ');
    print("모든 메뉴 후 0번을 눌러주세요")
    
    if select=='1':
        print("1. Hot(2500원) 2. Cold(3000원) : ");
        select=input('번호를 입력하세요 : ');
        if select=='1':
            purchase+=2500;
            purchaselist.append("아메리카노(Hot)")
        elif select == '2': 
            purchase+=3000;
            purchaselist.append("아메리카노(Cold)")
        else:
            print("제시된 번호를 입력하지 않으셨습니다. 다시 입력해주세요.")
        print("#"*35)
        print("{:^27}".format("장바구니 목록"))
        print("#"*35)   
        for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")               
        os.system("pause");
        os.system("cls");
    elif select == '2':
        print("Hot(3500원)");
        purchase+=3500;
        purchaselist.append("카푸치노(Cold)")
        print("#"*35)
        print("{:^27}".format("장바구니 목록"))
        print("#"*35)
        for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
        os.system("pause");
        os.system("cls");
        
    elif select == '3':
        menu="고구마라떼", "바닐라라떼", "슈크림라떼", "녹차라떼", "말차라떼";
        menu1=list(menu)
        for i in range(len(menu)):
            print(f"{i+1} .  {menu[i]}");
        select =input('음료 번호를 입력하세요 : ')
       
        if select=='1':
            print("1. Hot(3000원) 2. Cold(3500원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=3000;
                purchaselist.append("고구마라떼(Hot)");
            elif choice =='2':
                purchase+=3500;
                purchaselist.append("고구마라떼(Cold)");
            else:
                print('제시된 번호를 입력하세요.')
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
               
        elif select == '2':
            print("1. Hot(3500원) 2. Cold(4000원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=3500;
                purchaselist.append("바닐라라떼(Hot)")
            elif choice =='2':
                purchase+=4000;
                purchaselist.append("바닐라라떼(Cold)");
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
            
        elif select == '3':
            print("1. Hot(5000원) 2. Cold(5000원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=5000;
                purchaselist.append("슈크림라떼(Hot)")
            elif choice =='2':
                purchase+=5000;
                purchaselist.append("슈크림라떼(Cold)")
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
            
        elif select == '4':
            print("1. Hot(3500원) 2. Cold(4000원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=3500;
                purchaselist.append("녹차라떼(Hot)");
            elif choice =='2':
                purchase+=4000;
                purchaselist.append("녹차라떼(Cold)");
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
            
        elif select == '5':
            print("1. Hot(4000원) 2. Cold(4500원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=4000;
                purchaselist.append("말차라떼(Hot)");
            elif choice =='2':
                purchase+=4500;
                purchaselist.append("말차라떼(Cold)");
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
        else:
            print("제시된 번호를 입력하지 않으셨습니다. 다시 입력해주세요.")
        os.system("pause");
        os.system("cls");        
    elif select == '4':
        menu="레몬", "청포도", "딸기", "복숭아";
        menu1=list(menu)
        for i in range(len(menu)):
            print(f"{i+1} .  {menu[i]}");
        select =input('음료 번호를 입력하세요 : ');
       
        if select=='1':
            purchase+=3500;
            purchaselist.append("레몬에이드(Cold)");
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")  
        elif select == '2':
            purchase+=3500;
            purchaselist.append("청포도에이드(Cold)");
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
        elif select == '3':
            purchase+=3500;
            purchaselist.append("딸기에이드(Cold)")
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
        elif select == '4':
            purchase+=3500;
            purchaselist.append("복숭아에이드(Cold)");
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
        else:
            print("제시된 번호를 입력하지 않으셨습니다. 다시 입력해주세요.")
        os.system("pause");
        os.system("cls");
    elif select == '5':
        menu="녹차", "아이스티", "얼그레이", "밀크티";
        menu1=list(menu)
        for i in range(len(menu)):
            print(f"{i+1} .  {menu[i]}");
        select =input('음료 번호를 입력하세요 : ')
       
        if select=='1':
            print("1. Hot(2500원) 2. Cold(3000원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=2500;
                purchaselist.append("녹차(Hot)");
            elif choice =='2':
                purchase+=3000;
                purchaselist.append("녹차(Cold)");
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
               
        elif select == '2':
            print("1. Hot(1000원) 2. Cold(1500원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=1000;
                purchaselist.append("아이스티(Hot)")
            elif choice =='2':
                purchase+=1500;
                purchaselist.append("아이스티(Cold)");
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
            
        elif select == '3':
            print("1. Hot(3500원) 2. Cold(4000원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=3500;
                purchaselist.append("얼그레이(Hot)")
            elif choice =='2':
                purchase+=4000;
                purchaselist.append("얼그레이Cold)")
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
            
        elif select == '4':
            print("1. Hot(4500원) 2. Cold(5000원) : ");
            choice = input('번호를 입력하세요 : ');
            if choice == '1':
                purchase+=4500;
                purchaselist.append("밀크티(Hot)");
            elif choice =='2':
                purchase+=5000;
                purchaselist.append("밀크티(Cold)");
            else:
                print('제시된 번호를 입력하세요.');
            print("#"*35)
            print("{:^27}".format("장바구니 목록"))
            print("#"*35)
            for i in range(len(purchaselist)):
                if purchaselist[i-1]==purchaselist[i] and i>0:
                    pass;
                else:
                    print(f"{purchaselist[i]} - {purchaselist.count(purchaselist[i])} 개")
            
        else:
            print("제시된 번호를 입력하지 않으셨습니다. 다시 입력해주세요.")
        os.system("pause");
        os.system("cls");
    elif select =='0':
        choice=input(f"총 금액은 {purchase} 원 입니다. 결제하시겠습니까? (y/n) : ")
        if choice.lower() == 'n':
            continue;
        elif choice.lower() == 'y':
            print("1. 카드(카카오페이, 신용카드) 2. 현금 ");
            method=input("결제하실 수단을 선택하세요 : ");
            if method =='1':
                print("카드를 삽입해주세요.");
                print(f"{purchase} 원 결제되었습니다.");
                
            elif method =='2':
                money=0;
                while True:
                    money1=input("현금을 투입하세요 : ")
                    if money1.isdigit():
                        money+=int(money1);
                        if int(money)> purchase:
                            print(f"{purchase} 원 결제돼서 잔액은 {int(money)-purchase} 원 입니다.");
                            break;
                        elif int(money)==purchase:
                            print(f"{purchase} 원 결제되었습니다.");
                            break;
                        else:
                            print("잔돈을 더 투입해주세요.");
                            continue;
            break;
        else:
            print('잘못 입력하셨습니다.')                   
    else:
        print("제시된 번호를 입력하지 않으셨습니다. 다시 입력해주세요.")

        
        

    