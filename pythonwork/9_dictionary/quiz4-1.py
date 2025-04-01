import os

navi={};
key=1;
menu='등록','목적지 수정','검색','주소 검색','종료';
while True:
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    select= input("메뉴 번호 입력 : ");
    if select=='1':
        name=input('목적지 이름 입력 : ');
        value = list(navi.values()); #왜 이차원list인지
        
        for i in range(len(value)):
            if name == value[i][0]:
                print("f{name} 목적지는 이미 등록되었습니다.");
                break;
        else:  
            address=input('주소 입력 : ');
            navi[key]=[name,address]
            key+=1
            print(f'{name} 목적지를 등록했습니다.')      
    elif select=='2':
        print("##### 목적지 수정 #####")
        print("수정할 메뉴를 선택하세요.");
        submenu = input("1. 목적지 이름 2. 목적지 주소 : ");
        
        if submenu=='1':
            print("##### 목적지 수정 #####")
            name=input('수정할 목적지 입력 : ');
        
            keys = list(navi.keys());
            value = list(navi.values());

            for i in range(len(value)):
                if name == value[i][0]:
                    changename= input("수정할 목적지 이름 입력 : ");
                    navi[key[i]] = [changename,value[i][1]]
                    print(f"{name} 목적지 주소를 {changename} 로 변경했습니다.");
                    break;
            else:  
                print(f"{name} 목적지가 등록되어 있지 않습니다."); 
        
        elif submenu=='2':
            print("#### 목적지 주소 수정 ####")
            name = input("수정할 목적지 이름 입력 : ");
            
            keys = list(navi.keys());
            value = list(navi.values());

            for i in range(len(value)):
                if name == value[i][0]:
                    address = input("수정할 목적지 주소 입력 : ");
                    navi[keys[i]] = [name, address];
                    print(f"{name} 목적지 주소를 {address} 로 변경했습니다.");
                    break;
            else:
                print(f"{name} 목적지가 등록되어 있지 않습니다."); 
        
    elif select=='3':
        name = input("검색할 목적지 이름 입력 : ");

        value = list(navi.values());
        for i in range(len(value)):
            if name == value[i][0]:
                print(f"{name} 목적지의 주소는 {value[i][1]} 입니다.")
                break;
        else:
            print(f"{name} 목적지는 등록되어 있지 않습니다.");
        
    elif select=='4':
        keyword= input('주소 검색 입력 : ');
        
        value = list(navi.values());
        b=True
        for i in range(len(value)):
            if keyword in value[i][1]:
                print(f"{i+1}. {value[i][0]} : {value[i][1]}");
                b=False;
        if b:
            print(f"{keyword}와 유사한 주소는 없습니다.")
                
        
        
    elif select=='5':
        value=list(navi.values())
        keys = list(navi.keys());
        if len(value)==0:
            print("등록된 주소가 없습니다.")
        else:
            print("#####전체 주소 출력#####");
            for i in range(len(value)):
                print(f"{keys[i]}. {value[i][0]} : {value[i][1]}");
        print('종료합니다.')
        break;
    else:
        print('제시된 번호를 입력하세요.')
    os.system('pause');
    os.system('cls')
        