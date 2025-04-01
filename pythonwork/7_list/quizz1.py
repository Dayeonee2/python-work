# 연산식 list 구현해보세요.
# 문제


# 연산식을 저장하는 변수
data = input('연산식 입력 : ');
# 연산기호만 저장하는 list
operData=[];
# 정수만 저장하는 list
numData=[];
# 숫자를 저장하는 변수, 문자열+문자열 문자열이 합쳐지게 된다.
num= '';

#enumerate() : 인덱스와 데이터의 값을 하나씩 출력
for i , s in enumerate(data):
    if s.isdigit(): #한글자씩 가져오는데 그 글자가 숫자일때
        num+=s;
        if i==len(data)-1 :
            numData.append(int(num));
    else:
        operData.append(s);
        numData.append(int(num));
        num='';

# 결과값을 저장하는 변수
result=0;
#처음여부를 구분하는 변수
checkCnt= -1;

# * / 결과값
result_=[]

for i in range(len(operData)):# *,/ 를 먼저 계산
    if operData[i]=="*":
        result = numData[i]*numData[i+1];
        result_.append(result)
    elif operData[i]=="/":
        result = numData[i]/numData[i+1];
        result_.append(result)
    
if operData[0]=='*' or operData[0]=='/':
    if operData.count('*')>=1:
        for i in range(operData.count('*')):
            operData.remove('*');
    elif operData.count('/')>=1:
        for i in range(operData.count('/')):
            operData.remove('/');    

        
print(f"operData : {operData}");
print(f"numData : {numData}");
print(f"result_ : {result_}");


    for i in range(len(operData)):        
        if operData[i]=="+" and checkCnt==-1:
            result = result_[i]+result_[i+1];
            checkCnt+=1
        elif operData[i]=="-" and checkCnt==-1:
            result = result_[i]-result_[i+1];
            checkCnt+=1
        elif operData[i] =='+':
            if i==0: #연산식이 더하기로 시작할때
                result+=result_[i];
            else: # 연산식이 더하기로 시작하지 않을 때
                result += result_[i];
        elif operData[i] =='-':
            if i==0: # 연산식이 빼기로 시작할때
                result-=result_[i];
            else: # 연산식이 빼기로 시작하지 않을 때
                result -= result_[i];

else:
    if operData.count('*')>=1:
        for i in range(operData.count('*')):
            operData.remove('*');
    elif operData.count('/')>=1:
        for i in range(operData.count('/')):
            operData.remove('/');    

        
    print(f"operData : {operData}");
    print(f"numData : {numData}");
    print(f"result_ : {result_}");


    for i in range(len(operData)):        
        if operData[i]=="+" and checkCnt==-1:
            result = numData[i]+result_[i];
            checkCnt+=1
        elif operData[i]=="-" and checkCnt==-1:
            result = numData[i]-result_[i];
            checkCnt+=1
        elif operData[i] =='+':
            result = numData[i]+result_[i]
            if i==0: #연산식이 더하기로 시작할때
                result+=numData[i];
            else: # 연산식이 더하기로 시작하지 않을 때
                result += result_[i];
        elif operData[i] =='-':
            if i==0: # 연산식이 빼기로 시작할때
                result-=numData[i];
            else: # 연산식이 빼기로 시작하지 않을 때
                result -= result_[i];
           

print(f"결과값 : {result}");        
print(f"operData : {operData}");
print(f"numData : {numData}");


