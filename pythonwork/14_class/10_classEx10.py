class Parent():
    def aaa(self):
        print("부모 aaa 메서드");
        
class Child():
    # override : 부모 클래스의 함수를 자식 클래스가 변경하는 것을 의미한다.
    def aaa(self): # override 부모와 자식의 함수명이 같음
        print("자식 aaa 메서드");
    def aaa(self,num):
        print(f"{num}")
        
p = Parent();
p.aaa();
c = Child();
c.aaa();
