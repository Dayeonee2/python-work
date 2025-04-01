# 대입 연산자, 복합대입연산자
# = : 오른쪽의 식이나 결과값을 왼쪽에 대입해라
# += : a+=b : a = a+b
# -= : a-=b : a = a-b
# *= : a*=b : a = a*b
# /= : a/=b : a = a/b
# //= : a//=b : a = a//b
# %= : a%=b : a = a%b
# **= : a**=b : a = a**b

num1=10;
num2=5;
num1+=num2; # num1=num1+num2
print(num1);#15
num1-=num2; #num1 = num1-num2
print(num1);#10
num1*=num2; #num1=num1*num2
print(num1);#50
num1/=num2; #num1=num1/num2
print(num1)#10
num1//=num2; #num1=num1//num2
print(num1)#2
num1%=num2;
print(num1)#2
num1**=num2; #num1= num1**num2
print(num1)#32