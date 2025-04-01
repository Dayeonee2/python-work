navi={};
menu='등록','목적지 수정','검색','종료';

def menuOutput():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    select= input("메뉴 번호 입력 : ");
    return select;
    
def add():
    name=nameInput("등록","주소");
    if navi.get(name)!=None:
        print(f"{name} 목적지가 존재합니다. 수정메뉴에서 수정하세요.") 
    else:    
        address=input('주소 입력 : ');
        navi[name]=address
    
def modify():
    name=nameInput("수정","주소");
    if navi.get(name)!=None:
        navi[name]=input('수정할 주소 입력 : ');
    else:    
        print(f"{name} 목적지가 존재하지 않습니다.목적지를 등록해주세요.")
    
def find():
    if len(navi)==0:
        print('저장된 주소록이 없습니다.')
    else:
        name=nameInput("검색","주소");
        if name in navi:
            print(f'주소는 {navi[name]}이다.')
        else:
            print('저장된 목적지가 없습니다.')

def nameInput(sub1, sub2= "이름"):
    print(f"#### 목적지 {sub1} ####");
    name= input(f"{sub1}할 목적지 {sub2} 입력 :")
    return name

while True:
    select=menuOutput();
    
    menuList= [add, modify, find];
    if select.isdigit() and (1 <= int(select) <4):
        menuList[int(select)-1]();
    elif select=='4':
        print('종료합니다.')
        break;
    else:
        print('제시된 번호를 입력하세요.')
        