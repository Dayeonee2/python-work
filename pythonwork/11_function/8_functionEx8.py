# 전역변수(global)
# 파이썬 파일 안에서 사용할 수 있는 변수

num = 1;

def func():
    # 함수안에서 생성하는 변수 : 지역변수(local)
    # 지역변수는 함수가 종료되면 없어지는 변수
    num=100;
    print(f"{num}");

def func1():
    # 같은 이름의 변수가 없으면 전역변수 사용
    print(f"{num}"); 
    
func();
func1();
print(f"{num}");