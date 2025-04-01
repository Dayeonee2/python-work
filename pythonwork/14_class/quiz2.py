# 문제 
# quiz1.py에 있는 전화번호부를 좀 더 기능을 추가한다.
# 1. 전화번호부 등록 -> quiz1
# 2. 전화번호부 수정 -> class 에서 만들어야 함
# 3. 전화번호부 삭제 -> phonebook_list
# 4. 전화번호부 검색 -> main 에서 만들어야 함
# 5. 전화번호부 전체 출력 -> quiz1
# 6. 전화번호부 초기화  > phonebook_list

class PhoneBook:
    name = '';
    telnum = '';
    email = '';

    def init(self): # 등록
        self.name = input("이름 입력 : ");
        self.telnum = input("전화번호 입력 : ");
        self.email = input("이메일 입력 : ");
    
    def modify(self): # 수정
        self.name = input("이름 입력 : ");
        self.telnum = input("전화번호 입력 : ");
        self.email = input("이메일 입력 : ");
    
    def output(self): # 출력
        print(f"#### {self.name} ####")
        print(f"전화전호 : {self.telnum}");
        print(f"이메일 : {self.email}");

# 객체 저장
phonebook_list = [];

def func(sub):
    print(f"### 전화번호 {sub} ###");
    name = input(f"{sub}할 이름 입력 : ");

    b = True;
    for i in range(len(phonebook_list)):
        if phonebook_list[i].name == name:
            print(f"{i+1}. {phonebook_list[i].name}");
            phonebook_list[i].output();
            b = False;
    if b:
        print(f"{name} 을 찾을 수 없습니다.");
    else:
        idx = input("등록 번호 입력 : ");
        return int(idx)-1;

menu = "등록", "수정", "삭제", "검색", "전체 출력", "초기화";
while True:
    for i in range(len(menu)):
        print(f"{i+1}. 전화번호 {menu[i]}");
    print("0. 종료");
    select = input("메뉴 선택 : ");

    if select == "1":
        print("### 전화번호 등록 ###");
        p = PhoneBook();
        p.init();
        phonebook_list.append(p);
    elif select == "2":
        idx = func("수정");
        if idx != None:
            phonebook_list[idx].modify();
    elif select == "3":
        idx = func("삭제");
        if idx != None :
            phonebook_list.pop(idx);
    elif select == "4":
        idx = func("검색");
        if idx != None:
            phonebook_list[idx].output();
    elif select == "5":
        print("### 전화번호 전체 출력 ###");
        for i in range(len(phonebook_list)):
            print(f"{i+1}. {phonebook_list[i].name}");
            phonebook_list[i].output();
    elif select == "6":
        print("전화번호를 초기화 합니다.");
        phonebook_list.clear();
    elif select == "0":
        print("프로그램 종료");
        break;
    else:
        print("없는 메뉴 번호 입니다.");