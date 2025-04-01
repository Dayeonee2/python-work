# 문제 
# 학생 성적 프로그램
# 클래스 : 이름, 국어, 영어, 수학, 평균, 총점
# 입력, 수정, 삭제, 검색
class Score:
    def digitCheck(self, sub):
        while True:
            score = input(f"{sub} 점수 입력 : ");
            if score.isdigit():
                if 0 <= int(score) <= 100:
                    return int(score);
                else : 
                    print("0 ~ 100 사이 점수만 가능 합니다.");
            else:
                print("점수는 숫자만 가능 합니다.");
    
    def result(self):
        self.sum = self.kor + self.eng + self.math;
        self.avg = self.sum / 3;
    
    def __init__(self, stuId):
        self.stuId = stuId;
        self.name = input("이름 입력 : ");
        self.kor = self.digitCheck("국어");
        self.eng = self.digitCheck("영어");
        self.math = self.digitCheck("수학");
        self.result();

    def __str__(self):
        return f"""
### {self.stuId} ###
이름 : {self.name}
총점 : {self.sum} 점
평균 : {self.avg} 점""";

    def modify(self):
        self.kor = self.digitCheck("수정할 국어");
        self.eng = self.digitCheck("수정할 영어");
        self.math = self.digitCheck("수정할 수학");
        self.result();

    def find(self, stuId):
        if self.stuId == stuId:
            return True;
        else:
            return False;
    # 단일 객체는 삭제 되었을 때 잘 실행 된다.
    # 리스트에 포함 되어 있으면 소멸에 대한 정보가 제대로 처리 되지 않는다.
    # while 에 포함 해서 사용하는 것은 좋은 방법이 아니다.
    # def __del__(self):
    #     print(f"{self.name} 정보가 삭제되었습니다.");

def func(select):
    print(f"### 성적 {sub[(int(select)-2)]} ###");
    stuId = input("학번 입력 : ");
    if stuId.isdigit():
        for i in scoreList:
            if i.find(int(stuId)):
                if select == "2":
                    i.modify();
                elif select == "3":
                    scoreList.remove(i); #for in 리스트: 리스트 안의 객체를 의미->remove(객체) i = scoreList[i]
                    print(f"{i.name} 님의 정보를 삭제합니다.");
                elif select == "4":
                    print(i);
                return;
        else:
            print(f"{stuId} 학번이 존재하지 않습니다. 다시 입력 하세요.");
    else:
        print("학번은 숫자로 입력하셔야 합니다. 다시 입력 하세요.");

scoreList = [];
stuId = 1001;
sub = "수정","삭제","검색";
menu = "1. 성적 입력", "2. 성적 수정", "3. 성적 삭제", "4. 성적 검색";

while True :
    for i in menu:
        print(f"{i}");
    print("0. 종료");
    select = input("메뉴 선택 : ");

    if select == "1":
        print("### 성적 입력 ###");
        s = Score(stuId);
        scoreList.append(s);
        stuId+=1;
    elif select == "2" or select == "3" or select == "4":
        func(select);
    elif select == "0":
        print("프로그램을 종료합니다.");
        break;
    else:
        print("선택한 메뉴가 없습니다. 다시 입력 하세요.");