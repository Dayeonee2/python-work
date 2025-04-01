while True:
    num=input('숫자 5개를 입력하세요 : ');
    if num.isdigit()==False:
        print('문자가 아닌 숫자를 입력하세요.');
    else:
        if len(num)<5:
            print('숫자 5개를 입력하세요.');
        else:
            break
num=list(num)
num1=int(num[0])*100+int(num[1])*10+int(num[2])
num2=int(num[3])*int(num[4])
print(f'{num1}+{num[3]}*{num[4]}={num1+num2}');


while True:
    num3=input('숫자를 입력하세요: ');
    if num3.isdigit()==False:
        print('문자가 아닌 숫자를 입력하세요 : ');
    else:
        break;
    
result='';
for i in range(9,-1,-1):
    for j in range(len(num3)):
        if int(num3[j])==i:
            result+=num3[j];
print(f"가장 큰 수는 : {result}")


