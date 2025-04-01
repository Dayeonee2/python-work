navi={};
menu='등록','목적지 수정','검색','종료';
while True:
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    select= input("메뉴 번호 입력 : ");
    if select=='1':
        name=input('목적지 이름 입력 : ');
        if navi.get(name)!=None:
           print(f"{name} 목적지가 존재합니다. 수정메뉴에서 수정하세요.") 
        else:    
            address=input('주소 입력 : ');
            navi[name]=address       
    elif select=='2':
        name=input('수정할 목적지 입력 : ');
        if navi.get(name)!=None:
            navi[name]=input('수정할 주소 입력 : ');
        else:    
            print(f"{name} 목적지가 존재하지 않습니다.목적지를 등록해주세요.")
        
    elif select=='3':
        if len(navi)==0:
            print('저장된 주소록이 없습니다.')
        else:
            name=input('검색할 목적지 입력 : ');
            if name in navi:
                print(f'주소는 {navi[name]}이다.')
            else:
                print('저장된 목적지가 없습니다.')
        
    elif select=='4':
        print('종료합니다.')
        break;
    else:
        print('제시된 번호를 입력하세요.')
        