import os
filedir = "C:\\20240416\\pythonwork\\17_file\\shop";

# 재고관리-제품등록, 제품출력, 제품검색, 제품 재고 수정
#인덱스,종류,이름,개수
def screenCls():
    os.system("pause");
    os.system("cls");

def fileRead():
    with open(filedir, 'r', encoding="utf-8") as f:
        shop = f.readlines(); # 한줄씩 가져오기
        return shop;
    
def output2(shop_):
    if shop_[3]=='0\n':
        print(f"{shop_[0]} 번. {shop_[2].split("\n")[0]} : 품절")
    else:
        print(f"{shop_[0]} 번. {shop_[2]} : {shop_[3].split("\n")[0]} 개");
    
def output():
    shop = fileRead();
    print("### 제품 목록 ###")
    for i in shop:
        shop_=i.split(",");
        output2(shop_);


def check(sub,select):
    shop = fileRead();
    chance = input(f"검색할 제품 {sub} : ");
    b=True;
    for i in shop:
        shop_=i.split(",");
        if shop_[1]== chance and select == 2:
            output2(shop_);
            b=False;
        elif chance in shop_[2] and select == 3:
            output2(shop_);
            b=False;
        else:
            pass
            
    if b:
        print(f"{chance} 종류는 존재하지 않습니다.")
    

def modify():
    print("### 재고 수정 ###")
    shop = fileRead();
    chgmenu='';
    b=True;
    output()
    name= input("수정할 제품 이름을 입력하세요 : ");
    for i in shop:
        shop_=i.split(",");
        if name == shop_[2]:
            num = int(input("수정할 수량을 입력하세요 : "));
            shop_[3]= num;
            chgmenu +=f"{shop_[0]},{shop_[1]},{shop_[2]},{shop_[3]}\n"
            print("재고가 수정되었습니다.")
            b=False    
        else:
            chgmenu+=i
    if b:        
        print(f"{name} 은 존재하지 않습니다.");
    with open(filedir, 'w', encoding="utf-8") as f:
        f.write(chgmenu);

shop = fileRead();
shopindex = len(shop)+1;
            
while True:
    print("### 쇼핑몰 재고관리 ###");
    print("""
1.제품 등록
2.제품 목록 출력
3.제품 검색
4.재고 수정
0.종료""")
    
    try:
        select = int(input("메뉴 번호 입력 : "));
        screenCls();
        if select == 1:
            some = input("제품 종류 : ");
            name = input("제품 이름 : ");
            num = input("제품 수량 : ");
            if num.isdigit() and int(num)>=0:
                with open(filedir, 'a', encoding="utf-8") as f:
                    f.write(f"{shopindex},{some},{name},{num}\n");
                shopindex+=1;
                print(f" {name} 이(가) 등록되었습니다.");
                
                
            else:
                print("재고는 양수로 입력하세요.")
        elif select == 2:
            choice = input("1. 제품 종류 별 목록 2. 전체 목록 : ");
            if choice == '1':
                check("종류",select);
                          
            elif choice == '2':
                output();
                
            else:
                print("제시된 번호를 입력해주세요.");
                
        elif select == 3:
            check("이름",select)

            
        elif select == 4:
            modify();
            
        elif select == 0:
            print("종료합니다.")
            break;
        
        else:
            raise Exception("제시된 메뉴번호가 아닙니다.");                   
        
    except ValueError:
        print("메뉴 번호를 숫자로 입력하세요")
    except Exception as e: #이걸 지정해줘야 else안의 raise Exception이 실행됨.
        print(e);
    
        
                
                
        