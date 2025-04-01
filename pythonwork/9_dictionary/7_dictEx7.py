snack = {};

while True :
    print("1. 메뉴등록");
    print("2. 메뉴별 가격 보기");
    print("3. 가격 수정");
    print("0. 종료");
    select = input("메뉴 선택 : ");

    if select == "1":
        snackName = input("메뉴 입력 : ");
        if snack.get(snackName) != None:
            print(f"{snackName} 메뉴가 존재합니다. 수정메뉴에서 수정하세요.")
        else:
            snack[snackName] = input("가격 입력 : ");
    elif select == "2":
        for i in snack.keys():
            print(f"{i} : {snack[i]}");
    elif select == "3":
        snackName = input("수정할 메뉴 입력 : ");
        if snack.get(snackName) != None:
            snack[snackName] = input("수정할 가격 입력 : ");
        else:
            print(f"{snackName} 메뉴가 없습니다. 메뉴를 등록하세요.")
    elif select == "0":
        print("프로그램 종료");
        break;
    else:
        print("없는 메뉴 번호 입니다.");