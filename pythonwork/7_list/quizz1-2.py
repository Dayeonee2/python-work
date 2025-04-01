goal=input('연산 입력: ')  #str 상태로 받음 (ex. "123+4+5")
current='';
# lastNum=[];
Lst=[];
first=True
last=False

#-----------------------
# 사용자가 쓴 str을 각 리스트로 옮기기
print(goal)
for i in goal:
    if i.isdigit(): #숫자인 경우
        current+=i

    else:
        current+= " " + i + " "
Lst=current.split(" ") #공백을 기준으로 list변환해서 적용

print(Lst)

# 리스트 내 값이 숫자이면 int로 변환하여 그 자리에 넣기
for idx,val in enumerate(Lst):
    if val.isdigit():
        Lst[idx]=int(val)
print(Lst)

# 나누기 연산자가 리스트에 있는 경우 실행
while len(Lst) > 1 :
    if "/" in Lst:
        idx=Lst.index("/")   #/의 인덱스 확인
        rlt= Lst[idx-1] / Lst[idx+1]   #나눗셈 연산자 전, 후의 값으로 나눈 결과
        del Lst[idx-1:idx+2]   #연산이 끝난 값은 삭제
        Lst.insert(idx-1,rlt)
        print(f'나누기 후: {Lst}')

    elif "*" in Lst:
        idx=Lst.index("*")   #*의 인덱스 확인
        rlt= Lst[idx-1] * Lst[idx+1]   #곱셈 연산자 전, 후의 값으로 곱한 결과
        del Lst[idx-1:idx+2]   #연산이 끝난 값은 삭제
        Lst.insert(idx-1,rlt)
        print(f'곱셈 후: {Lst}')

    elif "-" in Lst:
        idx=Lst.index("-")   #+의 인덱스 확인
        rlt= Lst[idx-1] - Lst[idx+1]   #뺄셈 연산자 전, 후의 값으로 뺀 결과
        del Lst[idx-1:idx+2]   #연산이 끝난 값은 삭제
        Lst.insert(idx-1,rlt)
        print(f'뺄셈 후: {Lst}')

    elif "+" in Lst:
        idx=Lst.index("+")   #-의 인덱스 확인
        rlt= Lst[idx-1] + Lst[idx+1]   #덧셈 연산자 전, 후의 값으로 더한 결과
        del Lst[idx-1:idx+2]   #연산이 끝난 값은 삭제
        Lst.insert(idx-1,rlt)
        print(f'덧셈 후: {Lst}')



print(Lst)

# 검수작업
print(f'컴퓨터의 답은: {35-8*13/4}')