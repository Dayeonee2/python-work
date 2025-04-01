# 문제
# 이름, 국어, 영어 점수를 입력받고 출력하는 함수를 만들고 예외가 발생하지 않도록
# for 문이나 while 문으로 해서 구현 해 보세요 .
class Score():
    def __init__(self):
        self.name = input("이름 입력 : ");
        self.kor = int(input("국어 점수 입력 : "));
        self.eng = int(input("영어 점수 입력 : "));
    def __str__(self):
        return f"{self.name} 님, 국어 {self.kor}점, 영어 {self.eng}점";

n = 3
idx = 1;
for i in range(n):
    print(f"{i+1}회");
    i += 1;
    try:
        s = Score();
        print(s);
    except:
        print("점수는 숫자만 가능 합니다.");