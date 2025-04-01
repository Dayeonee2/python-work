# __init__() : 객체 생성시 객체의 데이터를 초기화하는 함수
class Student():
    name = '';
    age = '';
    
    #객체 생성시 무조건 실행 호출하지 않아도
    def __init__(self):
        self.name = input("이름 입력 : ");
        self.age = input("나이 입력 : ");
        
    def output(self):
        print(f"{self.name} 님의 나이는 {self.age} 살 입니다.");

stu1= Student();
stu1.output();
stu2= Student();
stu2.output();