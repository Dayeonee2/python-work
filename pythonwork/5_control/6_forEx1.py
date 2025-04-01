# range(시작,끝, 증감) : 시작~끝-1 까지 증감값만큼 값이 커지거나 작아짐
# for i in range(1,10,1):
#     print(i);


# range() : 기본 증감값은 +1 이다. 생략이 가능
# for i in range(1,10):
#     print(i);


# # range() : 기본 시작값은 0이다. 생략이 가능
# for i in range(10):
#     print(i);

# range() : 숫자가 하나가 들어가면 종료값으로 인식.
# for i in range(1):
#     print(i);

# range 함수 안에 숫자가 하나만 들어가면 종료값으로 인식
# range 함수 안에 숫자가 두개가 들어가면 시작값, 종료값으로 인식

# for i in range(10,2):
#     print(i);

# 증감값을 지정하려고 하면 모든 옵션의 숫자를 입력해야 한다.
# for i in range (0,10,2):
#     print(i);

for i in range(10,0,-1):
    print(i);

# for문의 시작은 0부터 시작하고 이유는 나중에 배우는 list 때문이다.
# list의 인덱스 시작값이 0부터 시작하기 때문이다.