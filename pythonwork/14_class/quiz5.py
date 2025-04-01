class Parent():
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
                 
    def __init__(self):
        self.name = input("이름 입력 : ");
        self.kor = self.digitCheck("국어");
        self.eng = self.digitCheck("영어");
        self.math = self.digitCheck("수학");
        self.sum = self.kor + self.eng + self.math;
        self.avg = self.sum / 3;
        
    def __str__(self):
        return f"{self.name} 님의 총점은 {self.sum} 평균은 {self.avg} 입니다.";
        
class Child(Parent):                 
    def __init__(self,sum):
        self.music = super().digitCheck("음악");
        self.exer = super().digitCheck("체육");
        self.sum= sum + self.music + self.exer;
        self.avg = self.sum / 5; 
        
    def __repr__(self,name):
        print(f"{name} 님의 총점은 {self.sum} 평균은 {self.avg} 입니다.");

        
s = Parent(); #값은 객체s가 저장하고 있어서 값을 불러오려면 변수를 사용해야함.
print(s);

c = Child(s.sum);
print(c.__repr__(s.name)); #None은 왜 실행?