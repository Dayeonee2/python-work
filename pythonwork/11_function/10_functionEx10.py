# 전역변수는 함수에서 먼저 선언한다.
# 선언 후에 초기화를 해야한다.
# 초기화 후 연산도 가능하다.
# def func():
#     global cnt;
#     cnt=0;
#     cnt+=1;
#     print(f"전역변수 : {cnt}")
#     cnt+=1;
    
# func();
# print(f"{cnt}")
 
def funt():
    global num1,num2;
    num1=int(input("첫번째 정수 입력 : "));
    num2=int(input("두번째 정수 입력 : "));
    
num1,num2=0,0; 

    
funt(); 
print(f"{num1}, {num2}");
