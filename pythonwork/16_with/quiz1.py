#문제
#회사 인사 관련 프로그램
# 직책 : 사장, 이사, 부장, 과장, 대리, 사원
# 임직원 : 이름, 주민번호, 이메일, 전화번호
# 인사 등록, 인사 수정, 인사 삭제, 인사 검색
# 등록시 : 이름, 주민번호, 이메일, 전화번호 등록
# 수정시, 이름만, 주민번호만, 이메일만, 전화번호만, 직책만 수정가능하도록
# 삭제 : 인사 정보 삭제
# 검색 : 이름 검색, 전체 검색
# try ~ except 사용 해 볼 것
# class 객체에 저장 이름, 주민번호, 이메일, 전화번호

mode =["","사장", "이사", "부장", "과장", "대리", "사원"];

user=[]; #객체 받을 리스트 직책,이름+직책,주민,이메일,전화

main=True;
 
class Work():
    def digitcheck(self,sub):
        while True:
            try:
                some = int(input(f"{sub} 입력 : "));
                return int(some);
                main=False;
            except ValueError as e:
                print('숫자로 입력하세요.');    
    
    def __init__(self,mode):
        self.name = input("이름 입력 : ");
        self.jj=mode #직책
        self.jumin = self.digitcheck("주민 번호");
        self.email = input("이메일 입력 : ");
        self.number = self.digitcheck("전화 번호");
        
    def __str__(self):
        return f"""
이름 :{self.name} {self.jj}
주민 번호 : {self.jumin}
이메일 : {self.email}
전화 번호 : {self.number}""";
    
    def modifyName(self,name):
        self.name = name;
    def modifyJumin(self,jumin):
        self.jumin = jumin;
    def modifyEmail(self,email):
        self.email = email;
    def modifyPhone(self,number):
        self.number = number;
    def modifyjj(self,jj):
        self.jj = jj;
        
                  
def func(select):
    print(f"### 인사{sub[select-2]} ###");
    name= input("이름 입력 : ");
    for i in range(len(user)):
        if name == user[i].name:
            return i
    else:
        print(f"{name} 님은 존재하지 않습니다.")                       
            
menu = "1. 인사 등록", "2. 인사 수정", "3. 인사 삭제", "4. 인사 검색";

while True:
    for i in menu:
        print(i);
    print("0. 종료")
    sub = '수정','삭제','검색'
    try:
        select = int(input("메뉴 입력 : "));
        if select == 1:
            for i in range(len(mode)):
                if i>=1:
                    print(f"{i}. {mode[i]}")
            choice = input("등록할 사람의 직책 선택 : ");
            if 1<= int(choice) <= 6:
                w=Work(mode[int(choice)]);
                user.append(w);
                print(user);              
            else:
                print("제시된 메뉴 번호를 입력하세요.")

        elif select ==2:
            k=func(select)
            if k!=None:
                print(user[k])
                sup=["이름","주민 번호","이메일","전화 번호","직책"]
                for i in range(len(sup)):
                    print(f"{i+1}. {sup[i]}")
                try:
                    choice = int(input("수정할 메뉴 입력:"))
                    if choice == 1:
                        user[k].modifyName(input("수정할 이름 입력 : "));
                    elif choice == 2:
                        user[k].modifyJumin(input("수정할 주민번호 입력 : "));
                    elif choice == 3:
                        user[k].modifyEmail(input("수정할 이메일 입력 : "));
                    elif choice == 4:
                        user[k].modifyPhone(input("수정할 전화번호 입력 : "));
                    elif choice == 5:
                        user[k].modifyGrade(input("수정할 직책 입력 : "));
                    else:
                        raise Exception;
                    print("인사 정보 수정이 완료 되었습니다.");
                except ValueError:
                    print("숫자로 입력하세요.");
                except Exception:
                    print("없는 메뉴 번호입니다.")
        elif select ==3:
            k=func(select)
            if k != None:
                print(f"{user[k].name} 님의 정보를 삭제합니다.");
                user.pop(k); 
        elif select ==4:
            choice = input("1. 이름 검색 2. 전체 검색 :");
            if choice == '1':
                k=func(select)
                if k!= None:
                    print(user[k])
            elif choice == "2":
                for i in range(len(user)):
                    print(user[i]);
            else:
                print("없는 메뉴 번호 입니다.")
        elif select ==0:
            print("종료합니다.");
            break;
        else:
            print("메뉴 번호가 없습니다.");
    except ValueError as e:
        print("숫자로 입력하세요");