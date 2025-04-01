#문제
#이름, 국어, 영어, 수학 점수를 입력 받고 총점, 평균을 출력하도록 구현
#점수는 0~100 사이만 가능
#숫자가 아닌 값을 입력해도 에러 없이 처리 되도록 구현
name=input('이름을 입력하세요 : ');

while True:        
    kor=input('국어 점수를 입력하세요 : ');
    if kor.isdigit()==False:
        print('숫자를 입력하세요.')
        continue;
    elif int(kor)<0 or int(kor)>100:
        print('0 ~ 100 사이의 수를 입력하세요')
    else:
        break;
while True:        
    eng=input('영어 점수를 입력하세요 : ');
    if eng.isdigit()==False:
        print('숫자를 입력하세요.')
        continue;
    elif int(eng)<0 or int(eng)>100:
        print('0 ~ 100 사이의 수를 입력하세요')
    else:
        break;
while True:
    math=input('수학 점수를 입력하세요 : ');
    if math.isdigit()==False:
        print('숫자를 입력하세요.')
        continue;
    elif int(math)<0 or int(math)>100:
        print('0 ~ 100 사이의 수를 입력하세요')
    else:
        break;
kor=int(kor)
eng=int(eng)
math=int(math)
print("\n\n")
print("%-5s%-6s%-6s%-6s%-6s%-6s"%('이름','국어','수학','영어','총점','평균'));
print(f"{name}\t{kor}\t{math}\t{eng}\t{kor+eng+math}\t{(kor+eng+math)/3:.1f}");

#선생님 풀이
