#문제
#학생 성적 프로그램
#클래스 : 이름 , 국어 , 영어 , 수학, 평균, 총점
#입력, 수정, 삭제, 검색

class Student():
    def __init__(self):
        self.name= input("이름 입력 : ")
        self.kor = self.digitCheck("국어");
        self.eng = self.digitCheck("영어");
        self.math = self.digitCheck("수학");
        self.scoreOper();
    
    def digitCheck(self, sub):
        while True:
            score = input(f"{sub} 점수 입력 : ");
            if score.isdigit():
                if 0<=int(score)<=100:
                    return int(score); #break와 같은 기능
                else:
                    print("0 ~ 100 사이 정수만 가능합니다.");
            else:
                print("점수는 숫자만 가능합니다.");
        
    def scoreOper(self):
        self.total = int(self.kor) + int(self.eng) + int(self.math);
        self.avg = self.total / 3

    def output(self):
        print(f"{self.name}님의 총합은 {self.total}, 평균은 {self.avg} 입니다.");

    def modify(self):
        self.kor = self.digitCheck("수정할 국어");
        self.eng = self.digitCheck("수정할 영어");
        self.math = self.digitCheck("수정할 수학");               
        self.scoreOper();
        
def func(sub):
    name= input(f"{sub}할 학생 이름 입력 :");
    for i in range(len(studentif)): #이름이 있는지 확인
        if name == studentif[i].name: #이름이 있다면
            print(f"{name}학생");
            print(f"국어 : {studentif[i].kor} 점");
            print(f"영어 : {studentif[i].eng} 점");
            print(f"수학 : {studentif[i].math} 점");
            return i   #studendif의 인덱스 번호 반환         
        else:
            print(f"{name} 이 없습니다. 다시 확인하세요.");
studentif=[];

menu= "1. 입력", "2. 수정", "3. 삭제", "4. 검색";
        
while True:
    for i in menu:
        print(f"{i}");
    print("0. 종료");
    select = input("메뉴 입력 : ");
    if select =='1':
        stu = Student();
        stu.output()
        studentif.append(stu);
    elif select =='2':
        k=func("수정"); #이름의 studentif 인덱스번호가 k
        if k != None:
            studentif[k].modify();
    elif select =='3':
        k=func("삭제");
        if k != None:
            studentif.pop(k);
    elif select =='4':
        func("검색");
    elif select =='0':
        print("종료합니다.");
        break;
    else:
        print('메뉴 번호가 없습니다.');