class Parent1():
    def aaa(self):
        print("aaa 메서드");
        
class Parent2():
    def bbb(self):
        print("bbb 메서드");
    
    
#파이썬에서는 다중 상속을 지원한다.
class Child(Parent1, Parent2):
    def ccc(self):
        print("ccc 메서드");
        
c = Child();
c.aaa();
c.bbb();
c.ccc();
    