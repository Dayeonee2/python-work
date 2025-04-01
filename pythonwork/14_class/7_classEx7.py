class Student():
    def __init__(self): # 초기화
        self.name = input("이름 입력 : ");
        self.age = input("나이 입력 : ");
    def output(self):
        print(f"{self.name} 님의 나이는 {self.age} 살 입니다.");
    def __str__(self): # 문자열을 반환
        return f"{self.name} 님의 나이는 {self.age} 살 입니다."; #output과 똑같이 출력됨
    def __repr__(self): # __str__과 같음.
        return f"{self.name} ";
    def __del__(self): # 소멸자
        print(f"{self.name} 객체가 삭제되었습니다.");


stu=Student();
stu.output();
print(stu); ##__str__ 실행됨 없으면 __repr__ 실행됨
stu.__del__(); # 매서드 실행으로 객체가 삭제되지는 않는다.
#del stu; # del : 객체(리스트, 딕셔너리, 인스턴스, 내장함수) 삭제
#stu.output();
print(stu.__repr__());
