def func(num1,num2 = 100):
    print(f"{num1} : {num2}");

#기본값을 함수로 넘길 때 : 매개변수 = 값
func(10,20);
func(10);

def func(num1=100):
    print(f"{num1}");
    
func(10);
func();

# 기본 값이 있는 매개변수는 맨 뒤에 넣어야 한다.
# 이유는 생략이 가능해야 하기 때문이다.
# def func(num1=100 ,num2):
#     print(f"{num1} : {num2}");
    
# func(10,20);
# func(,20);
