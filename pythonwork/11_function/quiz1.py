# 사칙연산 프로그램
# 두개의 정수를 입력 받고 +,-,*,/ 중 선책
# 결과값을 출력
# 함수로 만들 수 있는 부분을 생각하고 함수로 만들어 보세요.

def intNum(sub):
    num=input(f"{sub} 입력 : ");
    return num;

def result(num1,num2,oper):
    if oper == "+":
        print(f"{num1} + {num2} = {num1+num2}");
    elif oper=="-":
        print(f"{num1} - {num2} = {num1-num2}");
    elif oper=='*':
        print(f"{num1} * {num2} = {num1*num2}");
    elif oper=="/":
        print(f"{num1} / {num2} = {num1/num2:.2f}");

num1=int(intNum("첫번째 정수"));
num2=int(intNum("두번째 정수"));
oper=intNum("연산자")
result(num1,num2,oper);