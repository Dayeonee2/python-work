class ScoreParent():
    def __init__(self):
        self.name = input("이름 입력 : ");
        self.kor = int(input("국어 점수 입력 : "));
        self.eng = int(input("영어 점수 입력 : "));
        self.math = int(input("수학 점수 입력 : "));
        self.sum = self.kor + self.eng + self.math;
        self.avg = self.sum / 3
    def __str__(self):
        return f"{self.name} 님의 총점은 {self.sum}점 이고, 평균은 {self.avg}점 입니다."

class ScoreChild(ScoreParent):
    def __init__(self):
        super().__init__();
        self.music = int(input("음악 점수 입력 : "));
        self.sports = int(input("체육 점수 입력 : "))
        self.sum += self.music + self.sports;
        self.avg = self.sum / 5
s = ScoreParent();
print(s);
c = ScoreChild();
print(c);