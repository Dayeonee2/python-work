class Hello:
    def __enter__(self):
        print("enter")
        return self;
    
    def sayHello(self,name):
        print(f"hello, {name}");
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit");    

#파일 읽어올 때        
with Hello() as h:
    # 생성 -> 사용 -> 종료 : 라이프사이클을 가진다.
    h.sayHello("홍길동");
    h.sayHello("이순신");