# 함수이 반환데이터는 1개만 가능하다.
# list도 하나, 딕셔너리도 하나, 값도 하나만 가능하다.
def func():
    num1 = int(input("첫번째 정수 입력 : "));
    num2 = int(input("두번째 정수 입력 : "));
    print(f"{num1}, {num2}");
    return num1,num2 # , 가 있으면 튜플로 봄
    
    
num1,num2=func(); # 튜플을 언팩   
print(f"{num1}, {num2}");

def func1():
    ls=[1,2,3,]
    dict={1:"1",2:"2"};
    return ls,dict # , 가 있으면 튜플로 봄

ls,dict=func(); # 튜플을 언팩   
print(f"{ls}, {dict}");
