navi = {};
menu = "목적지 등록", "목적지 수정", "목적지 검색", "종료";

def inputPlace(sub):
    print(f"#### 목적지 {sub} ####");
    name = input(f"{sub}할 목적지 이름 입력 : ");
    return name;

def getNone(name):
    if navi.get(name) == None:
        return True;
    else:
        return False;

def add(name):
    address = input("목적지 주소 입력 : ");
    navi[name] = address;
    print(f"{name} 목적지를 등록했습니다.");
    
def modify(name):
    address = input("수정할 목적지 주소 입력 : ");
    navi[name] = address;
    print(f"{name} 목적지의 주소를 {address} 로 변경되었습니다.");
    
def find(name):
    print(f"{name} 목적지의 주소는 {navi.get(name)} 입니다.");

while True: 
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}");
    select = input("메뉴 번호 선택 : ");

    if select == "1":
        name = inputPlace("등록");
        if getNone(name):
            add(name)
        else:
            print(f"{name} 목적지는 이미 등록 되었습니다.");
    elif select == "2":
        name = inputPlace("수정");
        if getNone(name):
            print(f"{name} 목적지는 등록되어 있지 않습니다.");
        else :
            modify(name);
    elif select == "3":
        name = inputPlace("검색");
        if getNone(name):
            print(f"{name} 목적지는 등록되어 있지 않습니다.");
        else:
            find(name);
    elif select == "4":
        print("프로그램을 종료합니다.");
        break;
    else:
        print("없는 메뉴 번호 입니다. 다시 입력 하세요");