# 함수는 기본적으로 4가지 형태
# 매개변수 : 함수를 호출할 때 데이터를 넘겨받는 변수

# 1. 매개변수 없고 반환데이터가 없는 경우 - 출력
def output():
    print("#### 계산기 ####");
    
# 2. 매개변수 없고 반환데이터가 있는 경우
def inputNum():
    num=int(input("정수 입력 : "));
    # return :  데이터를 반환할 때 사용하거나 함수를 종료할 때 사용한다.
    return num;

# 3. 매개변수 있고 반환데이터가 없는 경우
def result(num1,num2):
    print(f"{num1} + {num2} = {num1+num2}");
    
# 4. 매개변수 있고 반환데이터가 있는 경우
def different(num1):
    num1+=1000;
    print(num1);
    return num1;

output();
num1=inputNum();
num2=inputNum();
#함수로 전달하는 변수와 매개변수는 다른 변수다.
result(num1,num2);
num3=different(num1);
print(num1);
print(num3);
