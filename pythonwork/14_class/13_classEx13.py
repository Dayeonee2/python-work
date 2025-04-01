class Parent1():
    def __init__(self):
        self.school = "케이지고"; # Parent1에서 사용하는 고정값
        self.grade = "3학년"; # Parent1에서 사용하는 고정값
        self.group = "1반"; # Parent1에서 사용하는 고정값
    def __str__(self):
        return f"{self.school}학교, {self.grade}, {self.group}";

class Child1(Parent1):
    def __init__(self):
        super().__init__();
        self.group = "2반"; # Child1에서 사용하는 고정값
        
class Child2(Parent1):
    def __init__(self):
        super().__init__();
        self.grade = "2학년"; # Child2에서 사용하는 고정값

p1 = Parent1();
print(p1);
c1 = Child1();
print(c1);

c2 = Child2();
print(c2);