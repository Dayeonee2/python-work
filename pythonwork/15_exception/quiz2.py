# 문제 
# 회사 인사 관련 프로그램
# 직책 : 사장, 이사, 부장, 과장, 대리, 사원
# 임직원 : 이름, 주민번호, 이메일, 전화번호
# 인사 등록, 인사 수정, 인사 삭제, 인사 검색
# 등록시 : 이름, 주민번호, 이메일, 전화번호, 직책 등록
# 수정시 : 이름만, 주민번호만, 이메일만, 전화번호만, 직책만 수정가능하도록 
# 삭제 : 인사 정보 삭제
# 검색 : 이름 검색, 전체 검색
# try ~ except 사용 해 볼 것
class Company:
    def __init__(self):
        self.name = input("이름 입력 : ");
        self.jumin = input("주민번호 입력 : ");
        self.email = input("이메일 입력 : ");
        self.phone = input("전화번호 입력 : ");
        self.grade = input("직책 입력 : ");

    def __str__(self):
        out = f"## {self.name} {self.grade} ##\n";
        out += f"주민번호 : {self.jumin}\n";
        out += f"이메일 : {self.email}\n";
        out += f"전화번호 : {self.phone}\n";
        return out;

    def modifyName(self,name):
        self.name = name;
    def modifyJumin(self,jumin):
        self.jumin = jumin;
    def modifyEmail(self,email):
        self.email = email;
    def modifyPhone(self,phone):
        self.phone = phone;
    def modifyGrade(self,grade):
        self.grade = grade;
        
    def find(self, name):
        if self.name == name:
            return True;
        else:
            return False;  

company=[];
        
while True:
    print("1. 인사정보등록");
    print("2. 인사정보수정");
    print("3. 인사정보삭제");
    print("4. 인사정보검색");
    print("0. 프로그램 종료");
    select = input("선택 : ");  
    
    if select == "1":
        c = Company();
        company.append(c);
        print("정보 입력이 완료 되었습니다.");
    elif select == "2":
        print("## 인사 정보 수정 ##");
        name = input("수정할 이름 입력 : ");
        
        for i in range(len(company)):
            if company[i].find(name):
                print(f"{i+1}. {company[i].name} {company[i].grade}")
        num = int(input("번호 입력 : ")); #동명이인
        print("1. 이름");
        print("2. 주민번호");
        print("3. 이메일");
        print("4. 전화번호");
        print("5. 직책");
        
        try:
            subselect = int(input("메뉴 입력 : "));
            
            if subselect == 1:
                company[num-1].modifyName(input("수정할 이름 입력 : "));
            elif subselect == 2:
                company[num-1].modifyJumin(input("수정할 주민번호 입력 : "));
            elif subselect == 3:
                company[num-1].modifyEmail(input("수정할 이메일 입력 : "));
            elif subselect == 4:
                company[num-1].modifyPhone(input("수정할 전화번호 입력 : "));
            elif subselect == 5:
                company[num-1].modifyGrade(input("수정할 직책 입력 : "));
            else:
                raise Exception;
            print("인사 정보 수정이 완료 되었습니다.");
            
        except ValueError:
            print("숫자로 입력하세요.")
            
        except Exception:
            print("없는 메뉴 번호입니다.")
                        
    elif select == "3":
        print("## 인사 정보 삭제 ##");
        name = input("삭제할 이름 입력 : ");
        
        for i in range(len(company)):
            if company[i].find(name):
                print(f"{i+1}. {company[i].name} {company[i].grade}")
                
        num = int(input("번호 입력 : ")); # 동명이인
        company.pop(int(num-1)); #for문을 range로 돌리면 인덱스번호삭제->pop
        
    elif select == "4":
        print("## 인사 정보 검색 ##");
        print("1. 이름 검색");
        print("2. 전체 검색")
        subselect = input("선택 : ");
        if subselect=='1':
            name = input("검색할 이름 입력 : ");
            for i in range(len(company)):
                if company[i].find(name):
                    print(f"{company[i]}")
        elif subselect=='2':
            for i in company:
                print(i);
    elif select == "0":
        print("프로그램을 종료합니다.");
        break;
    else:
        print("선택된 메뉴 번호가 없습니다.");