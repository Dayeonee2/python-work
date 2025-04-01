# 문제 : 야구게임
# num = 876
# 세자리 숫자 입력 받기 
# 자리와 숫자가 맞으면 스트라이크
# 숫자만 맞으면 볼
# 입력한 숫자 아무것도 없으면 아웃
# 10회 이내로 정답 찾기

num='876'
for i in range(10):
    qa=input("세자리 숫자를 입력하세요 : ");
    strike=0
    ball=0
    for j in range(3):
        for k in range(3):
            if j==k and num[j]==qa[k]:
                strike+=1
            elif j!=k and num[j]==qa[k]:
                ball+=1
    if strike==0 and ball==0:
        print('아웃입니다.');
    elif strike==3:
        print('정답입니다');
        break
    else:
        print(f"{strike} 스트라이크, {ball}  볼")