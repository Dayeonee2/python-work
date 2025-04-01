#quizz1 선생님 풀이
# 연산식 문제를 list 구현 해 보세요
# 123+2*3-4/2

data = input("연산식 입력 : ");

# 숫자만 저장
dataLs = [];
# 기호만 저장
operLs = [];
# 문자열로 받은 숫자를 저장할 변수 - 정수형으로 저장
num = '';
# 곱셈과 나눗셈은 연산된 값, 더하기와 빼기는 들어갈 값 저장
numLs = [];
# 더하기 빼기 기호만 순서대로 저장(곱셈, 나눗셈은 이미 연산이 된 값)
indexLs = [];

#dataLs 와 operLs 에 각 데이터를 저장 for 문
for i in range(len(data)):
    if data[i].isdigit():
        num+=data[i];
        if i == len(data)-1:
            dataLs.append(int(num));
    else:
        last = data[i-1];
        if i==0 and data[i]=='-':
            num='-'
        elif (data[i]=='-') and (last[i]=="+" or last[i] =='-' or last[i] =='*' or last[i] =='*'):
            num='-'
        else:
            dataLs.append(int(num));
            num='';
            operLs.append(data[i]);
        
for i in range(len(operLs)):
    if operLs[i] =='+' or operLs[i]=='-':
        if i==0:
            #단일연산: 4+4
            if len(operLs) == 1 and operLs[i] == "+":
                numLs.append(dataLs[i] + dataLs[i+1]);
            elif len(operLs) == 1 and operLs[i] == "-":
                numLs.append(dataLs[i] - dataLs[i+1]);
            #복합연산:4+4-4
            elif operLs[i+1]=='+':
                numLs.append(dataLs[i]+dataLs[i+1]); 
            elif operLs[i+1]=='-':
                numLs.append(dataLs[i]-dataLs[i+1]);
            else: # 뒤에 연산자가 +,-가 아니면 즉, 4+4*4 자신의 값 저장
                numLs.append(dataLs[i]);
                indexLs.append(operLs[i])
        elif (len(operLs)>i+1) and (operLs[i+1]=='*' or operLs[i+1]=='/'):
            indexLs.append(operLs[i]) # 값 안넣고 +,-만 저장 
        else:
            numLs.append(dataLs[i+1])
            indexLs.append(operLs[i])
    elif operLs[i]=="*":
        if (len(numLs)!=0) and (operLs[i-1]=="*" or operLs[i-1]=='/'):
            tmp=numLs[len(numLs)-1]*dataLs[i+1];#numLs는 곱하기 계산된값
            numLs.pop();
            numLs.append(tmp)
        else:
            numLs.append(dataLs[i]*dataLs[i+1])
    elif operLs[i]=='/':
        if (len(numLs)!=0) and operLs[i-1]=="*" or operLs[i-1]=='/':
            tmp=numLs[len(numLs)-1]/dataLs[i+1];
            numLs.pop();
            numLs.append(tmp)
        numLs.append(dataLs[i]/dataLs[i+1])


result =0;
if len(numLs)==1: # * /로만 이루어져서 +,-가 없는 경우 결과값이 나오지 않음
    result=numLs[0]


for i in range(len(indexLs)):
    if i==0: # 1+2 의 1 저장
        result= numLs[i]
    if indexLs[i]=="+": # 1에서 2 더하기
        result+=numLs[i+1];
    elif indexLs[i]=="-":
        result-=numLs[i+1];

 
print("result : ", result);        
print("dataLs : ", dataLs);
print('operLs : ', operLs);
print('numLs : ', numLs);
print('indexLs : ', indexLs);
