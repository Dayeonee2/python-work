# id() : 변수의 값의 위치를 출력하는 함수
# 파이썬은 모든 데이터(변수의 값)를 참조형으로 사용함
num1 = 100;
print(id(num1));
num2 = 100;
print(id(num2));
num2 = 200;
print(id(num2));

num1 = 10;
num2 = 20;
print('num1(',num1,') + num2(',num2,') =',num1+num2);

#선생님 답
print("num1( %d ) + num2( %d ) = %d"%(num1,num2,num1+num2));
print("num1( {} ) + num2( {} ) = {}".format(num1,num2,num1+num2));
print(f"num1( {num1} ) + num2( {num2} ) = {num1+num2}"); # 편리함
