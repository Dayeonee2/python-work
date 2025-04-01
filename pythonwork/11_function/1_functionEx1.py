# 함수
# def [함수이름](매개변수):
# 함수는 호출해야만 사용할 수 있다.
def add():
    num1=int(input("첫번째 정수 입력 : "));
    num2=int(input("두번째 정수 입력 : "));

    print(f"{num1} + {num2} = {num1+num2}");
    
# 함수 호출 : 함수이름()
add();