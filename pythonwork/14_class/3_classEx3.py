class Student():
    # 데이터
    name = '';
    kor = 0;
    eng = 0;
    math = 0;
    sum = 0;
    avg = 0;

    # 기능 
    # 클래스안의 함수에 제일 처음 매개변수는 self 해야 한다.
    # self 는 객체 자신을 의미한다.
    def scoreOper(self, name, kor, eng, math):
        self.name = name;
        self.kor = kor;
        self.eng = eng;
        self.math = math;
        self.sum = kor + eng + math;
        self.avg = self.sum / 3
    
    def scoreOutput(self):
        print(f"{self.name} 님 : 총점 {self.sum} 점, 평균 {self.avg} 점");

# 인스턴스 생성
stu1Class = Student();
stu1Class.scoreOper("홍길동", 100, 90, 80);
stu2Class = Student();
stu2Class.scoreOper("이순신", 90, 80, 80);

stu1Class.scoreOutput(); #홍길동 님 : 총점 270 점, 평균 90.0 점
stu2Class.scoreOutput(); #이순신 님 : 총점 250 점, 평균 83.33333333333333 점

print(stu1Class.name);
print(stu2Class.name);

stu1Class.name = "김유신";
print(stu1Class.name);
print(stu2Class.name);