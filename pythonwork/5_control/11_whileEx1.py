# for : 횟수가 정해진 반복 - 유한 반복
# range(시작, 끝, 증감)
# while : 횟수가 아닌 조건에 의한 반복 - 무한 반복
# while 문은 조건만 있다.

# while문 외부에  시작값을 생성한다.
# 0 만 컴퓨터에서 False-> 다른 수 넣으면 조건 없을 때 무한반복
i = 0;

# while문에는 종료 조건을 생성한다.
while i < 5:
    print(i);
    #while문 내부에 증감값을 생성한다.
    i+=1;

print("while문 종료");